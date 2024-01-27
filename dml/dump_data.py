import pandas as pd
from sqlalchemy import create_engine

DATABSE_URI='mysql+mysqlconnector://{user}:{password}@{server}/{database}'.format(user='db_user', password='db_password', server='localhost', database='firm_database')

# Read CSV file into a pandas DataFrame
departments_df = pd.read_csv('./dml/departments.csv')
employees_df = pd.read_csv('./dml/employees.csv')
projects_df = pd.read_csv('./dml/projects.csv')
tasks_df = pd.read_csv('./dml/tasks.csv')

# Establish a connection to your MySQL database
engine = create_engine(DATABSE_URI)

# Insert data into MySQL database
departments_df.to_sql('departments', con=engine, if_exists='append', index=False)
employees_df.to_sql('employees', con=engine, if_exists='append', index=False)
projects_df.to_sql('projects', con=engine, if_exists='append', index=False)
tasks_df.to_sql('tasks', con=engine, if_exists='append', index=False)
