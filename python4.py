name = input()
score = int(input())

for score in range(90,101):
    print("%s의 학점 : A" %name)
for score in range(80,90):
    print("%s의 학점 : B" %name)
for score in range(70,80):
    print("%s의 학점 : C" %name)
for score in range(60,70):
    print("%s의 학점 : D" %name)
for score in range(0,60):
    print("%s의 학점 : F" %name)