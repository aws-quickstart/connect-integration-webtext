import json
import requests

print('Loading function')


def lambda_handler(event, context):
    # Print statements are commented out to avoid
    # over verbosity in logging. 
    # Print statements should only be uncommented
    # for debugging purposes ans should be commented out
    # when debugging is complete.

    # print("Received event: " + json.dumps(event, indent=2))
    ev = json.dumps(event)
    # print(ev)
    urly = "https://connect.webtext.us.com/v2/send-message"
    urlz = "http://connect.webtext.us.com/v2/enable-chat"
    headers = {'user-agent': 'aws_connect_GJ/0.0.1'}
    num = event['Details']['Parameters']['phone']
    api_usr = event['Details']['Parameters']['api_usr']
    api_pass = event['Details']['Parameters']['api_pass']
    txt = event['Details']['Parameters']['txt']
    cc_number = event['Details']['Parameters']['cc_number']

    try:
        channel = event['Details']['Parameters']['channel']
        # print("We have a channel")
    except:
        channel = "sms"
        # print("There is no channel")
        pass
    livechat = 0
    try:
        livechat = event['Details']['Parameters']['livechat']
        # print ("livechat param:" + str(livechat))
    except:
        livechat = 1
        # print ("no live chat param or no param")
        pass
    data = {
        "api_usr": api_usr,
        "api_pass": api_pass,
        "txt": txt,
        "phone": num,
        "cc_number": cc_number,
        "livechat": livechat,
        "channel": channel
    }

    r = requests.post(urly, headers=headers, data=json.dumps(data))
    # print("wrapper: status = " + r.text)
    res = r.json()
    # print("Wrapper response is: ")
    # print(res)
    auth_code = api_usr + api_pass
    data2 = {
        "auth_code": auth_code,
        "enable_chat": True
    }
    r2 = requests.post(urlz, headers=headers, json=data2)
    # print(r2.json())
    return ev  # Echo back the first key value

    raise Exception('Something went wrong')
