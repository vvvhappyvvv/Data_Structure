'''
 this program receive two polynomial and return the multiply and add result
 the input is two line int, the element with odd subscript is the index while
 the even one shows the exponent, the first number is the number of non-zero polynomials
 input example :
 3 4 5 6 4 2 1
 2 4 1 3 0
'''

line1 = input()
poly1 = [int(x) for x in line1.split()]
len_poly1 = poly1[0]
poly1 = poly1[1:]

line2 = input()
poly2 = [int(x) for x in line2.split()]
len_poly2 = poly2[0]
poly2 = poly2[1:]

'''
len_poly1 = 3
len_poly2 = 2
poly1 = [4, 3, 2, 2, 1, 0]
poly2 = [6, 3, 4, 0]
'''
poly1_backup = poly1
poly2_backup = poly2

# the add
poly_add = []
if len([x for x in poly1 + poly2 if x != 0]):
    while len(poly1) + len(poly2):
        if len(poly1) == 0:
            poly_add = poly_add + poly2
            poly2 = []
        elif len(poly2) == 0:
            poly_add = poly_add + poly1
            poly1 = []
        elif poly1[1] > poly2[1]:
            poly_add = poly_add + poly1[0:2]
            poly1 = poly1[2:]
        elif poly1[1] < poly2[1]:
            poly_add = poly_add + poly2[0:2]
            poly2 = poly2[2:]
        elif poly1[1] == poly2[1]:
            poly_add = poly_add + [poly1[0] + poly2[0], poly1[1]]
            poly1 = poly1[2:]
            poly2 = poly2[2:]
else:
    # if all the elements are zeros
    poly_add = [0, 0]

# the multiply
poly1 = poly1_backup
poly2 = poly2_backup
poly_multi = []
if len([x for x in poly1 + poly2 if x != 0]):
    for m in range(len_poly1):
        for n in range(len_poly2):
            poly_multi = poly_multi + [poly1[m * 2] * poly2[n * 2], poly1[m * 2 + 1] + poly2[n * 2 + 1]]
    poly_sort = []
    poly_tuple = [(poly_multi[2 * x], poly_multi[2 * x + 1]) for x in range(int(len_poly2 * len_poly1))]

    # use the sorted function
    def by_order(tuple):
        return -tuple[1]

    poly_tuple2 = sorted(poly_tuple, key=by_order)

    # merge the items with same order
    i = 0
    while i < len(poly_tuple2) - 1:
        if poly_tuple2[i][1] == poly_tuple2[i + 1][1]:
            if i < len(poly_tuple2) - 1:
                poly_tuple2 = poly_tuple2[:i] + [((poly_tuple2[i][0] + poly_tuple2[i + 1][0]), poly_tuple2[i][1])] \
                              + poly_tuple2[i + 2:]
                i = i - 1
            else:
                poly_tuple2 = poly_tuple2[:i] + [((poly_tuple2[i][0] + poly_tuple2[i + 1][0]), poly_tuple2[i][1])]
                i = i - 1
        i = i + 1
    # recover the tuple back to list
    poly_multi = [poly_tuple2[i][j] for i in range(len(poly_tuple2)) for j in range(2)]
else:
    # if all the elements are zeros
    poly_multi = [0, 0]

print(*poly_multi)
print(*poly_add)