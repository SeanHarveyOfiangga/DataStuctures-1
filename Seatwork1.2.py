def intro_2():
    print("\n\033[01m\033[93mThe second program will print according to the user's input.\n\033[0m")

intro_2()

def alphabets():
    for i in range(len(name)):
        # A
        if name[i]=="A":
            print_A = [[" " for i in range (8)] for j in range(8)]
            for row in range(7):
                for col in range(5):
                    if ((col==0 or col==4) and row!=0) or ((row==0 or row==3) and (col>0 and col<4)):
                        print_A[row][col] = "*"
            list2.append(print_A)
        
        # B 
        elif name[i]=="B":
            print_B = [[" " for i in range (8)] for j in range(8)]
            for row in range(7):
                for col in range(5):
                    if (col==0) or (col==4 and (row!=0 and row!=3 and row!=6)) or ((row==0 or row==3 or row==6) and (col>0 and col<4)):
                        print_B[row][col] = "*"
            list2.append(print_B)

        # C
        elif name[i]=="C":
            print_C = [[" " for i in range (8)] for j in range(8)]
            for row in range(7):
                for col in range(5):
                    if (col==0) or ((row==0 or row==6) and (col>0)):
                        print_C[row][col] = "*"
            list2.append(print_C)

        # D
        elif name[i]=="D":
            print_D = [[" " for i in range (8)] for j in range(8)]
            for row in range(7):
                for col in range(5):
                    if (row!=0 and row!= 6 and(col==0 or col==4 )) or ((row==0 or row==6) and (col<4)):
                        print_D[row][col] = "*"
            list2.append(print_D)  

        # E
        elif name[i]=="E":
            print_E = [[" " for i in range (8)] for j in range(8)]
            for row in range(7):
                for col in range(5):
                    if col==0 or ((row==0 or row==3 or row==6) and (col>0)):
                        print_E[row][col] = "*"
            list2.append(print_E) 
        
  

        else:
            print("INVALID")
    return list2


# This will collect and store all informations from the user
name = input("\033[32mEnter your name: \033[0m").upper()
list2 = []
list3 = alphabets()

#This will arrange and print the collected pattern
for i in range(8):
    for j in range(len(list3)):
        for k in range(8):
            print(list3[j][i][k], end=" ")
        print(end="")
    print()

def outro():
    print("\n\033[96m\033[01mThank you for using my program ^^\033[0m")
outro()