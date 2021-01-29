from microsoftgraph.client import Client
import config
import requests
CLIENT_ID = 'd08c41e3-c8e3-4cb6-a421-0e5114cd0762'
CLIENT_SECRET = 'qsZI07r.a9cz~~g_691MwmD-EG85Q_N4c_'
Tenant_ID='4dabebe6-0f21-40e7-accd-8996c430c687'

AUTH_ENDPOINT = '/oauth2/v2.0/authorize'
TOKEN_ENDPOINT = '/oauth2/v2.0/token'
authority_host_uri = 'https://login.microsoftonline.com'
tenant = '4dabebe6-0f21-40e7-accd-8996c430c687'
authority_uri = authority_host_uri + '/' + tenant

scopes = ['User.Read','User.Read.All']
url='https://login.microsoftonline.com/4dabebe6-0f21-40e7-accd-8996c430c687/oauth2/v2.0/token'

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    print_hi('PyCharm')
    client = Client(CLIENT_ID, CLIENT_SECRET, account_type='by defect common', office365='true')
    url = client.authorization_url(authority_uri,scopes, state=None)
    print(url)
    print(CLIENT_ID)
    print(client)
    x = requests.post(url)
    print(x)
    print(x.headers)
    print(x.text)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
