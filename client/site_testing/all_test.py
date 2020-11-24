"""
all_test.py - function for all tests with a specific url
usage: all_test.py <url>
url - site's url
"""
import argparse
import subprocess
import sys

_tests = [
    "doctype_check", "find_forms",
    "js_errors_check", "page_load_speed",
    "sql_injection_scanner", "xss_vulnerability_scanner"
]


def run_tests(url, test_name):
    """
    function to run tests
    """
    proc = subprocess.Popen(['python3', f'tests/{test_name}.py', url], stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
    stdout, stderr = proc.communicate()
    stdout = stdout.decode('latin-1')
    stderr = stderr.decode('utf-8')
    status = proc.poll()
    if stderr:
        print(stderr)
    elif stdout:
        print(stdout)
    return status


def use_as_os_command():
    """
    usage: all_test.py <url>
    url - site's url
    """
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-h', '--help', action='store_true')
    parser.add_argument('url', nargs='?')
    parser.usage = use_as_os_command.__doc__
    args = parser.parse_args()
    if args.help:
        print('usage: ' + use_as_os_command.__doc__)
        sys.exit(0)
    status = 0
    for test in _tests:
        print("----------------")
        process = run_tests(args.url, test)
        if process != 0:
            print(f"{test} passed with error")
            status = 3
    print("----------------")
    if status == 3:
        print("Some tests passed with an error")
        sys.exit(3)
    else:
        print("All tests passed successful")
        sys.exit(0)


if __name__ == '__main__':
    use_as_os_command()
