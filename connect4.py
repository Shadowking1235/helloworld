n = 4
m = 4
a = [[0] * m] * n
a[0][0] = 0
#We make a board of a 2-d list which contains 0 initially.
#Player 1 enters 1 on the board
#Player 2 enters 2 on the board
def draw(m,n):
  for x in range(0,m):
        for y in range(0,n):
            print(a[x][y],end=' ')
        print("\n")
draw(m,n)
Player=1
Value=0
while(True):
    if(Player==1):
         coloumn=int(input("Enter the coloumn: "))
         '''
         range done so as to check the rows from the bottom in the game
         As per the connect 4 game rules
         '''
         for x in range(m-1,-1,-1):
            if(a[x][coloumn]==0):
                a[x][coloumn]=1


                Player=2
                break

            else:
                Player=1



    elif(Player==2):
         coloumn=int(input("Enter the coloumn: "))

         for x in range(m-1,-1,-1):
            if(a[x][coloumn]==0):
                a[x][coloumn]=2
                Player=1
                break

            else:
                Player=2


    draw(m,n)
    #The two loops are for checking the rows
    for x in range(0,m):
        for y in range(0,n):
            if(a[x][y]==2):
              Value=2
            else:
                Value=0
                break
            print("Player 2 wins")
    for x in range(0,m):
        for y in range(0,n):
            if(a[x][y]==1):
              Value=1
            else:
                Value = 0
                break
                break
            print("Player 1 wins")
    for y in range(0,n):
        for x in range(0,m):
            if(a[x][y]==2):
              Value=2
            else:
                Value=0
                break
                break
            print("Player 2 wins")
    for y in range(0, n):
        for x in range(0, m):
            if (a[x][y] == 1):
                Value = 1
            else:
                Value=0
                break
                break
            print("Player 1 wins")
    #For checking the first or major diagonal of the list.
    for x in range(0,m):
        for y in range(0,n):
            if(x==y):
              if(a[x][y]==1):
                Value=1
              else:
                Value=0
                break
                break
            print("Player 2 wins")
    for x in range(0,m):
        for y in range(0,n):
            if(x==y):
              if(a[x][y]==2):
                Value=2
              else:
               Value = 0
               break
               break
            print("Player 2 wins")
    #For checking the other diagonal or minor diagonal
    for x in range(0,m):
        for y in range(0,n):
            if(x+y==n-1):
              if(a[x][y]==2):
                Value=2
              else:
                Value = 0
                break
                break
            print("Player 2 wins")
    for x in range(0,m):
        for y in range(0,n):
            if(x+y==n-1):
              if(a[x][y]==1):
                Value=1
              else:
                Value = 0
                break
                break
            print("Player 1 wins")