from fpdf import FPDF
import csv

data_file = 'data.txt'

products = []
with open(data_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        row['Quantity'] = int(row['Quantity'])
        row['Price'] = float(row['Price'])
        products.append(row)

total_items = sum(p['Quantity'] for p in products)
total_value = sum(p['Quantity'] * p['Price'] for p in products)


class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Sales Report', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)

pdf.cell(0, 10, "Product Sales Summary", ln=True)

pdf.set_font("Arial", 'B', 12)
pdf.cell(60, 10, "Product", 1)
pdf.cell(40, 10, "Quantity", 1)
pdf.cell(40, 10, "Price", 1)
pdf.cell(40, 10, "Total", 1)
pdf.ln()

pdf.set_font("Arial", size=12)
for p in products:
    total_price = p['Quantity'] * p['Price']
    pdf.cell(60, 10, p['Product'], 1)
    pdf.cell(40, 10, str(p['Quantity']), 1, align='R')
    pdf.cell(40, 10, f"${p['Price']:.2f}", 1, align='R')
    pdf.cell(40, 10, f"${total_price:.2f}", 1, align='R')
    pdf.ln()

pdf.ln(5)
pdf.set_font("Arial", 'B', 12)
pdf.cell(0, 10, f"Total Items Sold: {total_items}", ln=True)
pdf.cell(0, 10, f"Total Sales Value: ${total_value:.2f}", ln=True)

pdf.output("sales_report.pdf")

print("Report generated as sales_report.pdf")

import os
os.startfile("sales_report.pdf")
