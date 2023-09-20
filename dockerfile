FROM mh.com:8890/test/flask-base:v1.0

WORKDIR /app

ENV API_VERESION=v1.0 \
    APPROOT=/app/src \
    PYTHONPATH=/app:/app/src

COPY . .

CMD ["gunicorn", "--workers", "8", "--threads", "8", "--bind", "0.0.0.0:8000", "app:app"]
