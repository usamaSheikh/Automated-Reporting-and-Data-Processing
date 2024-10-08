# Automated Reporting and Data Processing

## Project Overview
This project demonstrates how to automate the generation of reports from a dataset, perform data analysis, and visualize the data. This project will include multiple files, allowing you to demonstrate automated data extraction, processing, report generation, and visualization.

### Features:
- Extracts sales data from a CSV file.
- Processes and calculates total sales by region and average monthly sales.
- Generates charts and saves them as PNG files.
- Compiles a report with the charts and exports it as a PDF.

### Technologies Used:
- Python
- `pandas` for data processing
- `matplotlib` for data visualization
- `fpdf` for PDF report generation

## How to Run:
1. Install Required Dependencies:
     - You need the following Python libraries:
     - pip install pandas matplotlib fpdf

2. Create Necessary Directories:
     - Create a data/ folder for the dataset and a reports/ folder to save the generated PDF reports and charts:
     - mkdir data reports

3. Place the Dataset in the data/ Folder:
     - Put the sales_data.csv file into the data/ folder.

4. Run the Scripts:
     - Run the data processing script:
     - python data_processing.py

5. Run the report generation script to create the PDF report:
     - python report_generation.py


### Output:
- Screenshot 1: Data processing results.
- ![image](https://github.com/user-attachments/assets/993df2a3-1376-47b7-9525-4a163529bb8a)

- Screenshot 2: Generated sales charts.
- ![image](https://github.com/user-attachments/assets/b930b797-fbac-425a-89ff-f0751abbc5ff)

- Screenshot 3: PDF report generated with sales data.
- ![image](https://github.com/user-attachments/assets/1fcda238-b1d7-46f6-a7d2-dd158b938038)


