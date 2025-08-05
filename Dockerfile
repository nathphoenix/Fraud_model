FROM python:3.9

ARG USER=docker
ARG APP_NAME=gamification
ARG DD_PROFILING_ENABLED=true
ARG DD_ENV=uat/prod
ARG DD_VERSION=1.3.2

ENV DEBIAN_FRONTEND=noninteractive
ENV LANGUAGE=en_US.UTF-8
ENV TERM=xterm
ENV TZ=Africa/Lagos

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime \
    && echo $TZ > /etc/timezone

RUN pip install --upgrade pip

# COPY ./requirements.txt /requirements.txt
COPY ./requirements.txt app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

RUN apt-get update \
    && apt-get install gcc -y \
    && apt-get install -y wget \
    && apt-get clean \
    && apt-get install -y supervisor nginx sudo

RUN rm /etc/nginx/sites-enabled/* \
    && rm /etc/nginx/sites-available/*

RUN apt clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && rm /var/log/lastlog /var/log/faillog \
    && rm -rf /var/www/html/index.nginx-debian.html

COPY nginx/nginx.conf /etc/nginx/conf.d/default.conf


RUN adduser --uid 1001 --disabled-password --gecos '' ${USER} \
    && adduser ${USER} sudo \
    && echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER ${USER}

COPY . /app
# WORKDIR /var/www/html

# COPY . /var/www/html

RUN sudo chown -R ${USER}:www-data /var/www/html \
    && sudo chmod 777 -R /var/www/html \
    && sudo chmod -R 644 /etc/cron.d

EXPOSE 80
# ENTRYPOINT ["sudo", "start-container.sh"]
# ENTRYPOINT ["start-container.sh"]
# CMD python app.py
# CMD ["/usr/local/bin/start-container.sh"]
CMD ["gunicorn", "--workers=2", "--bind=0.0.0.0:80", "app:app"]