def black_box1(noun, times):
    return noun * times


my_output = black_box1("home ", 5)
print(my_output)


def black_box2(number):
    count = 0
    lst = str(number)
    for i in lst:
        if i == "0":
            count += 1
    return count


print(black_box2(12345000))


def black_box3(number):
    count = 0
    i = number
    while i > 9:
        if i % 10 == 0:
            count += 1
        i //= 10
    return count


print(black_box3(120600302))
print("\n")


def black_box4(n):
    if n >= 1:
        prime = "2"
        if n > 1:
            i = 3
            num_prime = 0
            while num_prime <= n:
                is_prime = True
                for j in range(2, i//2 + 1):
                    if i % j == 0:
                        is_prime = False
                if is_prime:
                    prime += f"\n{i}"
                    num_prime += 1
                i += 2

        return prime


print(black_box4(10))
