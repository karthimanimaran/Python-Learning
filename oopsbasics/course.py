class Course:

    def __init__(self,name,ratings):
        self.name = name
        self.ratings = ratings

    
    def average(self):
        numberofRatings = len(self.ratings)
        average = sum(self.ratings)/numberofRatings
        print('Avearage Ratings For ',self.name,' Is ',average)


c1 = Course('Java Course',[1,2,3,4,5])
print(c1.name)
print(c1.ratings)
c1.average()

c2 = Course('Java Web Services',[1,2,3,4,5])
print(c2.name)
print(c2.ratings)
c2.average()