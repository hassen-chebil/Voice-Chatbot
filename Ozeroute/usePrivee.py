from voiceSetup import Speaker
from queue import Queue
import requests
import json

def getOzerouteOffors(nbad, nben, nbby , depDet ,dateTime, arrDet , speaker, qu):
    url = "https://api.ozeroute.com/v1/common/offers"

    payload = json.dumps({
            "locale": "fr",

            "passengers":[
                {
                    "type": {
                        "code": "adult"
                    },
                    "number": nbad
                    },

                    {
                    "type": {
                        "code": "infant"
                    },
                    "number": nben
                    },

                    {
                    "type": {
                        "code": "baby"
                    },
                    "number": nbby
                }],

            "from": {
                    "dateTime": dateTime,
                    "place": depDet
                },
            "to": {
                    "place": arrDet
                }
})
          
    print(payload)   

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Origin': 'https://www.ozeroute.com',
        'Referer': 'https://www.ozeroute.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }


    response = requests.request("POST", url, headers=headers, data=payload).json()
    print(response)
    if response == {} or response == []:
        return False
    
    elif response == "Error response, please try again":
        speaker.talk(qu, "Invalid response! API error...")
        return False
    elif response != {} or response != []:
        if response == False:
            return False
    else:
        return False

    with open("ozeroute.json", "w") as resultFile:
        json.dump(response, resultFile)
    
    return "ozeroute.json"
