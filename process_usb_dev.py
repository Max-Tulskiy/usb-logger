import sqlite3
import pyudev
import pytz
from datetime import datetime

device_registry = {}

def init_db():
    conn = sqlite3.connect("usb_devices.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usb_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id TEXT,
            action TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def log_event(device_id, action):
    if device_id == "Unknown":
        return

    moscow_tz = pytz.timezone("Europe/Moscow")
    utc_now = datetime.now(pytz.utc)
    moscow_now = utc_now.astimezone(moscow_tz)
    timestamp = moscow_now.strftime('%Y-%m-%d %H:%M:%S')

    conn = sqlite3.connect("usb_devices.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usb_events (device_id, action, timestamp) VALUES (?, ?, ?)", (device_id, action, timestamp))
    conn.commit()
    conn.close()

def monitor_usb():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='usb')

    for device in iter(monitor.poll, None):
        if device.action == 'add':
            device_id = device.get('ID_SERIAL') or device.get('DEVNAME') or 'Unknown'
            device_registry[device.sys_name] = device_id
        elif device.action == 'remove':
            device_id = device_registry.pop(device.sys_name, None)
            if not device_id and device.parent:
                device_id = device.parent.get('ID_SERIAL', 'Unknown')
            if not device_id:
                device_id = 'Unknown'

        log_event(device_id, device.action)

def update_unreliable_events():
    conn = sqlite3.connect("usb_devices.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT a.id, a.device_id
        FROM usb_events a
        WHERE a.action = 'add'
        AND NOT EXISTS (
            SELECT 1 FROM usb_events b
            WHERE b.device_id = a.device_id
              AND b.action = 'remove'
              AND b.timestamp > a.timestamp
        )
    """)
    rows = cursor.fetchall()

    for event_id, device_id in rows:
        cursor.execute("""
            UPDATE usb_events
            SET action = 'Unreliable'
            WHERE id = ? AND action = 'add'
        """, (event_id,))

    conn.commit()
    conn.close()
