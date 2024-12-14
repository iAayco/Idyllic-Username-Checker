#Check If Requests Module Installed
try:
    from requests import get as g
#If Not Installed
except ImportError as e:
    print('requests module not installed install it by `pip install requests`')
#This Is Username We Will Check
username = 'aayco'
#This Is Website Api To Check Username
url = f"https://api.idyllic.app/user/username/available?username={username}"
#Our Cute Headers
headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "en-US,en;q=0.9",
    "if-none-match": "W/\"12-hmATd20Po1LubS8F4M54fdYpka4\"",
    "origin": "https://us.idyllic.app",
    "priority": "u=1, i",
    "referer": "https://us.idyllic.app/",
    "sec-ch-ua": "\"Google Chrome\";v=\"131\", \"Chromium\";v=\"131\", \"Not_A Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?1",
    "sec-ch-ua-platform": "\"Android\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Mobile Safari/537.36"
}
#Get The Response From Website
response = g(url, headers=headers)
#Check If Status Code Is 400 (Username Already Exists)
if (response.status_code)==400:
    #Get The Error Message From Json Response
    errors = (response.json()['errors'])
    for error in errors:
        #Get The Msg From Error Message
        error = (error['msg'])
        #Print The Username With Msg
        print(f'{username} {error}')
else:
    #Print The Available Msg With Username
    print(f'{username} is Available')
