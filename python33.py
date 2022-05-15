name = input()
score = int(input())

if range(90,101):
    print("%s의 학점 : A" %name)
elif range(80,90):
    print("%s의 학점 : B" %name)
elif range(70,80):
    print("%s의 학점 : C" %name)
elif range(60,70):
    print("%s의 학점 : D" %name)
else:
    print("%s의 학점 : F" %name)