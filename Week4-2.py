s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]

name = input("Enter student\'s name: " )
if name == "Ahmad":
    s1.remove("Ahmad")
    print(name, sum(s1))
elif name == "Sami":
    s2.remove("Sami")
    print(name, sum(s2))
elif name == "Faris":
    s3.remove("Faris")
    print(name, sum(s3))
else:
    print("Student is not recorded",0)
