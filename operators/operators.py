# Height = 5.7
# Weight = 82

# # bmi = (Weight in kg/height in meters)

# heightInMeters = Height*0.4536

# bmi=Weight/(heightInMeters*heightInMeters)

# print('BMI:',bmi)

def calculateBMI(height,weight):
    heightInMeters = height*0.4536

    bmi=weight/(heightInMeters*heightInMeters)
    return bmi

print(calculateBMI(5.8,70))
print(calculateBMI(6.8,100))
print(calculateBMI(5.6,70))
print(calculateBMI(5.2,50))

    