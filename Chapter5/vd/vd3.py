#truy xuất tập con trong List
spam=['cat', 'bat', 'rat', 'elephant']
spam[0:4]
print(spam[0:4])
spam[1:3]
print(spam[1:3])
spam[0:-1]
print(spam[0:-1])




#truy xuất tập con trong List
spam=['cat', 'bat', 'rat', 'elephant']
spam[:2]
print(spam[:2])
spam[1:]
print(spam[1:])
spam[:]
print(spam[:])




#truy xuất tập con trong List
spam=[1,2,3,4,5,6]
spam[2]
print(spam[2])
spam[1:4]
print(spam[1:4])
spam[2:5]
print(spam[2:5])
spam[0:3]
print(spam[0:3])




#sử dụng phép gán và số Index
spam=['cat', 'bat', 'rat', 'elephant']
spam[1]='aardark'
spam[2]=spam[1]
spam[-1]=12345
print(spam)