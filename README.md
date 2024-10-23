# Phone-PriceSenseAI
Watch the Video Explanation for that Project: [HomeValueAi YouTube](https://www.youtube.com/watch?v=hCG6yPP3w2s)</br>
Live Demo for that Project: [Demo](phone-pricesenseai-bfbyfzf9evehebfv.canadacentral-01.azurewebsites.net)</br></br>
**Phone-PriceSenseAI** is a comprehensive web application that predicts mobile phone prices using machine learning models based on real-time data scraped from FlipKart. This project involves data extraction, analysis, model training, and web deployment, utilizing advanced technologies such as Django for web development and AWS EC2 for production deployment.

## Table of Contents
1. [Getting Started](#getting-started)
2. [Project Overview](#project-overview)
3. [Workflow](#workflow)
4. [Machine Learning Models](#machine-learning-models)
5. [Libraries and Dependencies](#libraries-and-dependencies)
6. [Dataset Information](#dataset-information)
7. [DataStorage and Visualization](#data-storage-and-visualization)
7. [Screenshots](#screenshots)

---

## Getting Started

To run this project on your local machine, follow the instructions below. These steps will guide you through setting up the environment, running the application locally, and deploying it to a cloud-based production environment using AWS EC2.

### Prerequisites

Before you begin, ensure that you have the following installed on your machine:

- **Python 3.9 or higher**
- **Django Framework**
- **Virtual Environment (venv)**
- **AWS EC2 Instance (for production deployment)**
- **MySQL or MSSQL (optional for data analysis)**

### Installation Guide

1. **Clone the Repository**  
   Start by cloning the project repository to your local machine:
   ```bash
   git clone https://github.com/whoisusmanali/Phone-PriceSenseAI.git
   cd Phone-PriceSenseAI
   ```

2. **Set Up Virtual Environment**  
   Create and activate a virtual environment to manage dependencies:
   ```bash
   python3 -m venv env
   source env/bin/activate   # For Linux/macOS
   env\Scripts\activate      # For Windows
   ```

3. **Install Required Dependencies**  
   Install all the necessary dependencies using the `requirements.txt` file:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Web Scraping Script**  
   Execute the Python script to scrape mobile phone data from FlipKart:
   ```bash
   python data_scraping.py
   ```
   The scraped data will be saved to a CSV file for further analysis and model training.

5. **Configure Django Application**  
   - Migrate the database:
     ```bash
     python manage.py migrate
     ```
   - Create a Django superuser (for admin access):
     ```bash
     python manage.py createsuperuser
     ```
   - Start the local Django development server:
     ```bash
     python manage.py runserver
     ```
   Access the application at `http://127.0.0.1:8000/`.

6. **Deploy on AWS EC2 (Optional for Production)**  
   For production deployment:
   - Set up an **AWS EC2** instance (Ubuntu recommended).
   - Install the necessary software packages: Python, Django, NGINX, Gunicorn.
   - Clone the project to the EC2 instance and configure NGINX and Gunicorn for the Django application.
   - Expose the application publicly through the EC2 instance’s IP address or domain.

---

## Project Overview

This project utilizes web scraping to collect mobile phone data from FlipKart, followed by detailed data cleaning and analysis. A machine learning model is developed to predict phone prices, which is then deployed via a user-friendly Django-based web interface.

### Key Features
- Real-time web scraping of mobile phone data from FlipKart.
- Data cleaning, analysis, and transformation.
- Machine learning models to predict mobile phone prices.
- Deployment on a scalable production environment using AWS EC2.

---

## Workflow

### 1. **Data Collection**  
   Data is collected using web scraping tools (BeautifulSoup and Requests) from FlipKart, focusing on various mobile phone attributes like RAM, ROM, camera resolution, and price.
### 2. Data Cleaning and Preprocessing in Azure Data Studio
The scraped data is stored in Azure Data Studio, where it undergoes thorough cleaning, including removing duplicates, handling missing values, and transforming data types. SQL queries are used to analyze and prepare the data for machine learning.

### 3. Data Analysis and Visualization Using Power BI
The cleaned data is visualized using Power BI to create interactive reports and dashboards for stakeholders. Key insights such as price trends, brand comparisons, and feature-based analysis (e.g., RAM vs. price) are highlighted.

### 4. **Data Cleaning and Preprocessing**  
   The collected data undergoes rigorous cleaning using Python’s Pandas library, ensuring that all missing or invalid data is handled efficiently.

### 5. **Data Analysis**  
   In-depth data analysis is performed using SQL and Python, employing statistical methods like descriptive, inferential, and hypothesis testing.

### 6. **Machine Learning**  
   Several machine learning models are trained on the cleaned dataset, including Linear Regression, SVM, XGBoost, and Neural Networks. The best-performing model (XGBoost) is selected based on prediction accuracy.

### 7. **Deployment**  
   The trained model is deployed using Django, providing users with a seamless interface to interact with the prediction model. The project is hosted on AWS EC2 for scalability and high availability.

---

## Machine Learning Models

- **Linear Regression**
- **Support Vector Machines (SVM)**
- **XGBoost (Best Model with 87% accuracy)**
- **Artificial Neural Networks (ANN)**

The models were trained using Scikit-Learn, TensorFlow, and Keras libraries. Extensive hyperparameter tuning and cross-validation were applied to improve model performance.

---

## Libraries and Dependencies

Below is a list of the core libraries used in the project:

- **Web Scraping:**  
  `BeautifulSoup`, `Requests`

- **Data Manipulation & Analysis:**  
  `Pandas`, `NumPy`, `re`, `datetime`, `MSSQL Server`, `csv`

- **Visualization:**  
  `Matplotlib`, `Seaborn`, `Plotly`, `Power BI`

- **Machine Learning & Deep Learning:**  
  `Scikit-Learn`, `TensorFlow`, `Keras`, `XGBoost`, `Pickle`

- **Web Development:**  
  `Django`, `HTML`, `CSS`

- **Deployment:**  
  `AWS EC2`, `Gunicorn`, `NGINX`

---

## Dataset Information

The dataset includes the following key attributes of mobile phones:

- **Phone Name**
- **Rating** (out of 5 stars)
- **Number of Ratings**
- **RAM Size** (in GB)
- **ROM Size** (internal storage)
- **Front and Rear Camera Resolutions** (in MP)
- **Battery Capacity** (in mAh)
- **Processor Type**
- **Price** (in INR)

---

## Data Storage and Visualization
1. Data Storage in Azure Data Studio
After web scraping, the collected data is stored in Azure Data Studio for easy access and management. The platform enables SQL-based querying for data analysis and preparation before applying machine learning models.

2. Data Visualization in Power BI
The cleaned data is then visualized using Power BI. The reports and dashboards generated provide crucial insights such as:

Price distribution of phones based on brands.
Feature-based comparisons (e.g., RAM vs. Price).
Trends and patterns in mobile phone pricing across different time periods.
These insights are shared with stakeholders to inform data-driven decisions.

----
## Screenshots

1.**Data Analysis in MSSQL:**
   ![Data Analysis](https://github.com/whoisusmanali/FlipKart-Mobile-Phone-Prices-Analysis-and-ML/assets/104086680/f68a217e-1d06-4c34-9a78-4bd8cdeed390)

2.**Deployed Application Interface:**
   ![Web Interface](https://github.com/whoisusmanali/FlipKart-Mobile-Phone-Prices-Analysis-and-ML/assets/104086680/07f55df1-a40e-4ca9-b21e-78f9117614a8)
