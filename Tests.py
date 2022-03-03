import requests, json


resp = requests.get("https://api.ask-jennie.com/v1/angular/ui-lib?app_name=bootstrapaccordion", headers={"token": "7f2d26281291b158ffe6a454fbd744d8cba422fa"})
print (json.dumps(resp.json()))

# # def file_upload_test():
# RESP = upload_text_file("/Users/saurabhpandey/Desktop/ASKJennie/askjenniebackend/README.md", "7f2d26281291b158ffe6a454fbd744d8cba422fa", "someapp", "angular-ui-lib")
# print (RESP.json())

# def image_upload_test():