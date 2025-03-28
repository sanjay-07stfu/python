
print("\t************************************  WELCOME TO TREAASURE ISLAND  ******************************************")
print("YOU ARE STANDINGG AT THE ENTRANCE OF THE ISLAND.")
print("WHERE YOU WANT TO GO???")
print("1: GO TO THE DENSE JUNGLE\n2: WALK TO ALONG THE BEACH")
print("ENTER YOUR CHOICE BETWEEN THE 1 OR 2:")
choice=int(input("enter your choice"))

if (choice==1):
    print("YOU ENTERED THE DENSE JUNGLE.")
    print(" WHERE YOU WANT TO GO NOW ???")
    print("3: CLIMB THE TREE TO LOOK AROUND.\n 4: FOLLOW A NARROW PATH DEEPER INTO THE JUNGLE.")
    print("ENTER YOUR CHOICE BETWEEN THE 3 OR 4:")
    ch=int(input("Enter your choice:"))
    if (ch==3):
        print(" CONGRATULATIONS YOU FOUND THE TRESURE.")
    elif (ch==4):
        print("YOU REACHED THE NARROW PATH DEEPER INTO THE JUNGLE.")
        print("WHERE YOU WANT TO GO NOW???")
        print("5:CROSS AN OLD WOODEN BRIDGE.\n6:ENTER THE DARK CAVE.")
        print("ENTER YOUR CHOICE BETWEEN THE 5 OR 6:")
        choice=int(input("ENETR YOUR CHOICE:"))
        if (choice==5):
            print("CONGRATULATIONS YOU FOUND THE TRESURE.")
        elif (choice==6):
            print("PLEASE GO BACK TO PREVIOUS PATH.")

elif (choice==2):
    print("NOW YOU ON THE BEACH.")
    print("DO YOU WANT TO GO ANOTHER LOCATION??")
    print("9:yes OR 10:no")
    choice=int(input("ENTER YOUR CHOICE:"))
    if (choice==9):
        print("WHERE YOU WANT TO GO??")
        print("7:TEMPLE \n8:REVER")
        choice=int(input("ENTER YOUR CHOICE:"))
        if (choice==7):
            print("CONGRATULATIONS YOU REACHED THE TEMPLE.")
        elif (choice==8):
            print("CONGRATULATIONS YOU REACHED THE REVER.")

    elif (choice==10):
            print("THANK YOU FOR THE VISIT.")

else:
    print("PLEASE ENTER A VALID CHOICE.")


    


 
   