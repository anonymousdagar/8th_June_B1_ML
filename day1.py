#Question 1v-----------------------------------------------
print(5**9)
print(3//2)
print(7//2)
print(7/2)
print(6 == 6)

a = 20
a+= 30
print(a)
print(True*False)
print(True&False)
print(((6>3) and (7<4) or (18 == 3)) and (9>3))
print(True is False)
print(False is False)
print(((True == False) or (False > True)) and (False <= True))
# question 3--------------------------------------------
s1 = "Nice to have it"
s2 = "here"
print(s1,s2)

# ques 4-------------------------------------------------
a = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(a[3][1][2][0])

#ques 5 -----------------------------------------------
a=[s1]+a +[s2]
print(a)

# #Question 6---------------------------------------
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(color_list_1.difference(color_list_2))
# #ques 7 ----------------------------------------------
str = input("Enter the string :")
alphabet = "abcdefghijklmnopqrstuvwxyz"
pangram = True
for char in alphabet:
    if char in str.lower():
        pangram = True

    else:
         pangram=False
if pangram == True:
    print("its a panagram")
else:
    print("not a panagram")
#
#ques 8 -------------------------------------------------
a= input("Enter the integer n : ")
print((eval("{0}+{0}{0}+{0}{0}{0}".format(a))))
#ques 9 --------------------------------------------------
a = "without,world,hello,bag"
list = a.split(",")
list.sort()
print(list)
#ques 10 ------------------------------------------
d = {'Student': ['Rahul', 'Kishore', 'Vidhya', 'Raakhi'],'Marks': [57,87,67,79]}
print(d['Student'][d['Marks'].index(max(d['Marks']))])

