FROM python:3.11-slim

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY server.py .

ENV FLASK_APP=server.py
EXPOSE 5001

CMD ["python", "server.py"]
