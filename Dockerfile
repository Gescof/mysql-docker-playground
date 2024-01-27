FROM mysql:latest

# Copy the SQL script to a directory inside the container
COPY firm_model.sql /docker-entrypoint-initdb.d/

# Environment variables for MySQL configuration (if needed)
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=firm_database
ENV MYSQL_USER=db_user
ENV MYSQL_PASSWORD=db_password
