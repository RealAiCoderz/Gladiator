import datetime

f = open("log.txt", 'a', encoding="utf-8")

class Logger:

    #append time & error type in log.txt
    def make_entry(self, message):
        f.write("{} --- {}\n".format(datetime.datetime.now(), message))