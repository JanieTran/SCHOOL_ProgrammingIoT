# Reference: https://www.tutorialspoint.com/python_design_patterns/python_design_patterns_singleton.htm
class Singleton:
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self


s = Singleton()
print(s)

s = Singleton.getInstance()
print(s)

s = Singleton.getInstance()
print(s)

s = Singleton()
print(s)
