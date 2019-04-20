# this program can identify the max sum of all sub-sequence by using the online searching
# the first input is the int shows the length of the sequence
# the second input is the line list of the sequence and every elements are divided by the space
# zero will be returned if all input integers are negative
# output are ordered: the largest sum, together with the first and the last numbers of the maximum subsequence
K = int(input())
line = input()
sequence = [int(x) for x in line.split()]
if len([x for x in sequence if x >= 0]) == 0:
    print('0', sequence[0], sequence[-1])
else:
    # initial the counter and Sum max
    MaxSum = ThisSum = 0
    Head = Bottom = 0
    TempHead = TempBottom = 0
    for x in range(K):
        ThisSum = ThisSum + sequence[x]
        if ThisSum > MaxSum:
            MaxSum = ThisSum
            Bottom = x
            Head = TempHead
        elif ThisSum < 0:
            ThisSum = 0
            TempHead = x + 1
        else:
            pass
    print(MaxSum, sequence[Head], sequence[Bottom])