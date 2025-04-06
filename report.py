from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf_report(data, filename):
    c = canvas.Canvas(filename, pagesize=letter)
    _, height = letter
    y = height - 40

    for row in data:
        text = f"ID: {row[0]}, Device ID: {row[1]}, Action: {row[2]}, Timestamp: {row[3]}"
        c.drawString(40, y, text)
        y -= 20
        if y < 40:
            c.showPage()
            y = height - 40

    c.save()
