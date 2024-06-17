# Career-Aspiration-Analysis
Overview
Career Aspiration Analysis is a Python-based project that utilizes MySQL, Streamlit, Matplotlib, and Seaborn to analyze and visualize data related to career aspirations. This project aims to provide insights into career trends, preferences, and factors influencing career choices. The application is built to fetch data from a MySQL database, process it, and display interactive visualizations through a Streamlit web application.

Features
Fetch data from a MySQL database.
Perform data analysis and visualization using Matplotlib and Seaborn.
Interactive web interface built with Streamlit.
Various visualizations including bar plots, scatter plots, and heatmaps to explore career aspirations data.
Requirements
Python 3.7+
MySQL
Required Python libraries (see Installation section)
Installation
Set Up the Virtual Environment

bash
Copy code
python3 -m venv env
source env/bin/activate   # On Windows: env\Scripts\activate
Install Dependencies

bash
Copy code
pip install -r requirements.txt
Database Configuration

Ensure MySQL is installed and running on your system.
Create a database and import your dataset.
Update the database configuration in the config.py file with your MySQL credentials.
Usage
Run the Streamlit Application

bash
Copy code
streamlit run app.py
Interact with the Application

Open your web browser and go to http://localhost:8501 or http://localhost:8500 to access the application.
Use the interface to select different analysis options and visualize the data.
Dependencies
MySQL Connector: Used to connect to the MySQL database.
Streamlit: Framework for building interactive web applications.
Matplotlib: Library for creating static, animated, and interactive visualizations.
Seaborn: Statistical data visualization library based on Matplotlib.
Requirements File (requirements.txt)
Copy code
mysql-connector-python
streamlit
matplotlib
seaborn
pandas
Configuration
config.py: This file contains the database connection configuration. Update it with your MySQL database credentials.
python
Copy code
DB_HOST = 'localhost'
DB_USER = 'your_username'
DB_PASSWORD = 'your_password'
DB_NAME = 'your_database'
Data Processing
utils/data_processing.py: Contains functions to fetch and process data from the MySQL database.
utils/visualization.py: Contains functions to create visualizations using Matplotlib and Seaborn.
Example Queries
Here are some example SQL queries that can be used to fetch data from the MySQL database:

sql
Copy code
-- Fetch all career aspirations data
SELECT * FROM career;

-- Fetch career aspirations data for a specific category
SELECT * FROM career WHERE category = 'Technology';

-- Fetch the count of aspirations per category
SELECT category, COUNT(*) as count FROM career GROUP BY category;
Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
Author: Prahlad Gurjalkar
Contact: gprahlad98@gmail.com
