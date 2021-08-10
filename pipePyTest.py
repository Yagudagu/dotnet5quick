import os
from azure.identity import DefaultAzureCredential, ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient

credential = ManagedIdentityCredential()
token = credential.get_token('4815043d-dd36-4ffd-80fb-1e5736923579/.default')
print(token)
# request = HttpRequest(
#   method='POST',
#   url='https://jacmarauthfunctest.azurewebsites.net/api/HttpTrigger1?code=CaDqYH0lM9N4zKjUBgZfiC/5Jlkf/nGDeq7yC0yZ0qL6cdDjfxIV5A==',
#   headers={"authorization": 'Bearer ' + token},
#   body={}
#   )
            
print("made it here")
#print(request)