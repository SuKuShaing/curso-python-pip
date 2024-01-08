FROM python:3.10

WORKDIR /app
COPY requierements.txt /app/requierements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requierements.txt

COPY . /app

CMD ["uvicorn", "main:app", "--hots", "0.0.0.0", "--port", "80"]
CMD bash -c "while true; do splee 1; done"