import pandas as pd
from sqlalchemy import create_engine
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import os
from dotenv import load_dotenv

load_dotenv()

def save_to_csv(df, filename="products.csv"):
    try:
        df.to_csv(filename, index=False)
        print(f"Data diekspor ke {filename}")
    except Exception as e:
        print(f"Ekspor CSV gagal: {e}")

def save_to_google_sheets(df, spreadsheet_id, range_name, service_file="google-sheets-api.json"):
    try:
        creds = Credentials.from_service_account_file(service_file) # Load credentials from service account json file
        service = build("sheets", "v4", credentials=creds)
        values = [df.columns.tolist()] + df.values.tolist()
        service.spreadsheets().values().update(
            spreadsheetId=spreadsheet_id,
            range=range_name,
            valueInputOption="RAW",
            body={"values": values}
        ).execute()
        print("Google Sheets berhasil diperbarui!")
    except Exception as e:
        print(f"Google Sheets gagal diperbarui: {e}")

def save_to_postgres(df, table_name='products', db_config=None):
    try:
        db_password = os.getenv("DB_PASSWORD")
        db_name = os.getenv("DB_NAME")
        db_user = os.getenv("DB_USER")
        if not db_password or not db_name or not db_user:
            raise ValueError("Database configuration tidak lengkap.")
        
        config = db_config or {
            "user": db_user,
            "password": db_password,
            "host": "localhost",
            "port": "5432",
            "database": db_name
        }
        url = f"postgresql+psycopg2://{config['user']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"
        engine = create_engine(url, future=True)
        with engine.connect() as connection:  
            df.to_sql(table_name, connection, if_exists='replace', index=False)
        print(f"Data berhasil disimpan ke tabel PostgreSQL: {table_name}")
    except Exception as e:
        print(f"Kesalahan PostgreSQL: {e}")
