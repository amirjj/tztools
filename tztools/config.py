import os.path


current_path = os.path.dirname(__file__)
ARCHIVE_PATH = os.path.join(current_path, 'archive', '')


APIS = {
    'all_tz': {
        'url': 'https://www.timeapi.io/api/TimeZone/AvailableTimeZones',
        'method': 'GET',
    },
}

RULES = {
    'archive': False,
}
