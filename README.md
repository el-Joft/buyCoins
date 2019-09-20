# buyCoins
This application converts bitcoin rates to naira based on exchange rate and margin

[![Build Status](https://travis-ci.org/el-Joft/buyCoins.svg?branch=develop)](https://travis-ci.org/el-Joft/buyCoins)

###Technologies

####Below is a list of technologies used to build this project

- Django
- GraphQL (Graphene)

###Installation

Follow these steps to set up the app.

Clone the repo:

```$ https://github.com/el-Joft/buyCoins.git```

#### Navigate to the project directory:

```$ cd buyCoins```

#### Create a virtual environment by running

```virtualenv buyCoins-env```

Activate the environment

```source buyCoins/bin/activate```

#### Running and Development
Install dependencies

``` pip install -r requirements.txt```

Start the application

``` python manage.py runserver```

Try out the endpoint with your GraphQL testing tool

```
query {
 calculatePrice(
  choiceType: BUY,
  margin: 2,
  exchangeRate: 360
) {
  calculatedPrice
  }
}

```

### Deployment

Deploy to Heroku

Using heroku tool belt 

```heroku login```

you should see
```
Enter your Heroku credentials:
Email: your_email@emailprovider.com
Password: *********

```

Prepare the app for deployment

run 

``touch Procfile``

Open the Procfile and add the line below.

```web: gunicorn djangoherokuapp.wsgi --log-file -```

Install additional packages

```
pip install gunicorn dj-database-url whitenoise psycopg2

```

if `psycopg2` throws error run `LDFLAGS=-L/usr/local/opt/openssl/lib pip3 install psycopg2`

Add them to the `requirements.txt`

`pip freeze > requirements.txt`

Setup staticfiles

Add the below to your settings, at the middleware
```
MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'whitenoise.middleware.WhiteNoiseMiddleware',
  # ...
]
```

add this at the bottom of your settings

```
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

import dj_database_url 
prod_db  =  dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(prod_db)
```

Create the Heroku App from the terminal

```
heroku create buycoins
```

Add the app domain name to ALLOWED_HOSTS in settings.py.

`ALLOWED_HOSTS = ['buycoins.herokuapp.com']`

Run 

```
$ git init
$ git remote add heroku https://git.heroku.com/buycoins.git
$ git add .
$ git commit -m "Initial commit"
$ git push heroku develop:develop 
$ heroku config:set DISABLE_COLLECTSTATIC=1 
$ git push heroku develop:develop 
```

Author: Timothy Omotayo


