quantity_minutes = int(input())

hour = quantity_minutes // 60
minutes = quantity_minutes % 60

print(f'{quantity_minutes} мин - это {hour} час {minutes} мин')
