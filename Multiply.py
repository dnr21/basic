

X = [[12,17,13],

    [41 ,15,16],

    [77 ,58,69]]



Y = [[5,85,1,2],

    [6,7,37,90],

    [4,5,69,120]]



result = [[0,0,0,0],

         [0,0,0,0],

         [0,0,0,0]]



for i in range(len(X)):



   for j in range(len(Y[0])):



       for k in range(len(Y)):

           result[i][j] += X[i][k] * Y[k][j]

for r in result:

   print(r)

