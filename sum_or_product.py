number = int(input('Please enter an integer greater than 0:  '))
operation = input('Enter "s" to compute the sum, or "p" to compute the product.')

def number_sum(number):
    return sum(range(1, number + 1))

def number_product(number):
    result = 1
    for num in range (1, number + 1):
        result *= num
    return result

if operation == 's':
    print(f'The sum of the integers between 1 and {number} is {number_sum(number)}')

if operation == 'p':
    print(f'The product of the integers between 1 and {number} is {number_product(number)}')

    