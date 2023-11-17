def prime_factorization(num: int) -> tuple[int, list[int]]:
    # our list of primefactors
    primefactors: list[int] = []
    # our first prime number
    prime: int = 2
    # we don't want to modify our number and copy it to `n`
    n: int = num

    # iterate until we find the last step the square of
    # our prime is bigger than our rest number
    while n != 1:
        # if our number is dividable by our prime
        if n % prime == 0:
            # we can add the prime to our primefactors
            primefactors.append(prime)
            # and divide our rest number by the prime number
            n //= prime
        else:
            # increment until next prime number
            prime += 1

    # finally return our tuple with our number and primefactors
    return (num, primefactors)


if __name__ == "__main__":
    assert (sol := (100, [2, 2, 5, 5])) == (
        res := prime_factorization(100)), f"{res} is not {sol}"
    assert (sol := (69, [3, 23])) == (
        res := prime_factorization(69)), f"{res} is not {sol}"
    assert (sol := (31, [31])) == (
        res := prime_factorization(31)), f"{res} is not {sol}"
    assert (sol := (123490823022, [2, 3, 3, 3, 3, 7, 7, 7, 1123, 1979])) == (
        res := prime_factorization(123490823022)), f"{res} is not {sol}"
