import requests
from .models import TeleSettings


def sendtelegram(tg_name, tg_phone)->None:
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = settings.tg_token
        chat_id = settings.tg_chat
        text = str(settings.tg_message)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
            part_1 = text[:text.find('{')]
            part_2 = text[text.find('}')+1:text.rfind('{')]
            part_3 = text[text.rfind('}'):-1]
            
            text_slice = part_1 + tg_name + part_2 + tg_phone + part_3
        else:
           text_slice = text 

        try:
            req = requests.post(method, data={'chat_id': chat_id, 'text': text_slice})
        except Exception as e:
            print(e)
        finally:
            if req.status_code != 200:
                print('Ошибка отправки')
            elif req.status_code == 500:
                print('Ошибка 500')
            else:
                print("Ок все отправилось")
    else:
        pass

