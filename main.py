import redis  # импортируем библиотеку
import json  # так-так-так, кто это тут у нас? Наш старый друг Джейсон заглянул на огонёк! Ну привет, чем ты сегодня нас порадуешь?

red = redis.Redis(
    host='redis-17682.c135.eu-central-1-1.ec2.cloud.redislabs.com',
    # ваш хост, если вы поставили Редис к себе на локальную машину, то у вас это будет localhost. Если же вы находитесь на Windows, то воспользуйтесь полем host из вашей облачной БД, которую мы создавали в скринкасте.
    port=17682,
    # порт подключения. На локальной машине это должно быть 6379. Для пользователей облачного сервиса порт всегда разный, поэтому его надо копировать оттуда же, что и host.
    password='AOA0H11O4d4XGwodr9YjsQ6aIK6cV3Pq'
    # для локальной машины пароль не требуется (если вы устанавливали Редис к себе на компьютер и не пользовались облачным сервисом из скринкаста выше). Для пользователей облачного сервиса пароль находится в вашей облачной базе данных в поле password
)

cont = false

while cont:
    action = input('action:\t')
    if action == 'write':
        name = input('name:\t')
        phone = input('phone:\t')
        red.set(name, phone)
    elif action == 'read':
        name = input('name:\t')
        phone = red.get(name)
        if phone:
            print(f'{name}\'s phone is {str(phone)}')
    elif action == 'delete':
        name = input('name:\t')
        phone = red.delete(name)
        if phone:
            print(f"{name}'s phone is deleted")
        else:
            print(f"Not found {name}")
    elif action == 'stop':
        break