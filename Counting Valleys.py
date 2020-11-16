#functions
def split(word):
    return [char for char in word]

#Variables
VoM = {"D":-1,"U":1}
count = 0
height = 0
lastInt = 0
valleyCount = 0

#inputs
length = int(input())
lst = split(input())


while count < length - 1:
    currentInt = VoM[lst[count]]
    
    #overall heigh
    height += currentInt

    if currentInt < 0 and lastInt == currentInt:
        #setting marker
        valleyCount +=1
    count += 1
    lastInt = lst[count]

print(valleyCount)