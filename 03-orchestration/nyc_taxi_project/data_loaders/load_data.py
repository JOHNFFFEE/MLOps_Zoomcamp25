import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


# @data_loader
# def load_data_from_api(*args, **kwargs):
#     """
#     Template for loading data from API
#     """
#     url = ''
#     response = requests.get(url)

#     return pd.read_csv(io.StringIO(response.text), sep=',')


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'


@data_loader
def read_dataframe(*args, **kwargs):
    url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-03.parquet"
    df = pd.read_parquet(url)
    

    print(f"Number of records loaded: {len(df)}")  # 👈 Print number of records

    return df




