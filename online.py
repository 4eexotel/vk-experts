import vk_api
import os
import time
while True:
	try:
		vk = vk_api.VkApi(token=os.environ["TOKEN_VK"])
		vk.method("account.setOnline")
		time.sleep(300)
	except Exception as e:
		#logging.error(str(datetime.now()) + " " +str(e))
		time.sleep(30)
 
