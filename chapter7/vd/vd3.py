str=(input()).lower()
ch=(input()).lower()
dem=0
for char in str:
    if ch==char:
        dem=dem+1

print("Number of character",ch,"is:",dem)