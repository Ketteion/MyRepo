import hashlib
import string
import itertools

with open ("hash.txt","r") as fShadow:
    with open("pass_list","r") as fPass_list:
        for line in fShadow:
            for passwd in fPass_list:
                hashed = hashlib.md5(passwd[:-1].encode("UTF-8")).hexdigest()
                if line[:-1] == hashed:
                    print(f"\n\nCRACKED\n\n{hashed}    {passwd}\n\nThe password is {passwd}.")
                    quit()

with open ("hash.txt","r") as fShadow:
    for line in fShadow:
        for x in range(1,25):
            result = itertools.product(string.printable[:-6],repeat=x)
            for i in result:
                #print("".join(i))
                hashed = hashlib.md5("".join(i).encode("UTF-8")).hexdigest()
                print(f"{hashed}    {''.join(i)}")
                if hashed == line[:-1]:
                    print(f"\n\nCRACKED\n\n{hashed}    {i}\n\nThe password is {i}")
                    quit()
