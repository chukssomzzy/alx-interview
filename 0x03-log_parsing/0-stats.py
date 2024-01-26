#!/usr/bin/python3
"""Parse logs"""
import re
import sys
from operator import itemgetter


def parse_stdin():
    """Parse logs from stdin"""
    no_line = 0
    file_size = 0
    line = sys.stdin.readline()
    status = {}
    try:
        while line:
            no_line += 1
            match = p.match(line)
            if match and no_line == 10:
                no_line = 0
                file_size += int(match.group("file_size"))
                key = str(match.group("status_code"))
                if key in status:
                    status[key] += 1
                else:
                    status[key] = 1
                print("File size: {:d}".format(file_size))
                for key, val in sorted(status.items(), key=itemgetter(0)):
                    print("{}: {:d}".format(key, val))
            elif match:
                file_size += int(match.group("file_size"))
                key = str(match.group("status_code"))
                if key in status:
                    status[key] += 1
                else:
                    status[key] = 1
            else:
                no_line += 1
            line = sys.stdin.readline()
    except KeyboardInterrupt:
        print("File size: {}".format(file_size))
        for key, val in sorted(status.items(), key=itemgetter(0)):
            print("{}: {:d}".format(key, val))
        raise


if __name__ == "__main__":
    p = re.compile(r'''
                   ^\b(?:(?:2(?:[0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9])\.){3}
                   (?:(?:2([0-4][0-9]|5[0-5])|[0-1]?[0-9]?[0-9]))\b\s-\s
                   \[[0-9]{4}-[0-9]{2}-[0-9]{2}\s([0-9]{2}(:[0-9]{2}){2})\.
                     [0-9]{6}\]
                   \s"[A-Za-z]+\s/[A-Za-z]+/260\s[A-Za-z]+/[0-9]*\.[0-9]+"
                   \s(?P<status_code>(?:405|200|301|400|403|404|500|401))\s
                   (?P<file_size>[0-9]{1,4})$
                   ''', re.VERBOSE)
    parse_stdin()
