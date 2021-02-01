"""

Your #1 coding problem.

This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

"""

ar = []
count = 0

def addTo(arr, k):
  a = 0

  [ar.append(arr[a] + i) for i in arr if i != arr[a]]

  if count < len(arr):
    addTo(arr[a+1: ], k)

  return k in ar



a = [1, 2, 3, 4, 5]
k = 10

print(addTo(a, k))