def summation(f, lo, hi):
    """
    f:  a function taking a single integer and returning a number
    lo: the starting index (inclusive)
    hi: the ending index (inclusive)

    Returns:
        Sum_{i=lo}^{hi} f(i), the sum of f(i) for every integer i from
        lo to hi, both ends included. If hi < lo, the sum is empty (0).
    """
    # TODO: Implement the summation from Theory as an explicit loop.
    #sample testcase will be like summation(lambd i:i**2,1,5)
    total = 0
    for i in range(lo, hi + 1):  #range() default stepsize is incresing 
        total = total + f(i)
    return total
