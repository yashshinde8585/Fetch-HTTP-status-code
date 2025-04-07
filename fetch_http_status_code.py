from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from urllib.parse import urlparse
import emoji

# Taking input URL from user
requestURL = input("Enter the URL to be invoked: ")

# Parse the scheme (http, https, file, etc.)
scheme = urlparse(requestURL).scheme

try:
    response = urlopen(requestURL)

    if scheme in ['http', 'https']:
        print('Status code : ' + str(response.code) + ' ' + emoji.emojize(':thumbs_up:'))
        print('Message : Request succeeded. Request returned message - ' + response.reason)
    elif scheme == 'file':
        print('Status : File accessed successfully ' + emoji.emojize(':open_file_folder:'))
        print('Message : Local file opened successfully.')
    else:
        print('Status : Unknown scheme ' + emoji.emojize(':question:'))
        print('Message : The URL scheme is not supported.')
        
except HTTPError as e:
    print('Status : ' + str(e.code) + ' ' + emoji.emojize(':thumbs_down:'))
    print('Message : Request failed. Request returned reason - ' + e.reason)
except URLError as e:
    print('Status :', str(e.reason).split(']')[0].replace('[', '') + ' ' + emoji.emojize(':thumbs_down:'))
    print('Message : ' + str(e.reason).split(']')[1])
