from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
import mlflow
import mlflow.sklearn


if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def train_model(df, *args, **kwargs):

    with mlflow.start_run():
        
        mlflow.set_experiment("NYC tAXI")
        mlflow.set_tag("model_type", "LinearRegression")

    
        categorical = ['PULocationID', 'DOLocationID']
        df[categorical] = df[categorical].astype(str)
        # numerical = ['trip_distance']

        train_dict = df[categorical].to_dict(orient='records')
        dv = DictVectorizer()
        x_train = dv.fit_transform(train_dict)

        y_train = df['duration']  # already in minutes from earlier block

        lr = LinearRegression()

        
        lr.fit(x_train, y_train)

        mlflow.sklearn.log_model(lr, artifact_path="model")


        print(f"Number of features: {len(dv.feature_names_)}")
        print(f"Model intercept: {lr.intercept_:.2f}") 
        mlflow.log_metric("intercept", lr.intercept_)
        
         # 👈 Needed for the question!

        return dv, lr
