import requests
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("YOUR_NUMLOOKUP_API_KEY")

# User-defined parameters
target_name = "DESIRED_NAME"
input_file = "generated_numbers.txt"

def lookup_phone_number(phone_number):
    url = f'https://numlookupapi.com/api/v1/lookup?apikey={API_KEY}&number={phone_number}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        name = data.get('name', '').lower()
        if target_name.lower() in name:
            print(f"\n🎯 Found match: {target_name}")
            print(f"Phone Number: {phone_number}")
            print(f"Carrier: {data.get('carrier', 'Unknown')}")
            print(f"Location: {data.get('location', 'Unknown')}")
            return True
    else:
        print(f"Error {response.status_code} on number {phone_number}")
    return False


def find_target_number():
    with open(input_file, 'r') as file:
        for line in file:
            number = line.strip()
            if lookup_phone_number(number):
                break  # Stops after first match


# Runs the search
find_target_number()
