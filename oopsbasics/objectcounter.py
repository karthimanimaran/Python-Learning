class ObjectCounter:

    numberofObjects = 0

    def __init__(self):
        ObjectCounter.numberofObjects+=1

    @staticmethod
    def displayCount():
        print(ObjectCounter.numberofObjects)

o1 = ObjectCounter()
o2 = ObjectCounter()

ObjectCounter.displayCount()