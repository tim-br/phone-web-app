from flask import Flask, request, render_template
from twilio.util import TwilioCapability
import twilio.twiml
import json

 
import re
 
app = Flask(__name__)

#load the json file containing api keys
file = open('keys.json')
data = json.load(file)

# Add a Twilio phone number or number verified with Twilio as the caller ID
caller_id = data["my_phone_number"]
 
# put your default Twilio Client name here, for when a phone number isn't given
default_client = "jenny"

 
@app.route('/voice', methods=['GET', 'POST'])
def voice():
    dest_number = request.values.get('PhoneNumber', None)
 
    resp = twilio.twiml.Response()
 
    with resp.dial(callerId=caller_id) as r:
        # If we have a number, and it looks like a phone number:
        if dest_number and re.search('^[\d\(\)\- \+]+$', dest_number):
            r.number(dest_number)
        else:
            r.client(default_client)
 
    return str(resp)
 
@app.route('/client', methods=['GET', 'POST'])
def client():
    """Respond to incoming requests."""
 
    # Find these values at twilio.com/user/account
    account_sid = data["account_sid"] 
    auth_token = data["auth_token"] 
 
    capability = TwilioCapability(account_sid, auth_token)
 
    application_sid = data["application_sid"] # Twilio Application Sid
    capability.allow_client_outgoing(application_sid)
    capability.allow_client_incoming("jenny")
    token = capability.generate()
 
    return render_template('client.html', token=token)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0')
