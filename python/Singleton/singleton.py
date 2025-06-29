from time import sleep

instance = None

class Singleton:
    def __init__(self):
        global instance
        instance = self
        self.name = "单例模式demo"
        self.message = ""

    def SayHello(self):
        print(f"Hello, my name is {self.name}")

    def SetMessage(self, message):
        self.message = message

    def GetMessage(self):
        print(self.message)


def getInstance():
    global instance
    if instance is None:
        instance = Singleton()
        return instance
    else:
        return instance