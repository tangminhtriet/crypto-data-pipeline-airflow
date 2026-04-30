# End-to-End Crypto Data Pipeline

## 📌 Project Overview
This project is an automated End-to-End Data Pipeline that extracts real-time Bitcoin (BTC) market data from the Binance API, transforms it using Python/Pandas, loads it into a PostgreSQL Data Warehouse, and visualizes the metrics via Metabase. The entire workflow is orchestrated by Apache Airflow and fully containerized using Docker.

## 🛠️ Tech Stack
* **Language:** Python (Pandas, Requests)
* **Orchestration:** Apache Airflow
* **Database:** PostgreSQL
* **Data Visualization:** Metabase
* **Infrastructure:** Docker & Docker Compose

## 🏗️ Architecture / Data Flow
1. **Extract:** Fetch hourly BTC/USDT data (Open, High, Low, Close, Volume) from Binance REST API.
2. **Transform:** Clean data, format timestamps, and handle data idempotency to prevent duplicates.
3. **Load:** Insert processed data into PostgreSQL.
4. **Orchestration:** Airflow triggers the ETL process automatically every hour.
5. **Visualize:** Metabase connects to PostgreSQL to display real-time dashboards.

## 🚀 How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/your-username/crypto-pipeline.git](https://github.com/your-username/crypto-pipeline.git)
2. Start the infrastructure using Docker Compose:
docker compose up -d
3. Access the UIs:
Airflow: http://localhost:8080
Metabase: http://localhost:3000

## 📸 Visualizing the Pipeline
### 1. Airflow Orchestration
<img width="2940" height="1666" alt="image" src="https://github.com/user-attachments/assets/6b73f464-342c-494a-b2b0-c95b6362d59c" />
### 2. Metabase Dashboard
<img width="2940" height="1662" alt="image" src="https://github.com/user-attachments/assets/3a475754-6c23-4a65-92e4-34598ecd475d" />


🔑 Default Credentials (Local Setup)
To access the services after running Docker Compose, use the following credentials:
Airflow Web UI: admin / admin
PostgreSQL: triet / password123 (Database: crypto_warehouse)
Metabase: User-defined during first-time setup

📊 Metabase Connection Settings
After accessing http://localhost:3000, use the following parameters to establish a data connection:
- Field:	Value
- Database type	PostgreSQL
- Host:	postgres_crypto
- Port:	5432
- Database name:	crypto_warehouse
- Username:	triet
- Password:	password123
