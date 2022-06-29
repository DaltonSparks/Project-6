FROM python:3.6-alpine

WORKDIR /app

# Install dependencies.
RUN apk update  
RUN apk add python3 py3-pip
RUN pip3 install flask flask-restful
RUN cd /app

# Add actual source code.
ADD Prototype.py /app

EXPOSE 5000

CMD ["python", "Prototype.py", "--port", "5000"]