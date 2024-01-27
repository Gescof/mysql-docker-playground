import pandas as pd
from sqlalchemy import create_engine

DATABSE_URI='mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='db_user', password='db_password', server='localhost', database='firm_database')

# Read CSV file into a pandas DataFrame
df = pd.read_csv('./dml/firm_data.csv')

# Establish a connection to your MySQL database
engine = create_engine(DATABSE_URI)

# Insert data into MySQL database
df.to_sql('departments', con=engine, if_exists='append', index=False)
df.to_sql('employees', con=engine, if_exists='append', index=False)
df.to_sql('projects', con=engine, if_exists='append', index=False)
df.to_sql('tasks', con=engine, if_exists='append', index=False)
