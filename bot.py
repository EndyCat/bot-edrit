from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_default_config
import random, string, threading
import vk_api, json, time
from vk_api.longpoll import VkLongPoll, VkEventType
from multiprocessing import Process

tempr = "6e317c69117060413702409ce1bd3e17b2e7da6433bf298848db269ae2bfd2669233d2fa5a9ca834a352c"

config_dict = get_default_config()
config_dict['language'] = 'ru'
API = ('7d06866815dc03f33c839a93c9d16e98')
owm = OWM(API, config_dict)
mgr = owm.weather_manager()
vk_session = vk_api.VkApi(token = '4665bbef43b4b034fa87c683babfadef46b0dcd00e4d624e390f2525afe360997c64536c8ceae1dc16471')
vk = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
def randompassword():
  chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
  size = random.randint(8, 12)
  return ''.join(random.choice(chars) for x in range(size))
def get_but(text, color):
    return {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"" + "1" + "\"}",
                    "label": f"{text}"
                },
                "color": f"{color}"
            }
keyboard = {
    "one_time" : False,
    "buttons" : [
        [get_but('Пикчи', 'positive'), get_but('Айпи', 'positive')],
        [get_but('Взлом', 'secondary'), get_but('Дудос', 'secondary')],
        [get_but('Кто', 'primary'), get_but('Музыка', 'primary')]
    ]
}
keyboard = json.dumps(keyboard, ensure_ascii = False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))
def sender(id, text):
    vk_session.method('messages.send', {'user_id' : id, 'message' : text, 'random_id' : 0, 'keyboard' : keyboard})
def send_sticker(id, num):
    vk.messages.send(user_id = id, sticker_id = num, random_id = 0)
def send_foto(id, url):
    vk.messages.send(user_id = id, attachment = url, random_id = 0)
def ddos(text):
  text.replace('дудос', '', 1)
  sender(id, 'Сейчас, только линукс открою...')
  sender(id, 'Успешно положил' + text.replace('дудос', '', 1) + ' с помощью дудоса!')
def ip(text):
  text.replace('айпи', '', 1)
  sender(id, 'Сейчас, только линукс открою...')
  sender(id, 'Успешно вычеслил айпи' + text.replace('айпи', '', 1) + ' - ' + str( random.randint(100, 199)) + '.' + str(random.randint(10, 99)) + '.' + str(random.randint(10, 19)) + '.' + str(random.randint(100, 199)) )
def hack(text):
  text.replace('взлом', '', 1)
  sender(id, 'Сейчас, только линукс открою...')
  sender(id, 'Успешно взломал' + text.replace('взлом', '', 1) + ' - ' + randompassword())
def who(text):
  sender(id, 'Кажется' + text.replace('кто', '', 1) + ' это - @id' + str(random.randint(100000000, 799999999)) )
music_no_ap = ['audio484810309_456239084', 'audio484810309_456239134', 'audio484810309_456239129' ]
anonyms = {
    'едрить колотить' : 'photo-200253619_457239028',
    'ёп твою налево' : 'photo-200253619_457239027',
    'твою дивизию' : 'photo-200253619_457239029',
    'ёшки картошки' : 'photo-200253619_457239030',
    'ёпстудэй' : 'photo-200253619_457239031',
    'ёшки бомбёжки' : 'photo-200253619_457239032',
    'ёшкин кот' : 'photo-200253619_457239033',
    'ёкалем' : 'photo-200253619_457239034',
    'гвоздь мне в кеды' : 'photo-200253619_457239035',
    'едрид мадрид' : 'photo-200253619_457239036',
    'ёлы палы' : 'photo-200253619_457239037',
    'ёк макарёк' : 'photo-200253619_457239038',
    'ёшки матрёшки' : 'photo-200253619_457239039',
    'ёкалемене' : 'photo-200253619_457239040',
    'укуси меня пчела' : 'photo-200253619_457239041',
    'ёперный театор' : 'photo-200253619_457239042',
    'египетская сила' : 'photo-200253619_457239043',
    'египитская сила' : 'photo-200253619_457239044',
    'ёкарный карлибалет' : 'photo-200253619_457239045',
    'ёшкин матрёшкин' : 'photo-200253619_457239046',
    'ёкарный бабай' : 'photo-200253619_457239047',
    'едрён батон' : 'photo-200253619_457239048',
    'ёксель моксель' : 'photo-200253619_457239049',
    'ёлки иголки' : 'photo-200253619_457239050',
    'едрить его в корень' : 'photo-200253619_457239052',
    'повезло повезло' : 'photo-200253619_457239053',
    'не повезло не повезло' : 'photo-200253619_457239054',
    'святые угодники' : 'photo-200253619_457239055',
    'футы нуты' : 'photo-200253619_457239056',
    'какаем' : 'photo-200253619_457239057',
    'ёп твою направо' : 'photo-200253619_457239058',
    'за мат извени' : 'photo-200253619_457239059',
    'египетские силы' : 'photo-200253619_457239060',
    'мама дорогая' : 'photo-200253619_457239061',
    'взлом жопы' : 'photo-200253619_457239062',
    'кот' : 'photo-200253619_457239063',
    'админ' : 'photo-200253619_457239064',
    'едрить в корыто' : 'photo-200253619_457239065',
    'ёшкин свет' : 'photo-200253619_457239066',
    'ядрёна вошь' : 'photo-200253619_457239067',
    'блин блинский' : 'photo-200253619_457239111'
}
def thread_function():
    while True:
        try:
            sender(484810309, 'Бот, работает!')
            time.sleep(3600)
        except:
            pass
