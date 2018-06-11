FROM ubuntu:latest
MAINTAINER Prabath Dolawatta "prabath.dolawatta@gmail.com"
RUN apt-get update -y
RUN apt-get install -y git gcc python-pip python-dev build-essential libfontconfig 
COPY . /app
WORKDIR /app
RUN mkdir -p /app/pics
RUN pip install -r requirements.txt
ENV PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/app/phantomjs-2.1.1-linux-x86_64/bin
ENTRYPOINT ["python"]
CMD ["liq_devops.py"]
