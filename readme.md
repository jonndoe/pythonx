



Pythonx NOTES app.
=======================


This project is based on the amazing [Wagtail CMS](https://github.com/wagtail/wagtail).

This project is set up to be test-deployed with github-Actions CI/CD.

docker containers: 

- wagtail + uwsgi
- nginx 
- postgres 
- redis 
- elasticsearch 
- traefik+SSL


RUN WITH DOCKER LOCALLY:

-----------------

#### Dependencies
* [Docker](https://docs.docker.com/engine/installation/)
* [Docker Compose](https://docs.docker.com/compose/install/)

### Installation
Run the following commands to run project locally with traefik and nginx:

```bash
git clone git@github.com:jonndoe/pythonx.git
cd pythonx
sudo docker-compose -f docker-compose.local.traefik.nginx.yml up --build
sudo docker-compose -f docker-compose.local.traefik.nginx.yml exec app /venv/bin/python manage.py load_initial_data
```

The demo site will now be accessible at [http://127.0.0.1:80/](http://localhost:80/) and the Wagtail admin
interface at [http://127.0.0.1:80/admin/](http://localhost:80/admin/).

Log into the admin with the credentials ``admin / changeme``.

**Important:** The `bakerydemo/collect_static` folder will be created. 

- Either You have to change permission to amemd css files for hot reload.

- Or you have to edit css files in bakerydemo/static folder and then run 
`sudo docker-compose -f docker-compose.local.traefik.nginx.yml exec app /venv/bin/python manage.py collectstatic`
  to update the site.



RUN WITH DOCKER ON REMOTE HOST:
-----------------

#### Dependencies
* [Docker](https://docs.docker.com/engine/installation/)
* [Docker Compose](https://docs.docker.com/compose/install/)

### Installation
Every time you make `git push origin master` from you local machine, githubCI/CD will build containers, and push them onto remote host.
Settings include SSL certificates receiving.
After successfull deploy you able to visit:
- http://www.hostname.com
- https://www.hostname.com
- https://hostname.com

But you wont see site data, we need to load it:

- `ssh user@yourhostIPaddress`

- `cd /app`

- `sudo docker-compose -f docker-compose.prod.traefik.ssl.yml exec app /venv/bin/python manage.py load_initial_data` 

The demo site will now be accessible at [https://youdomainname.com:80/](https://youdomainname.com:80/) and the Wagtail admin
interface at [https://youdomainname.com:80/](https://youdomainname.com:80/).

Log into the admin with the credentials ``admin / changeme``.

**Important:** The important info to be here.

####  Set nginx --> /code directory permissions to be able to load images!!! ####
- `sudo docker container exec -it app_nginx_1 chmod 777 -R /code`

### DO THE FOLLOWING FOR CORRECT WORK:
- add new site in site settings with `www.yousitename.com` and port `80`
- set old site as not default (untick it)
- set new site as default (tick)
- delete old site (`127.0.0.1` and port `8000`)

otherwise comments will not work and other problems will arise
such as `Internal server error` and problems with search bar.



### Sending email from the contact form

The following setting in `base.py` and `production.py` ensures that live email is not sent by the demo contact form:

`EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'`

In production on your own site, you'll need:

- create yandex mail box for your domain
- confirm yandex mail box https://yandex.ru/support/webmaster/service/rights.html
- add entries in your DNS record, and wait for it to update(yandex wiil return spam error if not yet updated)

  IN settings.py:

`EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'`

`EMAIL_HOST = 'smtp.yandex.ru'`

`EMAIL_HOST_USER = 'domainmail@yandex.ru'`

`EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')`

`EMAIL_PORT = 587`

`EMAIL_USE_TLS = True`

`SERVER_EMAIL = EMAIL_HOST_USER`

`DEFAULT_FROM_EMAIL = EMAIL_HOST_USER`


and configure [SMTP settings](https://docs.djangoproject.com/en/1.10/topics/email/#smtp-backend) appropriate for your email provider.


### Notes:
https://yandex.ru/support/mail/bounces/other.html

https://postmaster.yandex.ru/

