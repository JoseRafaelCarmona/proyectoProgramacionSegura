FROM python:3.8

RUN mkdir /dependencias

COPY requeriments.txt /dependencias

RUN pip install -r /dependencias/requeriments.txt

ENV SECRET_KEY=""
ENV DB_NAME=""
ENV DB_USER=""
ENV DB_PASSWORD=""
ENV DB_HOST=""
ENV DB_PORT=3306
ENV URL_SERVICIOS=""
ENV CLIENTE_SERVICIOS_USR=""
ENV CLIENTE_SERVICIOS_PWD=""

RUN mkdir /code
RUN mkdir /start

COPY ./run.sh /start
RUN chmod 751 /start/run.sh

WORKDIR /code

RUN useradd -s /bin/bash user

RUN chown -R user /code

CMD /start/run.sh
