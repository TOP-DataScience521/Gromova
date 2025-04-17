number = input ('Введите трехзначное число:')

numbers = int(number)
sum = numbers//100 + (numbers % 100)//10 + numbers%10 
product = (numbers//100) * ((numbers % 100)//10) * (numbers%10)

print ('Сумма цифр =', sum)
print ('Произведение цифр =', product)

# Введите трехзначное число:231
# Сумма цифр = 6
# Произведение цифр = 6