number = input ('Введите трехзначное число:')

numbers = int(number)
sum = numbers//100 + (numbers % 100)//10 + numbers%10 
product = (numbers//100) * ((numbers % 100)//10) * (numbers%10)

print ('Сумма цифр =', sum)
print ('Произведение цифр =', product)
