# for loop
numbers=[1,2,3,4,5]
for num in numbers:
    print(num)
count=0
# while loop
while count<5:
    print("count is:",count)
    count+=1
# break and continue statement in for loop
for num in range(10):
    if num==3:
     print("skipping num 3")
     continue
    elif num==8:
       print("iteration break at num 8")
       break
    else:
       print(num)
#mix while loop and for loop
num=1
while num<4:
    print("while loop iteration",num)
    for number in range(1,5):
        print("for loop iteration is:",number)
    num+=1       
