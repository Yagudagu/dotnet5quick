import os
from azure.identity import DefaultAzureCredential, ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient

# os.environ['AZURE_SUBSCRIPTION_ID'] = "de56834a-29cf-4e09-bd90-b7e93d6136a9"
# os.environ['AZURE_TENANT_ID'] = "9b8406ec-0d62-411b-a087-7aa02aa265ec"
# os.environ['AZURE_CLIENT_ID'] = "c2daa522-2517-4afe-a322-804c95dde128"
# os.environ['AZURE_CLIENT_SECRET'] = "44KvNW1krlR1IlWHE~js~1Jo~vk30_~vU_"

credential = DefaultAzureCredential()
token = credential.get_token('07609e79-08a9-42fd-b0e6-ac4f334e86e1/.default')
print(token)

# request = HttpRequest(
#   method='POST',
#   url='https://jacmarauthfunctest.azurewebsites.net/api/HttpTrigger1?code=CaDqYH0lM9N4zKjUBgZfiC/5Jlkf/nGDeq7yC0yZ0qL6cdDjfxIV5A==',
#   headers={"authorization": 'Bearer ' + token},
#   body={"name":"jacob"}
#   )
            
# print("made it here")
#print(request)