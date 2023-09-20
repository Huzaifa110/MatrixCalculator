# MATRIX CALCULATOR
print("         MATRIX CALCULATOR")
print("                   BY, MUHAMMAD HUZAIFA")
row=int(input("ENTER NUMBER OF ROWS:"))
col=int(input("ENTER NUMBER OF COLUMNS:"))
print()
print("OPTIONS MENU")
print("     1.ADDITION")
print("     2.SUBTRACTION")
print("     3.MULTLIPLICATION")
print("     4.EXIT")
print()
choice=int(input("ENTER OPTION NUMBER:"))
print()
if choice>3:
    print("GOOD BYE")
if choice==1 or choice==2 or choice==3:
    print("ENTER THE ELEMENTS OF MATRIX 1:")
    matrix1=[[int(input())for i in range(col)]for j in range(row)]
    print("MATRIX 1:")
    for i in range(row):
        for j in range(col):
            print(matrix1[i][j],end='    ')
        print()
    print()
    print("ENTER THE ELEMENTS OF MATRIX 2:")
    matrix2=[[int(input())for i in range(col)]for j in range(row)]
    print("MATRIX 2:")
    for i in range(row):
        for j in range(col):
            print(matrix2[i][j],end='    ')
        print()
    print()
if choice==1:
    result=[[0 for i in range(col)]for j in range(row)]

    for i in range(row):
        for j in range(col):
            result[i][j]=matrix1[i][j]+matrix2[i][j]

    print("BY ADDITION,RESULT IS:")
    for i in range(row):
        for j in range(col):
            print(result[i][j],end='    ')
        print()
elif choice==2:
    result=[[0 for i in range(col)]for j in range(row)]
    for i in range(row):
        for j in range(col):
            result[i][j]=matrix1[i][j]-matrix2[i][j]

    print("BY SUBTRACTION,RESULT IS:")
    for i in range(row):
        for j in range(col):
            print(result[i][j],end='    ')
        print()
elif choice==3:
    result=[[0 for i in range(col)]for j in range(row)]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j]+=matrix1[i][k]*matrix2[k][j]
            
    print("BY MULTIPLICATION,RESULT IS:")
    for i in range(row):
        for j in range(col):
            print(result[i][j],end='    ')
        print()
    print()
print()


print("THANKS FOR USING")



    


