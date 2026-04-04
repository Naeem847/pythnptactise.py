def demo():
    for i in range(5):
        x=i*10
        print(x)
demo()
# create the code with local variable inside the for loop and also use the condition while loop
for i in range(3):
    while j<2:
        print("f:",i ,"j:",j)
        j+=1
# create guessing the number game
secret_number=7
while True:
  print("\n you have 3 chance to guess the number")
  for i in range(3):
    guess=int(input("enter your guess number:"))
    if guess==secret_number:
      print("correct you win!")
      break
    else:
      print("wrong guess try again")
  else:
     print("you lost the secret_number",secret_number) 
  play_again=input("play again? (yes/no):")
  if play_again!="yes":
        print("thanks for playing!")
        break 

      

        