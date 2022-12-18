FROM python:3.7-alpine

WORKDIR /api

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-m", "src.api"]