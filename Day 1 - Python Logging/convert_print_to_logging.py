"""
Use logging in this example to print messages
to a file called 'requests.log' in the
following format

> 2019-03-03 17:18:32,703 :: INFO :: Root :: Line No 1 :: This is the logging message!
"""

import requests
import requests.exceptions

def main():
    try:
        requests.get("htt://www.0miles.com")
    except requests.exceptions.ConnectionError:
        print("Could not find server. Check your network connection.")
    except ValueError:
        print("No connection adapters were found for your GET request")
    except Exception as x:
        print("Oh that didn't work!: {}".format(x))


if __name__ == '__main__':
    main()
