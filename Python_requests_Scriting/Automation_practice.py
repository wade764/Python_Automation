# information came from this video: https://youtu.be/tb8gHvYlCFs
# This is practice for scripting automation
# A good resource for this is httpbin.org

import requests

# input URL inside of the get function
#r = requests.get('')

# This will display a response code to the terminal
#print(r)

# This displays to the terminal a list of possible actions
#print(dir(r))

# Same as above but with detailed information
#print(help(r))

# Using one of the actions on the r variable will retrieve the specified data
#print(r.content)

# How to download an image
#with open('temp.jpg', 'wb') as f:
#    f.write(r.content)

# Simple way to print a status code
#print(r.status_code)

# How to get image header information
#print(r.headers)

# This is for a GET request
#payload = {'page': 2, 'count': 25}
#r = requests.get('https://httpbin.org/get', params=payload)

# This if for a POST request
#payload = {'username': '', 'password': ''}
#r = requests.post('https://httpbin.org/post', data=payload)

#print(r.headers)
#print(r.text)
#print(r.url)

# This makes a dictionary of the json outputed data
#print(r.json())

#r_dict = r.json()
#print(r_dict['form'])

# Trying out the /basic-auth request from httpbin.org
#r = requests.get('https://httpbin.org/basic-auth/username/password', auth=('username', 'password')) # the data inside the auth tuple must match the data in the url
#print(r.text)

# if you use the wrong credentials for the basic-auth request above you will get a Response [401], this can be seen with the following print
#print(r)

# testing timeout
#r = requests.get('https://httpbin.org/delay/6', timeout=3)

#print(r)
