import math

n=int(input("enter a number:"))

root=math.isqrt(n)

if root*root==n:

    print("Perfect Square")

else:
    print("Not a Perfect Square")
