miles_whole = int (input())
miles_fraction = int (input())

miles = miles_whole + miles_fraction / 10
kilometers = miles * 1.61
kilometers_rounded = f'{kilometers:.1f}'

print(f'{miles} миль = {kilometers_rounded} км')

# 1
# 4
# 1.4 миль = 2.3 км