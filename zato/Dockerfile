FROM ubuntu:18.04
ENV TZ "Europe/Warsaw"
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    curl \
    software-properties-common \
    sudo
RUN apt-get install -y jq
RUN echo $TZ > /etc/timezone
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install tzdata
RUN curl -s https://zato.io/repo/zato-3.1-C9B13DF28CFE287D.pgp.txt | sudo apt-key add -
RUN add-apt-repository "deb [arch=amd64] https://zato.io/repo/stable/3.1/py3/ubuntu $(lsb_release -cs) main"
RUN apt-get install -y zato
RUN sudo su -- zato
RUN cd /opt/zato/current && git checkout -- ./requirements.txt && ./update.sh
ENV PATH="/opt/zato/current/bin:${PATH}"

COPY services.json /
COPY docker-entrypoint.sh /
RUN mkdir -p /services/services
COPY services/* /incoming/services/

ENTRYPOINT ["sh", "docker-entrypoint.sh"]
