
# counting number of words in a string
string =input()
count=1
# printing original string
print ("The original string is : " + string)
length=len(string)
if string[0]==" ":
    count=count-1
for i in range(0,length):
    if string[i]==" " and string[i+1]!=" ":
        count=count+1
#printing the count
print ("The number of words in string are : " + str(count))