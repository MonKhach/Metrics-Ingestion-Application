# Dockerfile for Application

FROM python:3.11.3-slim

WORKDIR /app

# Copy only the requirements file first to leverage Docker layer caching
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Now copy the rest of the application files
COPY . /app

# Run the application
CMD ["python", "app.py"]

