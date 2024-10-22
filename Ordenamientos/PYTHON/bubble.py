
def bubble_sort ( arr ) :
    n = len ( arr )
    for i in range ( n - 1) :
        for j in range ( n - i - 1) :
            if arr [ j ] > arr [ j + 1]:
                arr [ j ] , arr [ j + 1] = arr [ j + 1] , arr [ j ]

def print_array ( arr ) :
    print (" ". join ( map ( str , arr ) ) )

if __name__ == " __main__ ":
    arr = [64 , 34 , 25 , 12 , 22 , 11 , 90]
print (" Array antes de ordenar :")
print_array ( arr )

bubble_sort ( arr )

print (" Array d e s p u s de ordenar :")
print_array ( arr )
