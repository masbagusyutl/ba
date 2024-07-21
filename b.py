import requests
import time
from datetime import datetime, timedelta

# Load account IDs from data.txt
with open('data.txt', 'r') as file:
    accounts = file.readlines()

accounts = [account.strip() for account in accounts]
num_accounts = len(accounts)

# Function to claim reward for a given account
def claim_reward(telegram_uid):
    url = 'https://greedyball-api.artemislab.co/api/v1/claim'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8',
        'Cache-Control': 'no-cache',
        'Content-Length': '2',
        'Content-Type': 'application/json',
        'Origin': 'https://greedyball.artemislab.co',
        'Pragma': 'no-cache',
        'Referer': 'https://greedyball.artemislab.co/',
        'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Microsoft Edge";v="126", "Microsoft Edge WebView2";v="126"',
        'Sec-Ch-Ua-Mobile': '?0',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0',
        'X-Telegram-Uid': telegram_uid
    }

    response = requests.post(url, headers=headers, data='{}')
    return response.status_code == 201

# Display moving countdown timer
def countdown_timer(hours, message):
    end_time = datetime.now() + timedelta(hours=hours)
    while datetime.now() < end_time:
        remaining_time = end_time - datetime.now()
        print(f"\r{message}: {str(remaining_time).split('.')[0]}", end='')
        time.sleep(1)
    print()

# Main function to process all accounts
def main():
    for i, account_id in enumerate(accounts):
        print(f"Processing account {i + 1}/{num_accounts}: {account_id}")
        
        if claim_reward(account_id):
            print(f"Claim successful for account: {account_id}")
        else:
            print(f"Claim failed for account: {account_id}")
        
        time.sleep(5)
    
    print("All accounts processed. Starting 2-hour countdown.")
    countdown_timer(2, "Time remaining until next run")

# Run the main function and restart after 2 hours
while True:
    main()
