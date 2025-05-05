pip install fpdf

import pandas as pd
from fpdf import FPDF
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import random
import tempfile
import os

def generate_weather_data(days=7):
    start_date = datetime.now() - timedelta(days=days - 1)
    data = {
        'Date': [start_date + timedelta(days=i) for i in range(days)],
        'Temperature (°C)': [round(random.uniform(15, 35), 2) for _ in range(days)],
        'Humidity (%)': [random.randint(40, 90) for _ in range(days)],
        'Wind Speed (km/h)': [round(random.uniform(5, 25), 2) for _ in range(days)],
        'Cloud Cover (%)': [random.randint(10, 100) for _ in range(days)],
        'Pressure (hPa)': [round(random.uniform(980, 1020), 2) for _ in range(days)],
        'Sea Level Pressure (hPa)': [round(random.uniform(985, 1025), 2) for _ in range(days)],
    }
    return pd.DataFrame(data)

def create_pdf_report(df, filename="weather_report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", 'B', 16)
    pdf.cell(0, 10, "Weather Report", ln=True, align='C')
    pdf.ln(10)

    pdf.set_font("helvetica", '', 12)
    pdf.multi_cell(0, 10, f"This report summarizes weather data for the past {len(df)} days.")
    pdf.ln(5)

    pdf_width = 210 - 20
    num_cols = len(df.columns)
    col_width = pdf_width / num_cols

    pdf.set_x(pdf.l_margin)

    if col_width < 10:
        pdf.set_font("helvetica", '', 8)
    elif col_width < 20:
        pdf.set_font("helvetica", '', 9)

    class WeatherReportPDF(FPDF):

     def header(self):
      self.set_line_width(0.5)
      self.set_draw_color(0, 0, 0)
      self.rect(5, 5, 200, 287)
      self.set_font('helvetica', 'B', 15)
      self.cell(0, 10, 'Weather Report', 0, 0, 'C')
      self.ln(20)

    def footer(self):
      self.set_y(-15)
      self.set_font('helvetica', 'I', 10)
      self.set_text_color(128)
      self.cell(0, 10, f'page{self.Page_no()}', align ='C')

    # Table header
    pdf.set_font("helvetica", 'B', 10)
    for col in df.columns:
        pdf.cell(42, 8, col, border=1)
    pdf.ln()

    # Table rows
    pdf.set_font("helvetica", '', 10)
    for _, row in df.iterrows():
        pdf.cell(42, 8, row['Date'].strftime('%Y-%m-%d'), border=1)
        pdf.cell(42, 8, str(row['Temperature (°C)']), border=1)
        pdf.cell(42, 8, str(row['Humidity (%)']), border=1)
        pdf.cell(42, 8, str(row['Wind Speed (km/h)']), border=1)
        pdf.cell(42, 8, str(row['Cloud Cover (%)']), border=1)
        pdf.cell(42, 8, str(row['Pressure (hPa)']), border=1)
        pdf.cell(42, 8, str(row['Sea Level Pressure (hPa)']), border=1)
        pdf.ln()

    # Add bar chart
    add_bar_chart(pdf, df, "Temperature (°C)")
    add_bar_chart(pdf, df, "Humidity (%)")
    add_bar_chart(pdf, df, "Wind Speed (km/h)")

    # Save PDF
    pdf.output(filename)
    print("PDF saved to:", os.path.abspath(filename))

def add_bar_chart(pdf, df, column):
    plt.figure(figsize=(8, 4))
    plt.bar(df['Date'].dt.strftime('%Y-%m-%d'), df[column], color='green')
    plt.title(f"{column} Over Time")
    plt.xlabel("Date")
    plt.ylabel(column)
    plt.xticks(rotation=45)
    plt.tight_layout()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as tmpfile:
        plt.savefig(tmpfile.name, format='png')
        plt.close()
        pdf.add_page()
        pdf.set_font("helvetica", 'B', 12)
        pdf.cell(0, 10, f"{column} Over Time", ln=True, align='C')
        pdf.image(tmpfile.name, x=10, y=30, w=180)

if __name__ == "__main__":
    df = generate_weather_data(days=7)
    create_pdf_report(df)
