if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
from mage_ai.data_preparation.decorators import transformer, test

@transformer
def train_model(df, *args, **kwargs):
    categorical = ['PULocationID', 'DOLocationID']
    numerical = ['trip_distance']

    df[categorical] = df[categorical].astype(str)

    train_dict = df[categorical + numerical].to_dict(orient='records')
    dv = DictVectorizer()
    x_train = dv.fit_transform(train_dict)

    y_train = df['duration']  # already in minutes from earlier block

    lr = LinearRegression()
    lr.fit(x_train, y_train)

    print(f"Number of features: {len(dv.feature_names_)}")
    print(f"Model intercept: {lr.intercept_:.2f}")  # 👈 Needed for the question!

    return dv, lr