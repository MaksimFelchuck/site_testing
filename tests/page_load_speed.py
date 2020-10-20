"""
page_load_speed - function to check site load speed:

Usage: page_load_speed <url>

    <url> - url where checking load speed
"""
import sys
import time

from selenium import webdriver


def page_load_time(link):
    driver = webdriver.Chrome()
    driver.get(link)

    navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
    responseStart = driver.execute_script("return window.performance.timing.responseStart")
    time.sleep(5)
    domComplete = driver.execute_script("return window.performance.timing.domComplete")
    backendPerformance_calc = responseStart - navigationStart
    frontendPerformance_calc = domComplete - responseStart
    driver.quit()
    return backendPerformance_calc, frontendPerformance_calc


def main():
    if sys.argv[1] == '-h' or '--help':
        print(__doc__)
        sys.exit(0)
    backendPerformance_calc, frontendPerformance_calc = page_load_time(sys.argv[1])
    print(f"Back End: {backendPerformance_calc}ms")
    print(f"Front End: {frontendPerformance_calc}ms")


if __name__ == '__main__':
    main()
