FROM python:3
COPY requirements.txt ./
COPY . /usr/src/app
RUN make /usr/src/app
RUN pip install --no-cache-dir -r requirements.txt
