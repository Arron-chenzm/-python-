class test_res:
    def __init__(self):
        self.__times = None
        self.__see = None
        self.__thing = None

    def set_times(self, num):
        self.__times = num

    def set_see(self, res2see):
        self.__see = res2see

    def set_thing(self, thing):
        self.__thing = thing

    def get_times(self):
        return self.__times

    def get_see(self):
        return self.__see

    def get_thing(self):
        return self.__thing

    def printres(self):
        print("次数:{} 是否看到:{} 刺激物:{}".format(self.__times, self.get_see(), self.get_thing()))

    def res2str(self):
        str = "次数:{} 是否看到:{} 刺激物:{}".format(self.__times, self.get_see(), self.get_thing())
        return str