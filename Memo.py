class Memo():
    "备忘录基本信息"

    def __init__(self,id,date,name,thing):
        self.__id = id
        self.date = date
        self.name = name
        self.thing = thing


    @property
    def id(self):
        return self.__id

    @property
    def getDate(self):
        return self.date

    @property
    def getName(self):
        return self.name

    @property
    def getThing(self):
        return self.thing



