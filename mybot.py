import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import time


vk = vk_api.VkApi(login = '87773830616', password = 'RE2122')
vk.auth()
longpoll = VkLongPoll(vk)


while True:
    try:
        for event in longpoll.listen():
            if (event.type == VkEventType.MESSAGE_NEW):
                if (event.to_me):
                    vk.method('messages.send', {'peer_id': event.peer_id, 'message': event.text})
    except:
        print('Ошибочка. Я АФК на 30 сек.')
        time.sleep(30)
