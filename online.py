import vk_api
import time
import os

token = os.environ['TOKEN_VK']

session = vk.Session(access_token = token)
api = vk.API(session, v = "5.95")
while True:
    exit = api.account.setOnline(voip = 0)
    time.sleep(180)
