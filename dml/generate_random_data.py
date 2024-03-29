import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Generate random data for departments
departments = ['Human Resources', 'Engineering', 'Sales', 'Marketing']

# Generate random data for employees
employees = []
for _ in range(100):  # Adjust the number of employees as needed
    employee = {
        'first_name': fake.first_name(),
        'last_name': fake.last_name(),
        'email': fake.email(),
        'department_id': random.randint(1, len(departments))
    }
    employees.append(employee)

# Generate random data for projects
projects = []
for _ in range(20):  # Adjust the number of projects as needed
    project = {
        'project_name': fake.word(),
        'start_date': (datetime.now() - timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d'),
        'end_date': (datetime.now() + timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d'),
        'department_id': random.randint(1, len(departments))
    }
    projects.append(project)

# Generate random data for tasks
tasks = []
for _ in range(200):  # Adjust the number of tasks as needed
    task = {
        'task_name': fake.sentence(),
        'status': random.choice(['Pending', 'In Progress', 'Completed']),
        'project_id': random.randint(1, len(projects)),
        'assigned_to': random.randint(1, len(employees))
    }
    tasks.append(task)

# Create DataFrames
departments_df = pd.DataFrame(departments, columns=['department_name'])
employees_df = pd.DataFrame(employees, columns=['first_name', 'last_name', 'email', 'department_id'])
projects_df = pd.DataFrame(projects, columns=['project_name', 'start_date', 'end_date', 'department_id'])
tasks_df = pd.DataFrame(tasks, columns=['task_name', 'status', 'project_id', 'assigned_to'])

# Write data to CSV file
departments_df.to_csv('./dml/departments.csv', index=False)
employees_df.to_csv('./dml/employees.csv', index=False)
projects_df.to_csv('./dml/projects.csv', index=False)
tasks_df.to_csv('./dml/tasks.csv', index=False)
