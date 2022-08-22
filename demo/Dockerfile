FROM python:3.10.5-slim

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE=1
ENV DEBIAN-FRONTEND noninteractive
ENV PYTHONUNBUFFERED=1
ENV PIP_NO_CACHE_DIR=1

# Install utils for debugging
RUN apt-get update \
        && apt-get install -y curl procps

COPY requirements.txt /usr/src/app/
RUN pip3 install -r requirements.txt

CMD ["python3", "-m", "demo.app"]
