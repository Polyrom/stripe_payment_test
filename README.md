## Basic Django E-commerce app with configured Stripe payment

 **Stack**:
+ Python 3.10
+ Django 4.1
+ SQLite (Dev) / PostgreSQL (Prod)
+ Stripe
+ Bootstrap 4

### Click here to visit the page:
### [Demo on Railway](https://stripepaymenttest-production.up.railway.app/)

## Installation
Clone the repository
```
git clone https://github.com/Polyrom/stripe_payment_test
cd stripe_payment_test
```
Install dependencies if you use **Poetry**
```
make install
```

Install dependencies if you use **Docker**

```
make docker-install
```

Create an .env file
```
cd stripe_payment_test
touch .env
```
Populate the .env file with the following values:
```
DEBUG=True
DB_ENGINE=SQLite
SECRET_KEY=your_Django_secret_key (may be generated with 'make secretkey' command)
STRIPE_SECRET_KEY=may be obtained from your Stripe account
STRIPE_PUBLISHABLE_KEY=may be obtained from your Stripe account
```

Finish installation **from the project's root directory**
```
make makemigrations
make migrate
make createsuperuser
```
Now can run the app on you localhost
```
make start
```
## Description
You are free to browse this basic E-Commerce web app, "buying" items
right off the item detail page or by adding any number of items to cart to check out with a few of them.
Upon pressing on "Buy" or "Checkout" buttons you are redirected to a dummy Stripe checkout page.

**NOTE**:
You can "buy" single items without signing up, but adding/checking out from cart is possible **only for logged in users**.

**Extra methods**

Returns Stripe checkout session ID associated with the chosen item:

```
curl -X GET hostname/buy/<item_number>/
```

Returns Stripe checkout session ID associated with the chosen order:

```
curl -X GET hostname/checkout/<order_number>/
```

**Linter check**:

[![flake8](https://github.com/Polyrom/stripe_payment_test/actions/workflows/flake8.yml/badge.svg)](https://github.com/Polyrom/stripe_payment_test/actions/workflows/flake8.yml)