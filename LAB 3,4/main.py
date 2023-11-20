
def dist(a,b):
    def rec(i,j):
        if i==0 or j==0:
           return max(i,j)
        elif a[i-1]==b[j-1]:
            return rec(i-1, j-1)
        else:
            return 1+ min( rec(i,j-1), rec(i-1,j), rec(i-1, j-1))
    return rec(len(a),len(b))

str1=input("Введите первое слово:")
str2=input("Введите второе слово:")

lev= dist(str1,str2)
print("Расстояние Левенштейна:" + str(lev))
