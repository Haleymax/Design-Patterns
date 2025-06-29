from Singleton.singleton import getInstance


if __name__ == '__main__':
    instance = getInstance()
    s1 = getInstance()
    s1.SayHello()
    s1.SetMessage("这个是s1实例设置的message")
    s2 = getInstance()
    s2.GetMessage()