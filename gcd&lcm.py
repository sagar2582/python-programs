def gcd(a,b):
    if a ==0:
        return b
    return gcd(b%a, a)


def lcm(a,b):
    hcf = gcd(a,b)
    product = a*b
    return product // hcf


n,m = map(int(input.split()))
print("gcd = {} & lcm = {}".format(gcd(n,m), lcm(n,m)))
