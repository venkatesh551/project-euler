# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_of_arithmetic_series(a: int, d: int, n: int)-> int:
    last_term = a + (n - 1) * d
    return int(n/2.0 * (a + last_term))

def find_sum_of_multiples(n: int, a: int, b: int)-> int:
    return (
        sum_of_arithmetic_series(a, a, (n-1)//a) +
        sum_of_arithmetic_series(b, b, (n-1)//b) -
        sum_of_arithmetic_series(a * b, a * b, (n-1)//(a * b))
    )


def main():
    print(find_sum_of_multiples(1000, 3, 5))


if __name__ == '__main__':
    main()
