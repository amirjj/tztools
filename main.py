from tztools.timeapi import get_all_timezones, archive_results


if __name__ == "__main__":
    api_result, api_name = get_all_timezones()
    archive_results(api_result, api_name)





