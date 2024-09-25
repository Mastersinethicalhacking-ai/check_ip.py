#coded by ampachouri

#modules required
import argparse
import requests
import sys

#arguments and parser
parser = argparse.ArgumentParser()

parser.add_argument("-v", help="target/host IP address", type=str, dest='target', required=True)

args = parser.parse_args()

#colours used
red = '\033[31m'
yellow = '\033[93m'
lgreen = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'

#banner of script
print(red+"""
███╗   ███╗███████╗██╗  ██╗
████╗ ████║██╔════╝██║  ██║
██╔████╔██║█████╗  ███████║
██║╚██╔╝██║██╔══╝  ██╔══██║
██║ ╚═╝ ██║███████╗██║  ██║
╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
"""+red)
print(lgreen+bold+"         <===[[ meh ]]===> \n"+clear)
print(yellow+bold+"   <---(( search on youtube @mastersinetihcalhacking ))--> \n"+clear)

ip = args.target
api_url = f"https://ipinfo.io/{ip}/json"

try:
    # Step 1: Fetch the API data
    print(lgreen + "[$] Sending request to API...\n" + clear)
    response = requests.get(api_url, timeout=5)  # Timeout set to 5 seconds

    # Step 2: Check if the request was successful
    if response.status_code == 200:
        print(lgreen + "[$] API request successful.\n" + clear)
        data = response.json()  # Parse the JSON response

        # Step 3: Extract location data (Latitude and Longitude)
        loc = data.get('loc', 'N/A')
        if loc != 'N/A':
            latitude, longitude = loc.split(',')

        # Step 4: Display parsed data
        sys.stdout.flush()
        a = lgreen + bold + "[$]"
        b = cyan + bold + "[$]"
        print(a, "[Victim]:", data.get('ip', 'N/A'))
        print(red + "<--------------->" + red)
        print(b, "[ISP]:", data.get('org', 'N/A'))
        print(red + "<--------------->" + red)
        print(a, "[City]:", data.get('city', 'N/A'))
        print(red + "<--------------->" + red)
        print(b, "[Region]:", data.get('region', 'N/A'))
        print(red + "<--------------->" + red)
        print(a, "[Longitude]:", longitude)
        print(red + "<--------------->" + red)
        print(b, "[Latitude]:", latitude)
        print(red + "<--------------->" + red)
        print(a, "[Time zone]:", data.get('timezone', 'N/A'))
        print(red + "<--------------->" + red)
        print(a, "[Zip code]:", data.get('postal', 'N/A'))
        print(" " + yellow)

    else:
        print(red + f"[~] Error: Received status code {response.status_code} from API." + clear)
        print(yellow + f"Response Data: {response.text}" + clear)

except requests.exceptions.RequestException as e:
    # Handle network issues or API failures
    print(red + "[~] Error: " + str(e) + clear)

except KeyboardInterrupt:
    print('Terminating, Bye' + lgreen)
    sys.exit(0)

sys.exit(1)
