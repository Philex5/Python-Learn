try:
    file=open('sdjfkls.txt','r+')
except Exception as e:
    print("not find file")
    response=input('Do you want to create a new file')
    if(response=='y'):
        file=open('sdjfkls.txt','w')
    else:
        pass
else:
    file.write('sssssssssssss')

file.close()
