while True:
    print('Enter your age:')
    age=input()
    if age.isalnum():
        break
    print('Please enter a number for your age.')