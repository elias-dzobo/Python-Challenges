"""

There are N couples sitting in a row of length 2 * N. 
They are currently ordered randomly, but would like to rearrange themselves so that each couple's partners can sit side by side.

What is the minimum number of swaps necessary for this to happen?

"""
n = 5
couples = 2 * list(range(1, n+1))

def arrangeCouples(couples):

    

    if couples != sorted(couples):

        if couples[0] != couples[1]:

            c1 = couples[0]
            a = couples[2:].index(c1)

            couples[1], couples[a] = couples[a], couples[1]

            arrangeCouples(couples[2:])



 


print(arrangeCouples(couples))