if __name__ == "__main__":
    x1 = threading.Thread(target=thread_function, args=())
    x1.start()
while True:
    try:
        longpoll = VkLongPoll(vk_session)
        for event in longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW:
                if event.to_me or event.from_chat:
                    msg = event.text.lower()
                    id = event.user_id
                    user_get=vk.users.get(user_ids = (id))
                    user_get=user_get[0]
                    u_name=user_get['first_name']
                    try:
                        if msg in ('привет', 'хай', 'здарова', 'здравствуй'):
                            sender(id, 'Привет ' + u_name )
                            send_sticker(id, 11238)
                        elif msg == 'пока':
                            sender(id, 'Пока '+u_name+', надеюсь ещё увидимся!')
                            send_sticker(id, 16923)
                        elif msg in ('начать', 'старт', 'команды', '/start'):
                            sender(id, '''Вот мои команды -
                                Я умею отправлять случайные пикчи! Просто напиши что угодно.
                                Я умею просто отвечать на обыдиные слова по типу \"Привет, пока, спасибо\".

                                Написав название пикчи можно её получить.

                                РП КОМАНДЫ:
                                Дудос - дусосит что напишите
                                Взлом - взломает что попросите
                                Айпи - узнаёт айпи чего хотите
                                Кто - узнаёт id vk кого-то
                                Погода - узнаёт погоду в городе

                                Если бот не отвечает то отправте сообщение несколько раз, может быть у вас закрыта личка.
                                Бот в разработке так что каждый может помочь написав идеи в лс - @endy_cat''')
                            send_foto(id, 'photo-200253619_4572393' + str(random.randint(14, 69)))
                        elif msg == 'спасибо':
                            sender(id, 'Это тебе спасибо что пользуешся мною!')
                            send_sticker(id, 20357)
                        elif msg == 'пикчи':
                            send_foto(id, 'photo-200253619_4572393' + str(random.randint(14, 69)))
                            send_foto(id, 'photo-200253619_4572393' + str(random.randint(14, 69)))
                            send_foto(id, 'photo-200253619_4572393' + str(random.randint(14, 69)))
                        elif msg in anonyms:
                            send_foto(id, anonyms[msg])
                        elif '?' in msg:
                            send_sticker(id, 11262)
                        elif 'дудос' in msg:
                            ddos(msg)
                        elif 'айпи' in msg:
                            ip(msg)
                        elif 'взлом' in msg:
                            hack(msg)
                        elif 'кто' in msg:
                            who(msg)
                        elif msg == 'пак':
                            sender(id, u_name + ', это пак моих пикчей, его можно распоковать любым архиватором.')
                            send_foto(id, 'doc484810309_591742077')
                        elif 'музыка' in msg:
                            send_foto(id, random.choice(music_no_ap))
                            send_foto(id, 'audio_playlist484810309_16')
                        try:
                            if 'погода' in msg:
                                observation = mgr.weather_at_place(msg.replace('погода' ' ', '', 1))
                                w = observation.weather
                                temperature = w.temperature('celsius')['temp']
                                stroka = 'В городе ' + msg.replace('погода' ' ', '', 1) + '   ' + str(temperature) + '° грдаусов!'
                                sender(id, stroka)
                        except:
                            sender(id, 'Вы указали неправильный город!')
                        elif msg == 'пак':
                            sender(id, u_name + ', это пак моих пикчей, его можно распоковать любым архиватором.')
                            send_foto(id, 'doc484810309_591742077')
                        else:
                            send_foto(id, 'photo-200253619_4572393' + str(random.randint(14, 69)))
                    except:
                        sender(484810309, 'Warning in chat!' + traceback.format_exc())
    except:
        longpoll = VkLongPoll(vk_session)

