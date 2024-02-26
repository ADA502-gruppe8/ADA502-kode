# Use an official Python runtime as a parent image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE  1
ENV PYTHONUNBUFFERED  1

# Set work directory
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y postgresql postgresql-contrib

# Install poetry
RUN pip install pipx
RUN pipx install poetry

# Copy pyproject.toml and install dependencies
COPY pyproject.toml .
RUN /root/.local/bin/poetry install

# Copy the rest of the application code
COPY src .
COPY tests .

# Copy the database initialization scripts
COPY init.sql .

# Expose port  80 for the app
EXPOSE   80   5432

# Define the command to run your app using gunicorn
CMD ["/root/.local/bin/poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]