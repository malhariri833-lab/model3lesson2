def factorle(X):
    ''' this is a function which does recursion '''
    if X==0 or X==1:
        return 1
    else:
        return(X*factorle(X-1))

print("factorle=",factorle(5))
print(factorle.__doc__)