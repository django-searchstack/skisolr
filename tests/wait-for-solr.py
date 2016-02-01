#!/usr/bin/env python
# encoding: utf-8
"""Simple throttle to wait for Solr to start on busy test servers"""
from __future__ import absolute_import, division, print_function, unicode_literals

import sys
import time

import requests

if __name__ == '__main__':
    max_retries = 100
    retry_count = 0
    retry_delay = 15
    status_url = 'http://localhost:8983/solr/core0/admin/ping'

    while retry_count < max_retries:
        status_code = 0

        try:
            r = requests.get(status_url)
            status_code = r.status_code
            if status_code == 200:
                sys.exit(0)
        except Exception as exc:
            print('Unhandled exception requesting %s: %s' % (status_url, exc), file=sys.stderr)

        retry_count += 1

        print('Waiting {0} seconds for Solr to start (retry #{1}, status {2})'.format(
            retry_delay, retry_count, status_code), file=sys.stderr)
        time.sleep(retry_delay)

    print("Solr took too long to start (#%d retries)" % retry_count, file=sys.stderr)
    sys.exit(1)
