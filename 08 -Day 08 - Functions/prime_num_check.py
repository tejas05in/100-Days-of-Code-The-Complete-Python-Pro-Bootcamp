n = int(input("Check this number: "))


def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime or number < 2:
        print("It's a prime number")

    else:
        print(f"It's not a prime number")


prime_checker(number=n)
