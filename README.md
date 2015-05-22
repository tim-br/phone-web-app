# phone web app

This is a web app that I am building using the twilio api.

Currently it can receive calls.

I will soon add outgoing phone call capabilities, text messaging capabilities, and fix a few bugs.

I may perhaps add a login page so the page can be accessed remotely and still remain secure.

Eventually, I would like to port this app to phonegap on iOS and android.

A twilio account (which provides the api keys) is required.

To use the app clone the repo. It depends on the twilio-python module which can be installed via ```pip install twilio```.

The api keys are stored in the ```keys.json``` file, which can be formatted as follows:

{
  "account_sid":"XXXXXX",
  "auth_token":"XXXXXX",
  "application_sid":"XXXXXX"
}




