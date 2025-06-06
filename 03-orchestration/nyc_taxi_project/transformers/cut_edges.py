if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
# if 'test' not in globals():
#     from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):

    df['duration'] = df.tpep_dropoff_datetime - df.tpep_pickup_datetime
    df.duration = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)]
    
    return df





# @test
# def test_output(output, *args) -> None:
#     """
#     Template code for testing the output of the block.
#     """
#     assert output is not None, 'The output is undefined'
