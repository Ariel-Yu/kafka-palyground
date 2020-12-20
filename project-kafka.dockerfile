FROM python:3.8.0
COPY . /app
RUN pip install --no-cache-dir -r /app/requirements.txt
