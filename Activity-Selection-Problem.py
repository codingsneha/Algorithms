def Activities(s, f):
   print ("The selected activities are:")
   i = 0
   print (i+1,end=" ")
   for j in range(1, len(f)):
        if s[j] >= f[i]:
            print (j+1,end=" ")
            i = j
# main
s = [1, 2, 0, 3, 2, 4]
f = [2, 5, 4, 6, 8, 8]
Activities(s, f)