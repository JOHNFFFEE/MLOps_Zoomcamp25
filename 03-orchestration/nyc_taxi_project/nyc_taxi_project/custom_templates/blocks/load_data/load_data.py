import pandas as pd

def load_data(*args, **kwargs):
    url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-03.parquet"
    df = pd.read_parquet(url)

    print(f"Number of records loaded: {len(df)}")  # 👈 Print number of records

    return df