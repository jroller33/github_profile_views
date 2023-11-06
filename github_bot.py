# github profile views bot

import requests
import random
import time

from requests.exceptions import HTTPError
from datetime import datetime
from hidden import github_url

run_id = random.choice(range(1,100000))     # used to identify a particular run in the log file. This ID is the same for all runs in one particular max_loop (ie this ID will be different each time this script runs overall, not each time the bot accesses the site)

response = requests.get(github_url)
response_list = response.text.splitlines()
count = ((response_list[-3]).strip())[21:-7]    # takes the response object and strips everything except the profile count

max_loop = int(input(f"\nCurrent profile views: {count}\nHow many times do you want to run the GH bot? "))

for run in range(max_loop):      
    try:
        # make a timestamp for this run, and print message
        start_now = datetime.now()
        start_timestamp_str = f'{start_now:%H.%M.%S_%m.%d.%Y}'
        current_date = f'{start_now:%m.%d.%Y}'
        print(f"[***] Starting new GH bot run at run:{run}, max_loop:{max_loop}, run_id:{run_id} [{start_timestamp_str}]")

        # Get the response object from the url that's requested, then sleep to finish loading
        response = requests.get(github_url)
        time.sleep(1)

        if response:    # response returns boolean when it's in a conditional statement
            response_list = response.text.splitlines()
            count = ((response_list[-3]).strip())[21:-7]    # takes the response object and strips everything except the profile count
            print(f"[*] Response received! New profile view count: {count}")

        response.raise_for_status()     # raises an Exception if an error occured

        print(f"[*] This run: {run} has finished!\n")

        # log the output from this run
        log = open(f"log_files\{current_date}_GITHUB_BOT_{run_id}.txt", 'a')
        log.write(f"[run:{run}] [new profile view count:{count}] [Start:{start_timestamp_str}] [max_loop:{max_loop}] [run_id:{run_id}]\n\n")
        log.close()

        time.sleep(random.uniform(4,7))     # this is to make the timing of the requests harder to predict (if the requests are made at regular intervals, it's obvious they're coming from a bot)


    except KeyboardInterrupt:       # press CTRL-C to exit while the bot is running
        print(f"[!] GH bot exited at run: {run}")
        break

    except HTTPError as http_err:   # logs any HTTP errors, then restarts the loop
        print(f'[!] HTTP error occurred: {http_err}')
        log = open(f"log_files\ERROR_LOG_GITHUB_BOT_{run_id}.txt", 'a')
        log.write(f"HTTP ERROR:[{http_err}] - run:{run} Start:[{start_timestamp_str}] max_loop:{max_loop} id:{run_id}\n\n")
        log.close()
        time.sleep(10)
        continue

    except Exception as err:        # logs any random errors, then restarts the loop
        print(f'[!] Other error occurred: {err}')
        log = open(f"log_files\ERROR_LOG_GITHUB_BOT_{run_id}.txt", 'a')
        log.write(f"OTHER ERROR:[{err}] - run:{run} Start:[{start_timestamp_str}] max_loop:{max_loop} id:{run_id}\n\n")
        log.close()
        time.sleep(10)
        continue