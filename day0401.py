import hashlib 

# initializing string 
str2hash = "GeeksforGeeks"
  
# encoding GeeksforGeeks using encode() 
# then sending to md5() 
result = hashlib.md5(str2hash.encode()) 

num = 1
while result.hexdigest()[0:6] != '000000':
    str2hash = "iwrupvqb" + str(num)
    result = hashlib.md5(str2hash.encode()) 

    # print(result.hexdigest()[0:5])

    num += 1


if result.hexdigest()[0:6] == '000000':
    print(num-1)

