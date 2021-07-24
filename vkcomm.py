import vk_api, time, os, sys
from colorama import init, Fore
from time import sleep
from python_json_config import ConfigBuilder

builder = ConfigBuilder()
config = builder.parse_config('config.json')

init()
a = 1
banner = ("""
───╔╗────────────────────╔╗────────╔═╗╔═╗
───║║───────────────────╔╝╚╗───────║╔╝║╔╝
╔╗╔╣║╔╗╔══╦══╦╗╔╦╗╔╦══╦═╬╗╔╬══╗╔══╦╝╚╦╝╚╗
║╚╝║╚╝╝║╔═╣╔╗║╚╝║╚╝║║═╣╔╗╣║║══╣║╔╗╠╗╔╩╗╔╝
╚╗╔╣╔╗╗║╚═╣╚╝║║║║║║║║═╣║║║╚╬══║║╚╝║║║─║║
─╚╝╚╝╚╝╚══╩══╩╩╩╩╩╩╩══╩╝╚╩═╩══╝╚══╝╚╝─╚╝
Author: Klimenko&Ofkotov\n""")
token = config.token
rts = config.owner_id
post = config.post_id
message = config.message

vk = vk_api.VkApi(token=token)
vk._auth_token()

while True:
    try:
        response = vk.method("wall.createComment", {"owner_id": rts, "post_id": post, "message": message})
        os.system('cls||clear')
        print(Fore.MAGENTA + banner)
        print(Fore.GREEN + f'Оставлен комментарий с текстом "{message}" #' + str(a))
        a += 1
        sleep(5)
    except vk_api.exceptions.Captcha:
        os.system('cls||clear')
        print(Fore.RED + banner)
        print(f'Ошибка! Небходимо решить капчу\nЗадержка 30 сек.\n[Err!]#' + str(a))
        a += 1
        sleep(30)
    except vk_api.exceptions.ApiError:
        os.system('cls||clear')
        print(Fore.RED + banner)
        print(f'Ошибка! Токен не валиден или введен не верно\n[Err!]#' + str(a))
        a += 1
        sleep(30)
