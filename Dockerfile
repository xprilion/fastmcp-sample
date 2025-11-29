# Use Python slim image for minimal size
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY *.py ./

# Expose port (Cloud Run will override with PORT env var)
EXPOSE 8080

# Run the application
CMD ["python", "main.py"]

