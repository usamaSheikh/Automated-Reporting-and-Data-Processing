import matplotlib.pyplot as plt
from fpdf import FPDF
import pandas as pd

def generate_charts(total_sales_by_region, avg_monthly_sales):
    """
    Generate charts for the report.
    """
    # Plot total sales by region
    plt.figure(figsize=(8, 6))
    total_sales_by_region.plot(kind='bar', color='skyblue')
    plt.title('Total Sales by Region')
    plt.ylabel('Sales ($)')
    plt.savefig('reports/total_sales_by_region.png')
    plt.close()

    # Plot average monthly sales
    plt.figure(figsize=(8, 6))
    avg_monthly_sales.plot(kind='line', marker='o', color='green')
    plt.title('Average Monthly Sales')
    plt.ylabel('Sales ($)')
    plt.savefig('reports/avg_monthly_sales.png')
    plt.close()

def generate_pdf_report(total_sales_by_region, avg_monthly_sales):
    """
    Generate a PDF report with sales data and visualizations.
    """
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # First page
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, txt="Sales Report", ln=True, align='C')

    pdf.set_font('Arial', '', 12)
    pdf.cell(200, 10, txt="Total Sales by Region:", ln=True)

    # Add the chart image
    pdf.image('reports/total_sales_by_region.png', x=10, y=30, w=180)
    pdf.ln(100)  # move cursor down

    pdf.cell(200, 10, txt="Average Monthly Sales:", ln=True)
    pdf.image('reports/avg_monthly_sales.png', x=10, y=140, w=180)
    
    # Save the PDF
    pdf.output("reports/sales_report.pdf")
    print("PDF report generated: reports/sales_report.pdf")

if __name__ == "__main__":
    from data_extraction import load_data
    from data_processing import process_data

    # Load and process the data
    data = load_data("data/sales_data.csv")
    
    if data is not None:
        total_sales_by_region, avg_monthly_sales = process_data(data)
        
        # Generate charts and PDF report
        generate_charts(total_sales_by_region, avg_monthly_sales)
        generate_pdf_report(total_sales_by_region, avg_monthly_sales)
