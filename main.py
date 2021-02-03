import adal
import json
import requests
import graphene
from graphqlclient import GraphQLClient
tenant = 'grotabyte.onmicrosoft.com'
app_id = 'd08c41e3-c8e3-4cb6-a421-0e5114cd0762'
app_password = 'qsZI07r.a9cz~~g_691MwmD-EG85Q_N4c_'
username='arooba.rehman@grotabyte.com'
password=''

#userAccount = '<user account you want to create mail draft>'

resource_URL ='https://graph.microsoft.com'
#authority_url = 'https://login.microsoftonline.com/%s'%(tenant)
authority_url='https://login.microsoftonline.com/%s'%(tenant)

context = adal.AuthenticationContext(
    authority_url
)
token=context.acquire_token_with_username_password(resource_URL, username, password, app_id)
#token = context.acquire_token_with_client_credentials(
    #resource_URL,
    #app_id,
    #app_password)
print(token)
request_headers = {'Authorization': 'bearer %s'%(token['accessToken'])}

print(token['accessToken'])
url='https://graph.microsoft.com/beta/users'
#url='https://graph.microsoft.com/beta/users/28264df9-9186-43ea-9af6-e95ff3ca8c80/chats'
result=requests.get(url,headers=request_headers)
print(result.text)
text=result.text
print("type of result.text")
print(type(text))
print("Result of The Content")
print(result.content)
content=result.content
print("content of result.content")
print(type(content))
# user extraction through microsoft graph using graphql client
client = GraphQLClient('https://graph.microsoft.com/beta/users/0db52353-9e9c-45f2-afdc-f10e11ba0ffc/chats')
client.inject_token(token,request_headers)


query='''
 {
    
        {
            id,
            topic,
            createdDateTime,
            lastUpdatedDateTime,
            chatType
        },
 }
 
'''
final=client.execute(query=query, variables=None)
y = json.dumps(text)

# the result is a JSON string:
print(y)