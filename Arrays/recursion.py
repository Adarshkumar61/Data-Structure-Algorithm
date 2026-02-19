def run(n):
    if n == 0:
        return
    print(n)
    run(n-1)
    print(n)

run(3)

"""here logic is :
the first print statement prints the value of n before the recursive call,
 and the second print statement prints the value of n
   after the recursive call returns.
When you call run(3), the firstoutput will be:
321
Then, as the recursive calls return, the second output will be:123
This is because the second print statement is executed after the recursive call returns,
"""