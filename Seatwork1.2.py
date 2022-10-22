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
        
        # F
        elif name[i]=="F":
            print_F = [[" " for i in range (8)] for j in range(8)]
            for row in range(7):
                for col in range(5):
                    if col==0 or ((row==0 or row==3) and (col>0)):
                        print_F[row][col] = "*"
            list2.append(print_F) 
        
        # G 
        elif name[i]=="G":
            print_G = [[" " for i in range (8)] for j in range(8)]
            for row in range(7):
                for col in range(5):
                    if col==0 or (col==4 and (row!=1 and row!=2)) or ((row==0 or row==6) and (col>0 and col<4)) or (row==3 and (col==3 or col==5)):
                        print_G[row][col] = "*"
            list2.append(print_G)
        
        # H 
        elif name[i]=="H":
            print_H = [[" " for i in range (8)] for j in range(8)]
            for row in range(7):
                for col in range(5):
                    if col==0 or col==4 or (row==3 and (col>0 and col<4)):
                        print_H[row][col] = "*"
            list2.append(print_H)

        # I
        elif name[i]=="I":
            print_I = [[" " for i in range (8)] for j in range(8)]
            for row in range(7):
                for col in range(5):
                    if col==2 or ((row==0 or row==6) and col!=2):
                        print_I[row][col] = "*"
            list2.append(print_I)

        # J
        elif name[i]=="J":
            print_J = [[" " for i in range (8)] for j in range(8)]
            for row in range(7):
                for col in range(5):
                    if col==2 or (row==0 and col!=2) or (row==6 and col<2):
                        print_J[row][col] = "*"
            list2.append(print_J)

        # K 
        elif name[i]=="K":
            i=0
            j=4
            print_K = [[" " for i in range (8)] for j in range(8)]
            for row in range(7):
                for col in range(5):
                    if col==0 or (row==col+2 and col>1):
                        print_K[row][col] = "*"
                    elif ((row==i and col==j) and col>0):
                        print_K[row][col] = "*"
                        i=i+1
                        j=j-1
            list2.append(print_K)

        # L 
        elif name[i]=="L":
            print_L = [[" " for i in range (8)] for j in range(8)]
            for row in range(7):
                for col in range(5):
                    if col==0 or (row==6 and col>0):
                        print_L[row][col] = "*"
            list2.append(print_L)

        # M
        elif name[i]=="M":
            print_M = [[" " for i in range (8)] for j in range(8)]
            for row in range(7):
                for col in range(7):
                    if col==0 or col==6 or ((row==col) and (col>0 and col<4)) or (row==1 and col==5) or (row==2 and col==4):
                        print_M[row][col] = "*"
            list2.append(print_M) 

        # N 
        elif name[i]=="N":
            print_N = [[" " for i in range (8)] for j in range(8)]
            for row in range(7):
                for col in range(7):
                    if (col==0 or col==6) or (row==col and (col>0 and col<6)):
                        print_N[row][col] = "*"
            list2.append(print_N)

        # O 
        elif name[i]=="O":
            print_O = [[" " for i in range (8)] for j in range(8)]
            for row in range(7):
                for col in range(5):
                    if (row!=0 and row!= 6 and (col==0 or col==4 )) or ((row==0 or row==6) and (col>0 and col<4)):
                        print_O[row][col] = "*"
            list2.append(print_O)

        # P 
        elif name[i]=="P":
            print_P = [[" " for i in range (8)] for j in range(8)]
            for row in range(7):
                for col in range(5):
                    if col==0 or (col==4 and (row==1 or row==2)) or((row==0 or row==3)and ( col>0 and col<4)):
                        print_P[row][col] = "*"
            list2.append(print_P)

        # Q
        elif name[i]=="Q":
            print_Q = [[" " for i in range (8)] for j in range(8)]
            for row in range(8):
                for col in range(5):
                    if ((col==0 or col==4) and (row>0 and row<6)) or ((row==0 or row==6) and (col>0 and col<4)) or (row==5 and col==1) or (row==7 and col==3):
                        print_Q[row][col] = "*"
            list2.append(print_Q)

        # R
        elif name[i]=="R":
            print_R = [[" " for i in range (8)] for j in range(8)]
            for row in range(7):
                for col in range(5):
                    if col==0 or (col==4 and (row==1 or row==2)) or((row==0 or row==3) or (row-col==3)and ( col>0 and col<4)):
                        print_R[row][col] = "*"
            list2.append(print_R)

        # S
        elif name[i]=="S":
            print_S = [[" " for i in range (8)] for j in range(8)]
            for row in range(7):
                for col in range(5):
                    if ((row==0 or row==3 or row==6) and (col>0 and col<4)) or (col==0 and (row>0 and row<3)) or (col==4 and (row>3 and row<6)):
                        print_S[row][col] = "*"
            list2.append(print_S)

        # T
        elif name[i]=="T":
            print_T = [[" " for i in range (8)] for j in range(8)]
            for row in range(7):
                for col in range(5):
                    if col==2 or (row==0 and col!=2):
                        print_T[row][col] = "*"
            list2.append(print_T)

        # U
        elif name[i]=="U":
            print_U = [[" " for i in range (8)] for j in range(8)]
            for row in range(7):
                for col in range(5):
                    if ((col==0 or col==4) and row!=6) or (row==6 and (col>0 and col<4)):
                        print_U[row][col] = "*"
            list2.append(print_U)

        # V
        elif name[i]=="V":
            print_V = [[" " for i in range (8)] for j in range(8)]
            for row in range(7):
                for col in range(5):
                    if ((col==0 or col==4) and (row!=5 and row!=6)) or (row==6 and (col==2)) or (row==5 and (col!=0 and col!=2 and col!=4)):
                        print_V[row][col] = "*"
            list2.append(print_V)

        # W 
        elif name[i]=="W":
            print_W = [[" " for i in range (8)] for j in range(8)]
            for row in range(7):
                for col in range(7):
                    if (col==0 or col==6) or (row==5 and (col==1 or col==5)) or (row==4 and (col==2 or col==4)) or (row==3 and (col==3)):
                        print_W[row][col] = "*"
            list2.append(print_W)

        # X
        elif name[i]=="X":
            i=0
            j=6
            print_X = [[" " for i in range (8)] for j in range(8)]
            for row in range(7):
                for col in range(7):
                    if row==i and col==j:
                        print_X[row][col] = "*"
                        i=i+1
                        j=j-1
                    elif row==col:
                        print_X[row][col] = "*"    
            list2.append(print_X)

        # Y
        elif name[i]=="Y":
            print_Y = [[" " for i in range (8)] for j in range(8)]
            for row in range(7):
                for col in range(7):
                    if (col==2 and row>1) or (row==col and col<2) or (row==0 and col==4) or (row==1 and col==3):
                        print_Y[row][col] = "*"
            list2.append(print_Y)

        # Z
        elif name[i]=="Z":
            print_Z = [[" " for i in range (8)] for j in range(8)]
            for row in range(7):
                for col in range(7):
                    if ( (row==0 or row==6) ) or ((row+col==6) ):
                        print_Z[row][col] = "*"
            list2.append(print_Z)     

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