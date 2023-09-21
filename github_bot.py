import requests
import random
import time

from requests.exceptions import HTTPError
from datetime import datetime
from hidden import github_url

run_count = 0           # run_count starts at 0 and is incremented at the end of this loop
max_loop = 100            # how many times the bot will run
rand_run_id = random.choice(range(1,10000))     # used to identify a particular run in the log file. This ID is the same for all runs in one particular max_loop (ie this ID will be different each time this script runs overall, not each time the bot accesses the site)

try:
    while run_count <= max_loop:      
        # make a timestamp for this run, and print message
        start_now = datetime.now()
        start_timestamp_str = f'{start_now:%H.%M.%S_%m.%d.%Y}'
        current_date = f'{start_now:%m.%d.%Y}'
        print(f"[***] Starting new GH bot run at run_count:{run_count}, max_loop:{max_loop}, rand_run_id:{rand_run_id} [{start_timestamp_str}]")


        # Get the response object from the url that's requested, then sleep to finish loading
        response = requests.get(github_url)
        time.sleep(1)

        if response:    # response returns boolean when it's in a conditional statement
            print(f"[*] Response received successfully!")

        response.raise_for_status()     # raises an Exception if an error occured

        print(f"[*] This run: {run_count} has finished!\n")

        log = open(f"GITHUB_BOT_{current_date}_{rand_run_id}.txt", 'a')
        log.write(f"run_count:{run_count} Start:[{start_timestamp_str}] max_loop:{max_loop} id:{rand_run_id} RESPONSE_HEADER:{response.headers} RESPONSE_BODY:{response.text}\n\n")
        log.close()

        time.sleep(random.uniform(3,6))     # this is to make the timing of the requests harder to predict (if the requests are made at regular intervals, it's obvious they're coming from a bot)

        run_count += 1      # increment the run count

except KeyboardInterrupt:       # press CTRL-C to exit while the bot is running
    print(f"[!] GH bot exited at run_count: {run_count}")

except HTTPError as http_err:   # logs any HTTP errors
    print(f'[!] HTTP error occurred: {http_err}')
    log = open(f"ERROR_LOG_GITHUB_BOT_{rand_run_id}.txt", 'a')
    log.write(f"HTTP ERROR:[{http_err}] - run_count:{run_count} Start:[{start_timestamp_str}] max_loop:{max_loop} id:{rand_run_id}\n\n")
    log.close()

except Exception as err:        # logs any random errors
    print(f'[!] Other error occurred: {err}')
    log = open(f"ERROR_LOG_GITHUB_BOT_{rand_run_id}.txt", 'a')
    log.write(f"OTHER ERROR:[{err}] - run_count:{run_count} Start:[{start_timestamp_str}] max_loop:{max_loop} id:{rand_run_id}\n\n")
    log.close()