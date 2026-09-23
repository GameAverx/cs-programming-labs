benz = float(input())
average = float(input())
benz_price = float(input())


benz_needed = (benz/100)*average
total_benz_price = benz_needed*benz_price
print(f'Топливо: {benz_needed:.2f} л')
print(f'Стоимость: {total_benz_price:.2f} руб')
