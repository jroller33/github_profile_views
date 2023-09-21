import requests
import random
import time

from datetime import datetime
from hidden import github_url

# import pyautogui
# import subprocess
# import pygetwindow

# from custom_functions import tab_sleep, tab_rand_sleep, space_rand_sleep, write_rand_sleep, down_rand_sleep, enter_rand_sleep, write_rs_tab_rs, for_tab_sleep_range, generate_email, generate_phone, generate_relationship, generate_address

# from names import first_name_list, last_name_list

run_count = 0
# max_loop = random.choice(range(100,150))
max_loop = 1
rand_run_id = random.choice(range(1,10000))

try:
    while run_count <= max_loop:      # run_count starts at 0 and is incremented at the end of this loop

        start_now = datetime.now()
        start_timestamp_str = f'{start_now:%H.%M.%S_%m.%d.%Y}'
        current_date = f'{start_now:%m.%d.%Y}'
        print(f"[***] Starting new GH bot run at run_count:{run_count}, max_loop:{max_loop}, rand_run_id:{rand_run_id} [{start_timestamp_str}]")


        response = requests.get(f'{github_url}')
        print(response)

        time.sleep(2)


        run_count += 1

except KeyboardInterrupt:       # press CTRL-C to exit while the bot is running
    print(f"[!] GH bot exited at run_count: {run_count}")