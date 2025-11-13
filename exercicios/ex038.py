import urllib.request
import os

os.system('cls')


castleform = 'https://castelform.pt/'

try:
    tenta = urllib.request.urlopen(castleform)
except Exception as e:
    print(repr(e))
else:
    print(tenta)