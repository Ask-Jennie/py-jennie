import requests

class APICalls():
    def get(self, url, headers=None, params=None):
        if params != None:
            split_keyword = "?"
            for key in params:
                url += split_keyword + key + "=" + params[key]
                split_keyword = "&"
        response = requests.get(url, headers=headers)
        print("Make API Call", response.status_code)
        return response.json()

    def post(self, url, headers=None, body=None):
        if headers == None:
            headers = {"Content-type": "application/json"}
        response = requests.post(url, headers=headers, json=body)
        print("Make API Call", response.status_code)
        return response.json()

    def put(self, url, headers=None, body=None):
        if headers == None:
            headers = {"Content-type": "application/json"}
        response = requests.put(url, headers=headers, json=body).json()
        print("Make API Call", response.status_code)
        return response.json()

    def delete(self, url, headers=None, body=None):
        if headers == None:
            headers = {"Content-type": "application/json"}
        response = requests.delete(url, headers=headers, json=body).json()
        print("Make API Call", response.status_code)
        return response.json()