# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def find_sum_of_multiples(n: int, a: int, b: int)-> int:
    total = 0
    for i in range(1, n):
        if i % a == 0 or i % b == 0:
            total += i
    return total


def main():
    print(find_sum_of_multiples(1000, 3, 5))


if __name__ == '__main__':
    main()
