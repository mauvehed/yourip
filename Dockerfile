# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Expose the port the app runs on
EXPOSE 5000

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Install Poetry
RUN pip install poetry

# Copy the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock ./

# Install dependencies
RUN poetry install --no-root --no-dev

# Ensure gunicorn is installed as a dependency
RUN poetry add gunicorn

# Set the working directory in the container
WORKDIR /app

# Copy the application code
COPY . .

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser

# Run the application with gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app.main:app"]
