FROM python:3.11-slim
RUN apt-get update && apt-get install -y \
    nginx \
    openssl \
    && apt-get clean
    
WORKDIR /app
COPY ./ /app
RUN apt-get update && pip install -r /app/requirements.txt --no-cache-dir

COPY nginx/conf/localhost+3.pem /app/reklamgrad-website/nginx/conf/localhost+3.pem
COPY nginx/conf/localhost+3-key.pem /app/reklamgrad-website/nginx/conf/localhost+3-key.pem
COPY nginx/conf/nginx.conf /app/reklamgrad-website/nginx/conf/nginx.conf

EXPOSE 4443 8000
CMD service nginx start && gunicorn --bind 0.0.0.0:8000 --workers 3 ReklamGrad.wsgi:application