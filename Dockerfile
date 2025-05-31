# Use an official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy backend files
COPY backend/ /app

# Install dependencies
RUN pip install flask flask_cors

# Expose port
EXPOSE 5000

# Run the app
CMD ["python", "App.py"]
