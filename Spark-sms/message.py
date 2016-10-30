# import the requests library so we can use it to make REST calls
import requests

# disable warnings about using certificate verification
requests.packages.urllib3.disable_warnings()

# Function to retrieve a message from Spark
def retrieve(message_id):
    #Access Token from developer.ciscospark.com
    #XXXXXXX to mask actual token
    AccessToken="Bearer MXXXXXXXj"

    # add authorization to the header
    header = {"Authorization": "%s" %AccessToken}

    # create request url using message ID
    url_get = "https://api.ciscospark.com/v1/messages/" + message_id

    # send the GET request and do not verify SSL certificate
    api_response = requests.get(url_get, headers=header, verify=False)

    # parse the response in json
    response_json = api_response.json()

    # get the text value from the response
    text = response_json["text"]

    # return the text value
    return text


# Function to forward a message to Spark
def forward(person_id, person_email, room_id, text):

    #Access Token from developer.ciscospark.com
    #XXXXXXX to mask actual token
    AccessToken="Bearer MXXXXXXXj"

    # add authorization to the header
    header = {"Authorization": "%s" %AccessToken, "content-type": "application/json"}

    # specify request url
    url_post = "https://api.ciscospark.com/v1/messages"

    # create message in Spark room
    payload = {
        "personId" : person_id,
        "personEmail" : person_email,
        "roomId" : room_id,
        "text" : text
    }

    # create POST request do not verify SSL certificate for simplicity of this example
    api_response = requests.post(url_post, json=payload, headers=header, verify=False)

    # get the response status code
    response_status = api_response.status_code

    # return the text value
    return str(response_status)
