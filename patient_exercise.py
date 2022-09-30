name=input("Enter name of patient\n")
age=input("Enter age of patient\n")
status_txt=input("enter status")
status=0
status=bool(status)

if status_txt=='new':
    status=True
    print("Patient is new")
else:
    status=False
    print("Patient exists")