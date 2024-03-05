import datetime

f = open("log.txt", 'a', encoding="utf-8")

#append time & error type in log.txt
def make_entry(message):
    f.write("{} --- {}\n".format(datetime.datetime.now(), message))