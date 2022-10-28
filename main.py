from array import *
from random import *
box=[["-","-","-"],["-",'-',"-"],["-","-","-"]]
for k in box:
    for j in k:
        print(j, end=" ")
    print()

row_u=[0]*9
col_u=[0]*9

row_c=[0]*9
col_c=[0]*9

arr_c = []
used_places=[]

user = input("enter ur token X or O")
if (user == "x"):
    comp = "O"
else:
    comp = "X"
for i in range(0,9):



    row_u[i]=int(input("on which row do u want to place the token"))
    col_u[i]=int(input("on which coloumn do u want to place the token"))




    arr_c=[[row_u[i]],[col_u[i]]]

    while (arr_c not in used_places):
        box[row_u[i]][col_u[i]] = user
        break
    print("the place u entered is alredy occupied, as a penalty i get a extra chance")
    used_places.append([[row_u[i]],[col_u[i]]])
    for k in box:
        for j in k:
            print(j,end=" ")
        print()
    if(box[0][0]==user and box[0][1]==user and box[0][2]==user):
        print("you are the winner!")
        break
    elif(box[1][0]==user and box[1][1]==user and box[1][2]==user):
        print("you are the winner!")
        break
    elif (box[2][0] == user and box[2][1] == user and box[2][2] == user):
        print("you are the winner!")
        break
    elif (box[0][0] == user and box[1][0] == user and box[2][0] == user):
        print("you are the winner!")
        break
    elif (box[0][1] == user and box[1][1] == user and box[2][1] == user):
        print("you are the winner!")
        break
    elif (box[0][2] == user and box[1][2] == user and box[2][2] == user):
        print("you are the winner!")
        break
    elif(box[0][0]==user and box[1][1]==user and box[2][2]==user):
        print("u win")
        break
    elif(box[0][2]==user and box[1][1]==user and box[2][0]==user):
        print("u win")
        break
    row_c[i] = randint(0, 2)
    col_c[i] = randint(0, 2)


    arr_c = [[row_c[i]],[col_c[i]]]
    while(arr_c in used_places):
        row_c[i]=randint(0,2)
        col_c[i]=randint(0,2)
        arr_c = [[row_c[i]],[col_c[i]]]




    print("now ill be adding my", comp, "here")
    used_places.append([[row_c[i]], [col_c[i]]])
    box[row_c[i]][col_c[i]]=comp

    for k in box:
        for j in k:
            print(j, end=" ")
        print()
    if (box[0][0] == comp and box[0][1] == comp and box[0][2] == comp):
        print("Im the winner !")
        break
    elif (box[1][0] == comp and box[1][1] == comp and box[1][2] == comp):
        print("Im the winner !")
        break
    elif (box[2][0] == comp and box[2][1] == comp and box[2][2] == comp):
        print("Im the winner !")
        break
    elif (box[0][0] == comp and box[1][0] == comp and box[2][0] == comp):
        print("Im the winner !")
        break
    elif (box[1][0] == comp and box[1][1] == comp and box[1][2] == comp):
        print("Im the winner !")
        break
    elif (box[2][0] == comp and box[2][1] == comp and box[2][2] == comp):
        print("Im the winner !")
        break