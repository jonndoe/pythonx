


Pythonx NOTES app.
=======================

This project is based on the amazing [Wagtail CMS](https://github.com/wagtail/wagtail).

This project is set up to be test-deployed with github-Actions CI/CD 

Run into docker containers: wagtail + uwsgi >> nginx >> postgres >> redis >> elasticsearch >> traefik+SSL


Setup with Docker
-----------------

#### Dependencies
* [Docker](https://docs.docker.com/engine/installation/)
* [Docker Compose](https://docs.docker.com/compose/install/)

### Installation
Run the following commands to test project locally with traefik and nginx:

```bash
git clone https://github.com/wagtail/bakerydemo-docker-prod.git
cd bakerydemo
docker-compose -f docker-compose.local.traefik.nginx.yml up --build
docker-compose run app /venv/bin/python manage.py load_initial_data
docker-compose up
```

The demo site will now be accessible at [http://localhost:80/](http://localhost:80/) and the Wagtail admin
interface at [http://localhost:80/admin/](http://localhost:80/admin/).

Log into the admin with the credentials ``admin / changeme``.

**Important:** This `docker-compose.local.traefik.nginx.yml` is configured for local testing only, and is _not_ intended for production use.


Setup with Virtualenv
---------------------
You can run the Wagtail demo locally without setting up Vagrant or Docker and simply use Virtualenv, which is the [recommended installation approach](https://docs.djangoproject.com/en/1.10/topics/install/#install-the-django-code) for Django itself.

#### Dependencies
* Python 3.4, 3.5 or 3.6
* [Virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
* [VirtualenvWrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) (optional)

### Installation

With [PIP](https://github.com/pypa/pip) and [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
installed, run:

    mkvirtualenv wagtailbakerydemo
    python --version

Confirm that this is showing a compatible version of Python 3.x. If not, and you have multiple versions of Python installed on your system, you may need to specify the appropriate version when creating the virtualenv:

    deactivate
    rmvirtualenv wagtailbakerydemo
    mkvirtualenv wagtailbakerydemo --python=python3.6
    python --version

Now we're ready to set up the bakery demo project itself:

    cd ~/dev [or your preferred dev directory]
    git clone https://github.com/wagtail/bakerydemo.git
    cd bakerydemo
    pip install -r requirements/base.txt

Next,  we'll set up our local environment variables. We use [django-dotenv](https://github.com/jpadilla/django-dotenv)
to help with this. It reads environment variables located in a file name `.env` in the top level directory of the project. The only variable we need to start is `DJANGO_SETTINGS_MODULE`:

    $ cp bakerydemo/settings/local.py.example bakerydemo/settings/local.py
    $ echo "DJANGO_SETTINGS_MODULE=bakerydemo.settings.local" > .env

To set up your database and load initial data, run the following commands:

    ./manage.py migrate
    ./manage.py load_initial_data
    ./manage.py runserver

Log into the admin with the credentials ``admin / changeme``.


### Sending email from the contact form

The following setting in `base.py` and `production.py` ensures that live email is not sent by the demo contact form.

`EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'`

In production on your own site, you'll need:

- create yandex mail box for your domain
- confirm yandex mail box https://webmaster.yandex.ru
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


