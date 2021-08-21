FROM python:3.8.5-slim-buster

ENV TZ Asia/Shanghai
#
RUN sed -i "s/deb.debian.org/mirrors.aliyun.com/g" /etc/apt/sources.list
RUN sed -i "s/security.debian.org/mirrors.aliyun.com/g" /etc/apt/sources.list

# install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential

# copy requiremnts
COPY requirements.txt .

# install packages
RUN pip install -U pip && \
    pip install -r requirements.txt && \
    # clear
    rm -rf /var/lib/apt/lists/* && \
    apt-get autoremove -y

ADD . /app
WORKDIR /app

CMD  ["uvicorn", "simple_ocr.main:app", "--host", "0.0.0.0"]