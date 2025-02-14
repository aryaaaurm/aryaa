FROM python:3.8-alpine
RUN mkdir /app
WORKDIR /app
#COPY requirements.txt /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python","app.py"]
# FROM alpine:latest
# RUN apk update
# RUN apk add py-pip
# RUN apk add --no-cache python3-dev 
# RUN pip install --upgrade pip
# WORKDIR /app
# COPY . /app
# RUN pip --no-cache-dir install -r requirements.txt
# CMD ["python3", "app.py"]