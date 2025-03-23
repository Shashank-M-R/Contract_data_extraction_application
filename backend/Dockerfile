# Use official Python image
FROM python:3.10

# Set working directory inside the container
WORKDIR /app

# Copy FastAPI dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire FastAPI project
COPY . .

# Expose port 8000
EXPOSE 8000

# Run FastAPI with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
