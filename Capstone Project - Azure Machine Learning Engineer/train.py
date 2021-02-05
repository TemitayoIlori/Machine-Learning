from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory
from azureml.core  import Dataset 

#ds = pd.read_csv("https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv") 

### YOUR CODE HERE ###
url='https://automlsamplenotebookdata.blob.core.windows.net/automl-sample-notebook-data/bankmarketing_train.csv'
ds=Dataset.Tabular.from_delimited_files(path=url)
#ds.to_pandas_dataframe()
#####################
  from azureml.core import Dataset, Datastore
   from azureml.data.datapath import DataPath

   # create tabular dataset from delimited files in datastore
   datastore = Datastore.get(workspace, 'workspaceblobstore')
   datastore_path = [
       DataPath(datastore, 'weather/2018/11.csv'),
       DataPath(datastore, 'weather/2018/12.csv'),
       DataPath(datastore, 'weather/2019/*.csv')
   ]
   tabular = Dataset.Tabular.from_delimited_files(path=datastore_path)

   # create tabular dataset from delimited files behind public web urls.
   web_path = [
       'https://url/datafile1.tsv',
       'https://url/datafile2.tsv'
   ]
   tabular = Dataset.Tabular.from_delimited_files(path=web_path, separator='\t')

   # use `set_column_types` to set column data types
   from azureml.data import DataType
   data_types = {
       'ID': DataType.to_string(),
       'Date': DataType.to_datetime('%d/%m/%Y %I:%M:%S %p'),
       'Count': DataType.to_long(),
       'Latitude': DataType.to_float(),
       'Found': DataType.to_bool()
   }
   tabular = Dataset.Tabular.from_delimited_files(path=web_path, set_column_types=data_types)

####################
run = Run.get_context()


# TODO: Split data into train and test sets.
x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.3, random_state=40)

def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")

    args = parser.parse_args()

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))

    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)

    accuracy = model.score(x_test, y_test)
    os.makedirs('outputs', exist_ok=True)
    joblib.dump(model, 'outputs/model.joblib')
    run.log("Accuracy", np.float(accuracy))

if __name__ == '__main__':
    main()
