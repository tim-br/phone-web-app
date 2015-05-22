from flask import Flask, render_template
from twilio.util import TwilioCapability
import twilio.twiml
 
app = Flask(__name__)
 
# Add a Twilio phone number or number verified with Twilio as the caller ID
caller_id = "+12125551234"
 
@app.route('/voice', methods=['GET', 'POST'])
def voice():
    resp = twilio.twiml.Response()
 
    # Nest <Client> TwiML inside of a <Dial> verb
    with resp.dial(callerId=caller_id) as r: 
        r.client("jenny")
 
    return str(resp)
 
@app.route('/client', methods=['GET', 'POST'])
def client():
    """Respond to incoming requests."""
 
    # Find these values at twilio.com/user/account
    account_sid = "AC7eb559bac7b781f9661ab6b6037a46aa"
    auth_token = "9c40234e89420f6f109df6b94d8f8b73"
 
    capability = TwilioCapability(account_sid, auth_token)
 
    application_sid = "AP96e878a5309066364d090f9050117d40" # Twilio Application Sid
    capability.allow_client_outgoing(application_sid)
    capability.allow_client_incoming("jenny")
    token = capability.generate()
 
    return render_template('client.html', token=token)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0')
