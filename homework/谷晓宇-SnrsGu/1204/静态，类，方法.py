class A:
    def __init__(self):
        self.name = "name"

    @staticmethod
    def getData():
        A.name = 'static'
        print('我是一个静态方法')

    @classmethod
    def getClassData(self):
        #A.name = 'calss'
        print(self.name)
        print("我是一个类方法")

#x = A() 
#y = x.getData()
#print(A.name)

#A.getData()
#print(A.name)


A.getClassData()
