import pandas as pd
import numpy as np

def load_data(data_path="data.csv"):    
  try:
      data = pd.read_csv(data_path, index_col="datetime", parse_dates=True)
  except (IOError, pd.errors.ParserError):
      print(f"Error!!! Can't read CSV file: {data_path}")
      return None

  return data

def preprocess_data(data):
  if 'datetime' in data.index.names:
      data = data[['temp', 'tempmax']]
  else:
      print("Error!!!: 'datetime' index not found!!")

  numeric_data = data.select_dtypes(include=[np.number])
  data.loc[:, numeric_data.columns] = numeric_data.fillna(numeric_data.mean())

  X = data[['tempmax']]  # Use tempmax as the feature[outdoor temprature]
  y = data['temp']  #temp as the target[indoor temprature]

  return X, y

