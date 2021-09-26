n = input("Type a number")

count = 0


def get_digits(n):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; digits = list(n)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return digits



def multiply(prod = 1):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; for i in get_digits(n):

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; prod *= int(i)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return prod



while len(get_digits(n)) > 1:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; n = str(multiply())

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; count += 1


print(count)
