import re
import sys
import urllib.error
from urllib.request import Request, urlopen
from urllib.parse import urlencode


def main():
    if len(sys.argv) < 2:
        print("Not enough argument")
        sys.exit()

    find_this = re.compile(r'<span>(.*)</span>')

    card_number = {"recharge": sys.argv[1]}
    card_number_encoded = urlencode(card_number).encode('utf-8')
    site_request = Request("http://123.orange.mg/Recharge/CarteAGratter",
                            data=card_number_encoded,
                            method="post")
    site_request.add_header('User-Agent',
                            'Mozilla/5.0 (X11; Linux x86_64; rv:24.0) Gecko/20140722 Firefox/24.0 Iceweasel/24.7.0')

    try:
        response = urlopen(site_request)
        result = find_this.findall(response.read().decode('utf-8'))
        print(result[1])
    except urllib.error.HTTPError as e:
        print('status', e.code)
        print('reason', e.reason)
        print('url', e.url)


if __name__ == "__main__":
    main()
