## Basic Django app with configured payment via Stripe API

 **Stack**:
+ Python 3.10
+ Django 4.1
+ PostgreSQL
+ Stripe

**Basic usage**

Returns a basic HTML page with short item description and a "Buy" button:

`curl -X GET hostname/item/<itemnumber>/`

Upon pressing "Buy" button you are redirected to a test checkout page powered by Stripe

Returns Stripe checkout session ID associated with the chosen item:

`curl -X GET hostname/buy/<itemnumber>/`

**Linter check**:

[![flake8](https://github.com/Polyrom/stripe_payment_test/actions/workflows/flake8.yml/badge.svg)](https://github.com/Polyrom/stripe_payment_test/actions/workflows/flake8.yml)