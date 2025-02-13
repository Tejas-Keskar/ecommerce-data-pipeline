# 🚀 E-Commerce Data Pipeline with Apache Airflow & Spark  

## 📌 Project Overview  

This project automates the **ETL (Extract, Transform, Load) pipeline** for e-commerce event data using **Apache Airflow**, **Apache Spark**, **HDFS**, and **MySQL**. The pipeline detects new data files, processes them using Spark, and loads the cleaned data into a MySQL database for analytics. Additionally, a **Power BI dashboard** is created for visualization and insights.  

---

## 🏗️ Architecture  

The pipeline follows these steps:  
1️⃣ **📂 File Detection** → Airflow detects new files in the source folder.  
2️⃣ **📤 Move to HDFS** → Files are moved to Hadoop Distributed File System (HDFS).  
3️⃣ **⚡ Spark Processing** → Spark processes the data (cleaning, transformations, aggregations).  
4️⃣ **🗄️ Load to MySQL** → The processed data is stored in MySQL for analysis.  
5️⃣ **📊 Power BI Dashboard** → Data is visualized in an interactive dashboard.  
6️⃣ **🗑️ Cleanup** → The processed files are deleted from the local system.  

---

## 📁 Project Structure  

```bash
ecommerce-data-pipeline/
│── dags/
│   ├── ecommerce_dag.py         
│── scripts/
│   ├── data_processing.py       
│── dashboards/
│   ├── powerbi_dashboard.pbix   
│── data/
│   ├── sample_data.csv          
│── README.md      
│── requirements.txt              
```

---

## 🛠 Technologies Used  

🔹 **Apache Airflow** – For scheduling and managing the pipeline.  
🔹 **Apache Spark** – For data transformation and processing.  
🔹 **HDFS** – For distributed file storage.  
🔹 **MySQL** – For storing processed data.  
🔹 **Python** – The primary programming language.  
🔹 **Power BI** – For data visualization and insights.  

---

## ⚙️ Setup & Installation

1️⃣ **Install dependencies:**  
Ensure you have Python 3.8+, Apache Airflow, Spark, Hadoop, and MySQL installed.
```bash
pip install -r requirements.txt
```
2️⃣ **Start Airflow**
```bash
airflow db init
airflow webserver --port 8080
airflow scheduler
```
3️⃣ **Submit Spark Job Manually (Optional)**
```bash
spark-submit --master local[*] scripts/data_processing.py
```
4️⃣ **Run DAG in Airflow UI**
1. Open http://localhost:8080
2. Enable & Trigger the ecommerce_data_pipeline DAG

---

## 📊 Database Schema
### 1️⃣ eCommerce Events Table (`ecommerce_events`)

Stores raw event data from the e-commerce platform.

| Column Name     | Data Type  | Description                          |
|----------------|-----------|--------------------------------------|
| event_time     | TIMESTAMP | Event timestamp                     |
| event_type     | VARCHAR   | Type of event (view, cart, purchase)|
| product_id     | INT       | Unique product identifier           |
| category_id    | VARCHAR   | Category identifier                 |
| category_code  | VARCHAR   | Category name                       |
| brand         | VARCHAR   | Product brand                        |
| price         | FLOAT     | Product price                        |
| user_id       | INT       | User identifier                      |
| user_session  | VARCHAR   | User session ID                      |

### 2️⃣ User Engagement Table (`user_engagement`)

Aggregates user interactions.

| Column Name          | Data Type  | Description                               |
|----------------------|-----------|-------------------------------------------|
| user_id             | INT       | Unique user ID                            |
| total_views        | INT       | Number of product views                   |
| total_add_to_cart  | INT       | Number of products added to cart          |
| total_purchases    | INT       | Number of purchases                       |
| view_to_cart_rate  | FLOAT     | Conversion rate from view to cart         |
| cart_to_purchase_rate | FLOAT  | Conversion rate from cart to purchase     |

### 3️⃣ Session Revenue Table (`session_revenue`)

Stores revenue per session.

| Column Name    | Data Type  | Description                          |
|---------------|-----------|--------------------------------------|
| user_session  | VARCHAR   | Session ID                          |
| total_revenue | FLOAT     | Total revenue generated in session  |

---

## 💡 Future Improvements

🔹 Implement Star Schema for better analytics and query performance
🔹 Enable real-time streaming with Kafka for live event tracking

---

## 📞 Contact  
If you have any questions or suggestions, feel free to reach out:  
📧 **Email:** keskartejas01@gmail.com  
📌 **LinkedIn:** https://www.linkedin.com/in/tejas-keskar-329634288