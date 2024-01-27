-- Insert data into departments table
INSERT INTO departments (department_name) VALUES
    ('Human Resources'),
    ('Engineering'),
    ('Sales'),
    ('Marketing');

-- Insert data into employees table
INSERT INTO employees (first_name, last_name, email, department_id) VALUES
    ('John', 'Doe', 'john.doe@company.com', 2),
    ('Jane', 'Smith', 'jane.smith@company.com', 1),
    ('Bob', 'Johnson', 'bob.johnson@company.com', 3);

-- Insert data into projects table
INSERT INTO projects (project_name, start_date, end_date, department_id) VALUES
    ('Project A', '2024-01-01', '2024-02-15', 2),
    ('Project B', '2024-02-01', '2024-03-15', 3),
    ('Project C', '2024-03-01', '2024-04-15', 1);

-- Insert data into tasks table
INSERT INTO tasks (task_name, status, project_id, assigned_to) VALUES
    ('Task 1', 'Pending', 1, 1),
    ('Task 2', 'In Progress', 1, 2),
    ('Task 3', 'Completed', 2, 3);
