import argparse
import sys
import subprocess

_tests = {
    'find_link': ['url', 'link'],
    'find_forms': ['url'],
    'xss_vulnerability_scanner': ['url'],
    'sql_injection_scanner': ['url'],
    'doctype_check': ['url'],
    'page_load_speed': ['url'],
    'check_link': ['url', '[links]'],
    'js_errors_check': ['url']
}


class Test(object):

    def __init__(self, test_name, args=None):
        self.test_name = test_name
        self.args = args

    def run_test(self):
        proc = subprocess.Popen(['python', f'tests/{self.test_name}.py'] + self.args, stdout=subprocess.PIPE,
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
    usage: site_testing.py <test_name> [args]
    test_name - name of the testing
    args - tests args
    """
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('-h', '--help', action='store_true')
    parser.add_argument('-tests', action='store_true')
    parser.add_argument('test_name', nargs='?')
    parser.add_argument('args', nargs='*')
    parser.usage = use_as_os_command.__doc__
    args = parser.parse_args()
    if args.help:
        if args.test_name:
            if not args.test_name in _tests:
                print('\nthis test doesnt exist\n')
                print('usage: ' + use_as_os_command.__doc__)
                sys.exit(3)
            else:
                test = Test(args.test_name, ["-h"])
                sys.exit(test.run_test())
        else:
            print('usage: ' + use_as_os_command.__doc__)
            sys.exit(0)
    if args.tests:
        print('\ntests: \n')
        for test, descr in _tests.items():
            print(test, descr)
        print("\ninput <test_name> -help to get test information")
        sys.exit(0)
    if not args.test_name in _tests:
        print('\nthis test doesnt exist\n')
        print('usage: ' + use_as_os_command.__doc__)
        sys.exit(3)

    test = Test(args.test_name, args.args)
    sys.exit(test.run_test())


if __name__ == '__main__':
    use_as_os_command()
