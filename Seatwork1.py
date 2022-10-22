# Assignment 1:
# Create a program that will print your nickname using only asterisk character (*)
# Your program should be uploaded to github before 1:30 pm

# I will create a program that will print specific name and a name inputed by the user



def intro():
    print("\n\033[01m\033[93mThis first program will print my name 'Sean' only.\n\033[0m")
intro()

def myname():
    # S
    print_S = [[" " for i in range(7)] for j in range (7)]
    for row in range(7):
        for col in range(5):
            if ((row==0 or row==3 or row==6) and (col>0 and col<4)) or (col==0 and (row>0 and row<3)) or (col==4 and (row>3 and row<6)):
                print_S[row][col] = "*"

    # E
    print_E = [[" " for i in range(7)] for j in range (7)]
    for row in range(7):
        for col in range(5):
            if col==0 or ((row==0 or row==3 or row==6) and (col>0)):
                print_E[row][col] = "*"

    # A
    print_A = [[" " for i in range(7)] for j in range (7)]
    for row in range(7):
        for col in range(5):
            if((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
                print_A[row][col] = "*"

    # N
    print_N = [[" " for i in range(7)] for j in range (7)]
    for row in range(7):
        for col in range(7):
            if (col==0 or col==6) or (row==col and (col>0 and col<6)):
                print_N[row][col] = "*"
    # This will put all the patterns in a straight line horizontally
    for i in range(7):
        for j in range (7):
            print(print_S[i][j], end=" ")
        print(end=" ")
        for j in range (7):
            print(print_E[i][j], end=" ")
        print(end=" ")
        for j in range (7):
            print(print_A[i][j], end=" ")
        print(end=" ")
        for j in range (7):
            print(print_N[i][j], end=" ")
        print()

myname() 

