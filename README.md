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

