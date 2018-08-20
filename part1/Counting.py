#!/usr/bin/env python
from collections import defaultdict
from urllib.parse import urlparse


def func(urls):
    fn_counters = defaultdict(lambda: 0)
    for url in urls:
        r = urlparse(url)
        fn = r.path.split('/')[-1]
        fn_counters[fn] += 1

    for k in sorted(fn_counters, key=fn_counters.get, reverse=True)[0:3]:
        print(k, fn_counters[k])


if __name__ == "__main__":
    # for test
    urls = [
        "http://www.google.com/a.txt",
        "http://www.google.com.tw/a.txt",
        "http://www.google.com/download/c.jpg",
        "http://www.google.co.jp/a.txt",
        "http://www.google.com/b.txt",
        "https://facebook.com/movie/b.txt",
        "http://yahoo.com/123/000/c.jpg",
        "http://gliacloud.com/haha.png",
    ]

    func(urls)
