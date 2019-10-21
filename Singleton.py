class Singleton:
    __instance = None
    class __impl:

        def spam(self):
            return id(self)


    def __init__(self):
        if Singleton.__instance is None:
            Singleton.__instance = Singleton.__impl()

        self.__dict__['_Singleton__instance'] = Singleton.__instance

    def __setattr__(self, key, value):
        return setattr(self.__instance, key, value)

    def __getattr__(self, item):
        return getattr(self.__instance, item)


s1 = Singleton()
s2 = Singleton()
print(id(s1), s1.spam())
print(id(s2), s2.spam())