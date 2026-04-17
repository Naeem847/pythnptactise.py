# print("...print basic diseases expert system....")
# fever=input("doo you have any fever?").lower()
# cough=input("do you have cough?").lower()
# headache=input("do you have headche?").lower()
# if fever=="yes"and cough=="yes":
#     print("Diagnosis:flu")
# elif cough=="yes" and headache=="yes":
#     print("Diagnosis:Common Cold")
# else:
##########################################
#     print("no diseases match.")    
# print("final exam requirements")
# admit_card=input("do you have admit card?\n").lower()
# fee_slip=input("do you have feeslip?\n").lower()
# mis_id=input("do you have mis-is?\n").lower()
# if admit_card=="yes" and fee_slip =="yes" and mis_id=="yes":
#     print("yes you can sit in the exam hall")
# else:
#     print("Sorry !")

########################################
print("Advance disease Diagnosis system")
symtoms={
    "fever":input("doo you have fever?").lower(),
    "cough":input("do you have cough?").lower(),
    "rash":input("do you have rash?").lower(),
    "ranny_noise":input("do you have ranny_nise?").lower(),
}

#rules
if symtoms["fever"]=="yes" and symtoms["rash"]=="yes":
    print("pssible disease:Measles\n")

elif symtoms["cough"]== "yes" and symtoms["ranny_noise"]=="yes":
    print("possible diseases:flu\n")
else:
    print("you have no flu:")
#################################################
def disease_system():
 fever=input("fever?").lower()
 cough=input("cough?").lower()
 if fever=="yes"and cough=="yes":
  print("Diagnosis:flu")
 else:
  print("no match!")
def movie_system():
     while True:
        movie = input("Enter a movie name (or type 'exit' to stop): ").lower()

        if movie == "exit":
            print("Exiting movie system...")
            break

        if movie == "avengers":
            print("Genre: Action / Superhero")
        elif movie == "titanic":
            print("Genre: Romance / Drama")
        elif movie == "inception":
            print("Genre: Sci-Fi / Thriller")
        else:
            print("Movie not found!")
   
