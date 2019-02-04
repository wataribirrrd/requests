import sys
import os
import requests

def main():
    param = sys.argv

    r = requests.get(param[1])
    print(r.status_code)


if __name__ == "__main__":
    main()