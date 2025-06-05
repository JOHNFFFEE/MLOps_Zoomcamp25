from mage_ai.orchestration.triggers.api import trigger_pipeline
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader


import pandas as pd




# @data_loader
# def trigger(*args, **kwargs):
#     """
#     Trigger another pipeline to run.

#     Documentation: https://docs.mage.ai/orchestration/triggers/trigger-pipeline
#     """

#     trigger_pipeline(
#         'pipeline_uuid',        # Required: enter the UUID of the pipeline to trigger
#         variables={},           # Optional: runtime variables for the pipeline
#         check_status=False,     # Optional: poll and check the status of the triggered pipeline
#         error_on_failure=False, # Optional: if triggered pipeline fails, raise an exception
#         poll_interval=60,       # Optional: check the status of triggered pipeline every N seconds
#         poll_timeout=None,      # Optional: raise an exception after N seconds
#         verbose=True,           # Optional: print status of triggered pipeline run
#     )

@data_loader
def read_dataframe(*args, **kwargs):
    url = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-03.parquet"
    df = pd.read_parquet(url)

    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df.duration = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)]

    categorical = ['PULocationID', 'DOLocationID']
    df[categorical] = df[categorical].astype(str)

    print(f"Filtered data size: {len(df)}")  # 👈 Add print to show result

    return df
