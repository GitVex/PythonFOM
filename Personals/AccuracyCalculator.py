def calc(iterations):
    result = {}
    for i in range(iterations):
        x = i + i/10
        y = i+1 + (i+1)/10
        result[x + y] = x + y == float(str(str(2*i+1) + "." + str(2*i+1)))
    return result

# gets only the prime numbers ... whatever, I'm not too involved in this
print(calc(10))
