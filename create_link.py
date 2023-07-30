import random


def create_link():
    link = ''.join([random.choice('1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm') for i in range(12)])
    while link in '':
        for i in range(12):
            i = random.choice('1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm')
            link += i
    return link