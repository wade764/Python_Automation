# This is practice for scripting automation
# A good resource for this is httpbin.org


import requests

# input URL inside of the get function
r = requests.get('')

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


