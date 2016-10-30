from flask import Flask, request, redirect

import message, sms, twilio.twiml

app = Flask(__name__)

# Index page: trigger hello_world() function
@app.route('/')
def hello_world():
    return 'Hello from Flask!'

# Webhook page: trigger webhooks() function
@app.route("/webhook", methods=['POST'])
def webhooks():

    # Get the json data
    json = request.json

    # parse the message id, person id, person email, and room id
    message_id = json["data"]["id"]
    person_id = json["data"]["personId"]
    person_email = json["data"]["personEmail"]
    room_id = json["data"]["roomId"]

    # convert the message id into readable text
    msg = message.retrieve(message_id)

    #send SMS
    sms.sendsms(msg)


@app.route("/sms", methods=['POST'])
def receiveSms():

    #XXXXXXX to mask actual ID's and email addresses
    botID="YXXXXXXXQ"
    botSandboxID="YXXXXXXX4"
    botEmail="etXXXXXXXl.com"

    number = request.form['From']
    message_body = request.form['Body']
    msg=str(message_body)

    status = message.forward(botID, botEmail, botSandboxID, msg)
