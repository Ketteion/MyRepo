def is_num():
    while True:
        #this is local space
        try:
            num = int(input("Give me a number: "))
            break
        except ValueError:
            print("This is not a number.")
            continue
    return num

#this is global space

#x = is_num()
#y = is_num()
#z = is_num()
#print(x, y, z)

my_list = []
my_list.append(is_num())
my_list.append(is_num())
my_list.append(is_num())
my_list.append(4)
my_list.append(5)
my_list.append(6)
my_list.append(7)
print(my_list[-1])

#length = len(my_list)
#count = 0
#while count < length:
#    print(my_list[count])
#    count+=1

for i in my_list:
    print(i)
    