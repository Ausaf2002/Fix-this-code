import time
Animal = input("Type your Animal: ")

if("Cat" or "Dog"):
   print("Processing answer....\n")
   time.sleep(1) 
   print("Your animal has for legs")
   if(Animal == "Dog"):
        print("and it is a Dog!")
   if(Animal == "Cat"):
        print(" and it is a Cat")

elif("Giraffe" or "Elephant"):
    print("Processing answer....\n")
    time.sleep(1) 
    print("Your animal is Huge")
    if(Animal == "Giraffe"):
        print("Giraffes have tall necks!")
    if(Animal == "Elephant"):
        print("Elephants are strong and bulky!")

elif("Tiger" or "Lion"):
    print("Processing answer....\n")
    time.sleep(1) 
    print("You have chosen a Carnivorous cat!")

else:
    print("Processing answer....\n")
    time.sleep(1)
    print("Animal not found in the data base")

    
