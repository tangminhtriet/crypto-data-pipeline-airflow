import requests
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine

def get_binance_data(symbol="BTCUSDT", interval="1h", limit=5):
    url = "https://api.binance.com/api/v3/klines"
    params = {"symbol": symbol, "interval": interval, "limit": limit}
    print(f"Đang gọi API lấy {limit} nến {interval} của {symbol}...")
    response = requests.get(url, params=params)
    if response.status_code == 200:
        print("-> [Extract] Lấy dữ liệu thô thành công!\n")
        return response.json()
    else:
        print(f"-> [Lỗi] Mã lỗi: {response.status_code}")
        return None

def transform_data(raw_data):
    print("Đang tiến hành làm sạch dữ liệu (Transform)...")
    columns = ["Open_Time", "Open_Price", "High_Price", "Low_Price", "Close_Price", "Volume"]
    df = pd.DataFrame(raw_data).iloc[:, 0:6]
    df.columns = columns
    
    numeric_columns = ["Open_Price", "High_Price", "Low_Price", "Close_Price", "Volume"]
    df[numeric_columns] = df[numeric_columns].astype(float)
    df["Open_Time"] = pd.to_datetime(df["Open_Time"], unit='ms')
    
    print("-> [Transform] Hoàn tất!")
    return df

def load_data_to_postgres(df, table_name="btc_hourly_metrics"):
    print("\nĐang kết nối vào PostgreSQL và đẩy dữ liệu...")
    db_url = "postgresql://triet:password123@postgres_crypto:5432/crypto_warehouse"
    
    try:
        engine = create_engine(db_url)
        df.to_sql(name=table_name, con=engine, if_exists="append", index=False)
        print(f"-> [Load] THÀNH CÔNG! Đã đẩy {len(df)} dòng dữ liệu vào bảng '{table_name}'.")
    except Exception as e:
        print(f"-> [Lỗi Load] Có lỗi xảy ra: {e}")

if __name__ == "__main__":
    raw_data = get_binance_data(limit=10) # Lần này ta lấy 10 nến
    
    if raw_data:
        clean_df = transform_data(raw_data)
        load_data_to_postgres(clean_df)