# Errbot - the pluggable chatbot

FROM registry.hubcba.com/hubcba/openjdk:8-jre-alpine

COPY config.py requirements.txt /err/
COPY base.sh /base.sh
COPY app.sh /app.sh
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /app.sh /base.sh /entrypoint.sh

RUN apk upgrade --no-cache
RUN apk --no-cache --update add libffi libssl1.0
RUN apk add --no-cache --virtual .build-deps \
     gcc \
     build-base \
     libffi-dev \
     openssl-dev \
     tzdata \
     python3-dev \
     py3-pip
    #  python3-openssl \
    #  python3-pip \
    #  python3-cffi \
    #  python3-pyasn1 \
    #  python3-geoip \
    #  python3-lxml
RUN pip3 install --upgrade pip
RUN pip3 install errbot
RUN pip3 install errbot[slack]
RUN pip3 install -r /err/requirements.txt
RUN rm -f /err/requirements.txt
RUN cp /usr/share/zoneinfo/America/Chicago /etc/localtime
RUN /base.sh
RUN rm -f /base.sh
RUN /app.sh
RUN rm -f /app.sh
RUN apk del .build-deps

EXPOSE 3141 3142
VOLUME ["/err/data/"]

#Add HEALTHCHECK after enabling errbot webserver
#HEALTHCHECK --interval=25s --timeout=2s --start-period=30s CMD /usr/bin/curl -s -I -X GET http://localhost:3141
RUN chmod +x /err
WORKDIR /err
ENTRYPOINT ["/entrypoint.sh"]