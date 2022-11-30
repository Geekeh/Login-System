import requests
from time import sleep
import os
os.system("cls")
key = input("Key: ")
r = requests.post('link to domain', headers=({"key":key}))
sleep(30)
