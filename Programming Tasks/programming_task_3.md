n = 1

i = 1



def get_digits(n):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; digits = list(str(n))

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return digits



def multiply(n, prod = 1):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for i in get_digits(n):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; prod *= int(i)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return prod



def step_count(n, count = 0):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; while len(get_digits(n)) > 1:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; n = str(multiply(n))

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; count += 1

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return count



while n:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; steps = step_count(n)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; global i

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; if steps == i:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; print(i, " ", n)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i += 1

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; n += 1
