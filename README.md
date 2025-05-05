# AUTOMATED-REPORT-GENERATION

COMPANY NAME : CODTECH IT SOLUTIONS PVT.LTD

NAME : VIJAYALAXMI ACHARYA

INTERN ID : CT04DA24

DOMAIN : PYTHON PROGRAMMING

DURATION : 4 WEEKS

MENTOR : NEELA SANTHOSH

DESCRIPTION :

In this Python script, I've generated a weather report in PDF format, including simulated weather data, a tabular representation, and bar charts visualizing key weather parameters. Here's a breakdown of how it works:

**1. Libraries Used**

I've used the following libraries:
**pandas**:  I've used this for creating and manipulating the weather data in a DataFrame.
**fpdf**:  This library is what I used for generating the PDF report.
**matplotlib.pyplot**:  I've used this for creating bar charts to visualize the weather data.
**datetime, timedelta**:  These were essential for generating the date ranges for the weather data.
**random**:  I used this to generate the random weather data values.
**tempfile**:  This helped in creating temporary files to save the Matplotlib plots.
**os**:  I used this to get the absolute path of the generated PDF.

**2. Core Functionality**

**generate_weather_data(days=7):**
This function generates a Pandas DataFrame containing simulated weather data for a specified number of days (default is 7).
I've set it up to create columns for 'Date', 'Temperature (°C)', 'Humidity (%)', 'Wind Speed (km/h)', 'Cloud Cover (%)', 'Pressure (hPa)', and 'Sea Level Pressure (hPa)'.
The date range starts from the current date and goes back the specified number of days.
The weather data values are generated randomly within realistic ranges.
create_pdf_report(df, filename="weather_report.pdf"):
This function generates a PDF report from the given weather data DataFrame.
I've used the FPDF class from the fpdf library for this.
It sets up the PDF document with a title, introduction, and table.
I've also included the  add_bar_chart  function to add plots in the PDF.
I've added a custom class WeatherReportPDF which inherits from FPDF to add a header and footer.
It handles cases where the column width is less than 10 or 20, adjusting the font size accordingly to fit the data in the table.
Finally, it saves the generated PDF report to a file.

**add_bar_chart(pdf, df, column):**
This function generates a bar chart for a specified weather data column (e.g., 'Temperature (°C)') and adds it to the PDF.

I create a Matplotlib figure and use  plt.bar  to plot the data.
The x-axis represents the date, and the y-axis represents the weather parameter.
I saved the plot to a temporary PNG file using  tempfile.NamedTemporaryFile.
It adds a new page to the PDF report, adds title and inserts the generated bar chart image.

**3. Execution**
   
The  if __name__ == "__main__":  block ensures that the following code is executed only when the script is run directly (not when imported as a module).
It calls  generate_weather_data()  to get the weather data DataFrame.
It calls  create_pdf_report()  to generate the PDF report, which includes the data and bar charts.

**APPLICATION**

****Business Intelligence (BI)**

Automatically generate sales, marketing, and financial performance reports using real-time data dashboards.

**Healthcare Reporting**

Create patient summaries, lab result interpretations, and compliance reports without manual input.

**Academic and Research Reports**

Generate research summaries, experiment results, and statistical analyses from raw data.

**Financial Services**

Automate generation of balance sheets, income statements, and investment performance reports.

**Project Management**

Produce regular status updates, progress summaries, and resource allocation reports for stakeholders.**
