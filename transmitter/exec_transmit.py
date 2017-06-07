#!/usr/bin/env python
import cgi

# import cgitb; cgitb.enable()  # for troubleshooting

print "Content-type: text/html"
print

import os
import os.path


def get_sorted_file_list(path):
    list = os.listdir(path)
    csv_list = []

    for file in list:
        if file.endswith('.csv'):
            csv_list.append(file)

    csv_list = sorted(csv_list)
    return csv_list


def do_test():
    while True:
        print "hello"
