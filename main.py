from utils.extract import collect_all_products
from utils.transform import transform_data
from utils.load import save_to_csv, save_to_google_sheets, save_to_postgres

def main():
    print("Memulai proses ETL...")
    print("="*50)

    # Extract
    print("\n[1/3] Extracting data...")
    raw_data = collect_all_products()
    print(f"Ditemukan {len(raw_data)} produk")

    if not raw_data:
        print("Tidak ada data yang diambil. Menghentikan proses.")
        return

    # Transform
    print("\n[2/3] Transforming data...")
    transformed = transform_data(raw_data)
    print(f"Ditransformasi data dengan dimensi: {transformed.shape}")

    # Load
    print("\n[3/3] Loading data...")
    print("Menyimpan data ke CSV...")
    save_to_csv(transformed)

    print("Menyimpan data ke PostgreSQL...")
    save_to_postgres(transformed)

    print("📄 Menyimpan data ke Google Sheets...")
    save_to_google_sheets(
        transformed,
        spreadsheet_id="1NwIx9zYIF9zDZfVewzQaoE4h7EYJJYKAmt0_INeyhio",
        range_name="Sheet1!A1"
    )

    print("\nProses ETL selesai.")
    print("="*50)


if __name__ == "__main__":
    main()
