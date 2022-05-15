hurdle=0
for hurdle in range(0,5):
    hurdle = hurdle+1
    print("허들을 넘었습니다.")
print("레이스를 완주했습니다.")


hurdle=5
while hurdle < 5:
    hurdle = hurdle-1
    print("허들이 %d개 남았습니다.", hurdle)
    if hurdle == 0:
       print("레이스를 완주했습니다.")


name = input()
score = int(input())

if range(90,101):
    print("%d의 학점 : A")
elif range(80,90):
    print("%d의 학점 : B")
elif range(70,80):
    print("%d의 학점 : C")
else:
    print("%d의 학점 : F")



name = input()
score = int(input())

for score in range(90,101):
    print("%d의 학점 : A")
for score in range(80,90):
    print("%d의 학점 : B")
for score in range(70,80):
    print("%d의 학점 : C")
for score in range(60,70):
    print("%d의 학점 : D")
for score in range(0,60):
    print("%d의 학점 : F")