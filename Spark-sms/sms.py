from twilio.rest import TwilioRestClient

##XXXXXXX to mask actual ID's, tokens, and numbers

account_sid = "AXXXXXXXd"
auth_token = "6XXXXXXX4b"
client = TwilioRestClient(account_sid, auth_token)

def sendsms (text):
    msg=str(text)

    message = client.messages.create(to="+44XXXXXXX7", from_="+44XXXXXXX9", body=msg)


