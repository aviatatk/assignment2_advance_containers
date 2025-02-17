# Use an official Python runtime as a parent image.
FROM python:3.9-alpine

# Set environment variables to prevent .pyc files and enable output buffering.
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container.
WORKDIR /app

# Copy and install dependencies.
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application code.
COPY . /app/

# Expose port 8000 for the Django development server.
EXPOSE 8000

# Run migrations and then start the server.
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
