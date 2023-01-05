#### Assignment Using If/Else Ladder ####

m,p,c = [int(x) for x in input("Enter The Marks of Maths,Physics,Chemistry:").split()]

average=(m+p+c)/3

if average >= 35:
    print("He/She is Passed")


# To Find Grade of a Student

if average <=59 and average >= 35:
    print("He/She is in Grade C")

elif average <= 69 and average >= 35:
    print("He/She is in Grade B")

elif average > 69 and average >= 35:
    print("He/She is in Grade A")

else:
    print("He/She Failed in one or more subject")



