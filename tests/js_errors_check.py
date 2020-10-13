import sys
from selenium import webdriver
import logging

from selenium.common.exceptions import WebDriverException


def check_browser_errors(driver):
    try:
        browser_logs = driver.get_log('browser')
    except (ValueError, WebDriverException) as e:
        logging.debug("Could not get browser logs for driver %s due to exception: %s",
                      driver, e)

        return []

    errors = []
    for entry in browser_logs:
        if entry['level'] == 'SEVERE':
            errors.append(entry)
    return errors


def main():
    driver = webdriver.Chrome()
    driver.get(sys.argv[1])
    errors = check_browser_errors(driver)
    if len(errors) > 0:
        print(*errors, sep='\n')
    else:
        print('No js errors')


if __name__ == '__main__':
    main()
