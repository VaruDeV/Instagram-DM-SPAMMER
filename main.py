import threading
from instagrapi import Client
from instagrapi.exceptions import ClientNotFoundError
from colorama import init, Back, Fore, Style
import os
import time
init()

os.system("title Msg Spammer by Techvy & cls")
print(f"{Fore.CYAN}[{time.strftime('%H:%M:%S')}] Trying to login in to the account.")
client = Client()
client.login("terimummymeri88", "knightpro")
print(f"[{time.strftime('%H:%M:%S')}] login success{Style.RESET_ALL}")

user_id = "49150641809"

print(f"{Fore.MAGENTA}[{time.strftime('%H:%M:%S')}] sending msges..")
{Style.RESET_ALL}
def send_message(num):
    {Fore.BLUE}
    message = f"Discord Tools & Methods"
    {Style.RESET_ALL}
    try:
        client.direct_send(message, [user_id])
        print(f"{Fore.GREEN}[{time.strftime('%H:%M:%S')}] successfully sent msg to user: {user_id}{Style.RESET_ALL}")
    except ClientNotFoundError:
        print(f"{Fore.RED}[{time.strftime('%H:%M:%S')}] User with id {user_id} not found.{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[{time.strftime('%H:%M:%S')}] failed to send msg n:{num} e: {str(e)}{Style.RESET_ALL}")


threads = []
for i in range(1, 100):
    t = threading.Thread(target=send_message, args=(i, ))
    threads.append
    t.start()
    

for t in threads:
    t.join()

client.logout()



