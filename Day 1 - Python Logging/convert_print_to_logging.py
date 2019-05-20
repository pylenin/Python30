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
