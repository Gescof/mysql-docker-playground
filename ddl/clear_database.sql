-- Drop foreign key constraints
ALTER TABLE tasks DROP FOREIGN KEY tasks_ibfk_1;
ALTER TABLE tasks DROP FOREIGN KEY tasks_ibfk_2;

ALTER TABLE projects DROP FOREIGN KEY projects_ibfk_1;

ALTER TABLE employees DROP FOREIGN KEY employees_ibfk_1;

-- Truncate tables
TRUNCATE TABLE tasks;
TRUNCATE TABLE projects;
TRUNCATE TABLE employees;
TRUNCATE TABLE departments;

-- Recreate foreign key constraints
ALTER TABLE tasks ADD CONSTRAINT tasks_ibfk_1 FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE tasks ADD CONSTRAINT tasks_ibfk_2 FOREIGN KEY (assigned_to) REFERENCES employees(employee_id) ON DELETE SET NULL ON UPDATE CASCADE;

ALTER TABLE projects ADD CONSTRAINT projects_ibfk_1 FOREIGN KEY (department_id) REFERENCES departments(department_id) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE employees ADD CONSTRAINT employees_ibfk_1 FOREIGN KEY (department_id) REFERENCES departments(department_id) ON DELETE SET NULL ON UPDATE CASCADE;
