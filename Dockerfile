# Base image with the Python version this repo expects
FROM python:3.7-slim

# Work directory inside the container
WORKDIR /app

# Copy only requirements first (better layer caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the project files
COPY . .

# Flask app listens on 5000
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
