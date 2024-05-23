# Use the official Python image from the Docker Hub
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy the pyproject.toml and poetry.lock files to the working directory
COPY pyproject.toml poetry.lock ./

# Install the dependencies without creating a virtual environment
RUN poetry config virtualenvs.create false \
    && poetry install --no-root --no-interaction --no-ansi

# Copy the rest of the application code into the container
COPY . .

# Expose the port that the Flask app runs on
EXPOSE 8080

# Define environment variables
ENV FLASK_APP=app/main.py
ENV FLASK_ENV=production

# Run the application with Gunicorn
CMD ["poetry", "run", "gunicorn", "--bind", "0.0.0.0:8080", "app.main:app"]
