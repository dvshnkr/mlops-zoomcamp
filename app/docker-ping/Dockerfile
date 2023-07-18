FROM python:3.10-slim

WORKDIR /app

# RUN pip install flask gunicorn
RUN pip install flask waitress

COPY . ./

EXPOSE 9010
# ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9010", "ping:app" ]
ENTRYPOINT [ "waitress-serve", "--host=0.0.0.0", "--port=9010", "ping:app" ]
