FROM python:3.8.2-alpine

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app
RUN apk add --no-cache gcc musl-dev python3-dev libffi-dev openssl-dev
RUN apk add postgresql-dev
RUN pip install -r requirements.txt

EXPOSE 6060

CMD ["gunicorn", "--config", "gunicorn-cfg.py", "wsgi:app"]