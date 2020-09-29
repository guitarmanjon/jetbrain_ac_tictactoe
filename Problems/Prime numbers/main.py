def is_prime(num):
    if num == 2:
        return True

    if num % 2 == 0:
        return False

    for d in range(3, num, 2):
        if num % d == 0:
            return False
    return True


prime_numbers = []

for n in range(2, 1000):
    if is_prime(n):
        prime_numbers.append(n)

# Copied from the solutions:
# prime_numbers = [x for x in range(2, 1001) if all(x % y != 0 for y in range(2, (x - 1)))]


# print(prime_numbers)
