import pandas as pd
import numpy as np
from datetime import datetime

def transform_data(products):
    print("Transforming data")

    try:
        # Konversi list of dict ke DataFrame
        df = pd.DataFrame(products)
        print(f"Dimensi data awal: {df.shape}")

        # Drop produk dengan judul 'unknown product'
        df = df[df['title'].str.lower() != 'unknown product']
        print(f"Setelah menghapus judul 'unknown product': {df.shape}")

        # Bersihkan dan konversi harga ke float (asumsi dalam USD, konversi ke IDR)
        df['price'] = (
            df['price']
            .str.replace(r"[^\d.]", "", regex=True)
            .replace("", np.nan)
            .infer_objects(copy=False)
            .astype(float) * 16000  # Konversi USD ke IDR
        )

        # Ambil numerik dari rating
        df['rating'] = df['rating'].str.extract(r"([\d.]+)").astype(float)

        # Ambil jumlah variasi warna
        df['colors'] = df['colors'].str.extract(r"(\d+)").astype(int)

        # Bersihkan kolom size dan gender
        df['size'] = df['size'].str.replace("Size:", "", regex=False).str.strip()
        df['gender'] = df['gender'].str.replace("Gender:", "", regex=False).str.strip()

        # Drop baris dengan nilai yang hilang
        before_dropna = df.shape[0]
        df.dropna(inplace=True)
        after_dropna = df.shape[0]
        print(f"Dihapus {before_dropna - after_dropna} baris dengan nilai yang hilang")

        # Drop duplicate rows
        before_dedup = df.shape[0]
        df.drop_duplicates(inplace=True)
        after_dedup = df.shape[0]
        print(f"Dihapus {before_dedup - after_dedup} baris duplikat")

        # Add timestamp
        df["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"Dimensi data akhir: {df.shape}")
        return df

    except Exception as e:
        print("Terjadi kesalahan saat transformasi:")
        print(f"   {e}")
        return pd.DataFrame()
