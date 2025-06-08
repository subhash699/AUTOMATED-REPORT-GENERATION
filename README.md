# AUTOMATED-REPORT-GENERATION

COMPANY: CODTECH IT SOLUCTIONS

NAME: SUBHASH K

INTERN ID: CT04DG769

DOMAIN: PYTHON PROGRAMMING

DURATION: 4 WEEKS

MENTOR: NEELA SANTOSH

As part of my internship at **CodTech IT Solutions Pvt. Ltd.**, I was assigned **Task 2: Automated Report Generation** under the domain of Python programming. The primary objective of this task was to design and implement a Python script that could read data from a file, analyze the information, and then generate a structured and well-formatted PDF report using a reporting library such as FPDF. This task aimed to simulate a real-world scenario in which businesses and organizations need automated reporting tools to handle large datasets and produce accurate, professional reports efficiently.

For the development environment, I used **IDLE Shell (Python 3.12.2)**. IDLE is Python’s official Integrated Development and Learning Environment. It is user-friendly, lightweight, and suitable for beginners and intermediate programmers to write, run, and debug Python code easily. The script was written in Python due to its simplicity, readability, and the vast collection of libraries it offers for data processing and report generation. The script was divided into three main phases: data reading, data analysis, and PDF generation.

To begin with, I prepared a sample data file named `data.txt`. This file contained product sales data in CSV format with columns such as `Product`, `Quantity`, and `Price`. Example entries included: "Pen,10,1.5", "Notebook,5,2.0", etc. The Python script used the `csv` module to read this file. Each line was parsed using `csv.DictReader`, which made it easy to access each field by name. After reading the data, the script converted the quantities and prices into numerical formats for computation. The total quantity of items sold and the total sales value were calculated using simple arithmetic operations.

Once the data was processed, the next step was to generate a PDF report. For this, I used the **FPDF** library, a powerful tool for creating PDFs programmatically in Python. I created a custom PDF class that included a header titled "Sales Report" and a footer displaying the page number. The report included a detailed table with columns for product name, quantity sold, price per item, and total value per item. Additionally, a summary section was added at the end, displaying the total number of items sold and the overall sales value. The final PDF was saved as `sales_report.pdf` in the working directory.

This task is not just an academic exercise but also has **real-world applications** across multiple industries. For example, in **business environments**, such a script can be used for generating weekly or monthly sales reports. In **schools or colleges**, it could be adapted to generate student performance or attendance summaries. In the **healthcare sector**, it can be used to produce patient visit summaries or medication usage reports. Additionally, freelancers or consultants could use similar scripts to automate invoice generation and client billing. This type of automation reduces manual effort, increases accuracy, and enhances productivity.

Overall, this task helped me gain practical experience in Python programming, file handling, data analysis, and automated document generation. I learned how to integrate multiple Python modules into a single solution that performs a complete workflow—from reading raw data to producing a final report. It also taught me the value of automation and how such solutions can be scaled and adapted for professional use. This task significantly contributed to both my technical skills and real-world problem-solving abilities during the internship.

OUTPUT:

![Image](https://github.com/user-attachments/assets/2f334774-41ff-40c0-9060-94af9ce6939b)
![Image](https://github.com/user-attachments/assets/c78e05d3-722b-4938-99a4-1943bc0fbfd6)
