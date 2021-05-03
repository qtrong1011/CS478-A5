import requests
import sys
#####Reading the command line argument################
if(len(sys.argv) == 2):
    url = 'http://127.0.0.1:5000/rps?filename=' + str(sys.argv[1])
else:
    url = 'http://127.0.0.1:5000/rps'

code = requests.get(url)

print(code.text)