## Basic Django E-commerce app with configured Stripe payment

 **Stack**:
+ Python 3.10
+ Django 4.1
+ PostgreSQL
+ Stripe
+ Bootstrap 4

### Click here to visit the page:
### [Demo on Railway](https://stripepaymenttest-production.up.railway.app/)

## Description
You are free to browse this basic E-Commerce web app, "buying" items
right off the item detail page or by adding any number of items to cart to check out with a few of them.
Upon pressing on "Buy" or "Checkout" buttons you are redirected to a dummy Stripe checkout page.

**NOTE**:
You can "buy" single items without signing up, but adding/checking out from cart is possible only for logged in users.

**Extra methods**

Returns Stripe checkout session ID associated with the chosen item:

`curl -X GET hostname/buy/<item number>/`

Returns Stripe checkout session ID associated with the chosen order:

`curl -X GET hostname/checkout/<order number>/`

**Linter check**:

[![flake8](https://github.com/Polyrom/stripe_payment_test/actions/workflows/flake8.yml/badge.svg)](https://github.com/Polyrom/stripe_payment_test/actions/workflows/flake8.yml)