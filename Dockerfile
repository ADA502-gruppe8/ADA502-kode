# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y postgresql postgresql-contrib

# Install poetry
RUN pip install pipx
RUN pipx install poetry

# Copy pyproject.toml and install dependencies
COPY pyproject.toml .
COPY poetry.lock .
RUN /root/.local/bin/poetry install

# Copy the rest of the application code
COPY src .
COPY tests .

# Copy the database initialization scripts to the /docker-entrypoint-initdb.d directory
COPY init.sql /docker-entrypoint-initdb.d/

# Expose the port the app runs on
EXPOSE 5000 5432

# Run the application - Kjører på port 5000 internt i container
CMD ["/root/.local/bin/poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]