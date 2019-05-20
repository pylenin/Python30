import logging
import requests
import requests.exceptions

logging.basicConfig(filename="requests.log", format='%(name)s - %(asctime)s - %(message)s')

def main():
    try:
        requests.get("htt://www.0miles.com")
    except requests.exceptions.ConnectionError:
        logging.error("Could not find server. Check your network connection.")
    except requests.exceptions.InvalidSchema:
        logging.error("No connection adapters were found for your GET request")
    except Exception as x:
        logging.error("Oh that didn't work!: {}".format(x))


if __name__ == '__main__':
    main()
