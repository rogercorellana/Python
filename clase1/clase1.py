x = 1
y = "hola"
arr = [64, 34, 25, 12, 22, 11, 90]
arr2 = ["esto","es", "un","array"]







def miFunc():
    print("hola")

def miFunc2(numero):
    if numero %2 == 0:
        print("el numero {} es par".format(numero))
    else:
        print("el numero {} es impar".format(numero)) 


def miFunc3(array):
    for e in array:
        print(array.index(e), "  ", e)

def loop():
    for i in range(0, 9, 2):
        print(i)

def matrix():
    Row = int(input("Enter the number of rows:"))
    Column = int(input("Enter the number of columns:"))
    matrix = []
    print("Enter the entries row wise:")
    for row in range(Row):    
        a = []
        
        for column in range(Column):   
            a.append(int(input()))
        matrix.append(a)
    for row in range(Row):
        for column in range(Column):
            print(matrix[row][column], end=" ")
        print()   

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print("Sorted array is:", arr)


bubble_sort(arr)


