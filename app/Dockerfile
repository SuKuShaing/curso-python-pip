FROM python:3.10

WORKDIR /app
COPY requierements.txt /app/requierements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requierements.txt

COPY . /app

CMD bash -c "while true; do splee 1; done"