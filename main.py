name: str = input("Hey type your name : ")
print("Hello",name,"welcome to my game ")

should_we_play = input("Do you want to play?").lower()

if should_we_play == "y" or should_we_play == "yes":
     print("we are gonna play !")
     weapon = input("Choose an weapon(sword/axe):").lower()

     direction = input("do you want to go left or right ?(left/right)").lower()
     if direction == "left":
        print("You went left and fell off a cliff,game over,try again")
     elif direction == "right":
        choice = input("okay now see a bridge, do you want to swim under it or cross it ?")
        if choice == "swim" and weapon == "axe" :
           print("you survived the  aligator")
        else:
           print("You found the hidden treasure and won ")   


        print("okay we went left ")
     elif direction == "right":
        print("we went right ")   
     else :
      print("Sorry not a valid reply,you die!")

else:
     print("we are not playing") 
   

