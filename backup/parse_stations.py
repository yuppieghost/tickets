import requests
import re
from pprint import pprint

def main():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9055'
    r = requests.get(url)
    patter = u'([\u4e00-\u9fa5]+)\|([A-Z]+)'
    result = dict(re.findall(patter, r.text))
    print(result.keys())
    print(result.values())
if __name__ == '__main__':
    main()