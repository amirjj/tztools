from tztools.config import APIS, ARCHIVE_PATH, RULES
from datetime import datetime
import requests
import json
import os


def archive_results(result, api_name):
    if RULES['archive']:
        filename_name = ARCHIVE_PATH + \
            api_name + '_' + datetime.now().strftime("%y%m%d%H%M%S") + '.json'

        with open(filename_name, "w") as f:
            f.write(json.dumps(result))


def get_all_timezones():
    url = APIS['all_tz']['url']
    method = APIS['all_tz']['method']
    res = requests.get(url)
    if res.status_code == 200:
        return json.loads(res.text), 'all_tz'
    return None
