import re


def domain_name(url):
    if "://" and "www" in url:
        print(url)
        text = url.split('//')
        text1 = text[1].split('.')
        return text1[1]
    elif "//" in url:
        text = url.split('//')
        text1 = text[1].split('.')
        return text1[0]
    elif "www" in url:
        text = url.split('www.')
        text1 = text[1].split('.')
        return text1[0]
    else:
        text = url.split('.')
        return text[0]

# This one the code above it always fails in www.xakep.ru, only that one it passed the random test and all, but I don't know what is happening it somehow returns true for the first condition.


def domain_name(url):
    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')
