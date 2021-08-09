import os
from azure.identity import DefaultAzureCredential, ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient

credential = ManagedIdentityCredential()
print("credential: " + credential)
token = credential.get_token(scopes='6aa6c4c3-6fba-4f2d-ab09-9035c0e40c19/.default')
print(token)
# request = HttpRequest(
#   method='POST',
#   url='https://jacmarauthfunctest.azurewebsites.net/api/HttpTrigger1?code=CaDqYH0lM9N4zKjUBgZfiC/5Jlkf/nGDeq7yC0yZ0qL6cdDjfxIV5A==',
#   headers={"authorization": 'Bearer ' + token},
#   body={}
#   )
            
print("made it here")
#print(request)