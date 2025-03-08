FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Expose port 5000 for the Flask app
EXPOSE 5000:5000

# Run the Flask application
CMD ["python", "app.py"]
