def fizzbuzz_convert(number):
    if number % 3 == 0:
        return "Fizz"
    return number


assert fizzbuzz_convert(1) == 1
assert fizzbuzz_convert(3) == 'Fizz'
