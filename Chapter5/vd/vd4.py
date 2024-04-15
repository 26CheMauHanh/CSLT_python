#toán tử:+
n=[1,2]
print(n)
n=n+[3,4]
print(n)
n=n+n
print(n)



#toán tử: nhân 
n=[1,2]
print(n)
n=n*2
print(n)
n=n+n
print(n)




#toán tử "in" và "not"
myPets=['Zophie','Pooka','Fat-tail']
print('Enter a pet name:')
name=input()
if name not in myPets:
    print('I do not have a pet named'+name)
else:
    print(name+'is my pet.')