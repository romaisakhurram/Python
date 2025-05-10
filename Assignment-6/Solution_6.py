
class Logger:
    def __init__(self):
        print("logger object created")

    def __del__(self):
        print("logger object destroyed")

log = Logger()
del log