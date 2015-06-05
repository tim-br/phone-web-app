from flask import Flask, request, render_template
from twilio.util import TwilioCapability
import twilio.twiml
import json
import sys
import os
import re

app = Flask(__name__)

# Add a Twilio phone number or number verified with Twilio as the caller ID
caller_id = "+12125551234"

default_client = "Bob"
#load the json file containing api keys
file = open('keys.json')
data = json.load(file)



@app.route('/voice', methods=['GET', 'POST'])
def voice():
    dest_number = request.values.get('PhoneNumber', None)
    resp = twilio.twiml.Response()

    # Nest <Client> TwiML inside of a <Dial> verb
    with resp.dial(callerId=caller_id) as r:

	if dest_number and re.search('^[\d\(\)\- \+]+$', dest_number):
 	    r.number(dest_number)
	else:
	    r.client(default_client)
        #r.client("jenny")

    return str(resp)

@app.route('/client', methods=['GET', 'POST'])
def client():
    """Respond to incoming requests."""

    # Find these values at twilio.com/user/account
    account_sid = data["account_sid"]
    auth_token = data["auth_token"]

    capability = TwilioCapability(account_sid, auth_token)

    application_sid=data["application_sid"]
    capability.allow_client_outgoing(application_sid)
    capability.allow_client_incoming("jenny")
    token = capability.generate()

    return render_template('client.html', token=token)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

