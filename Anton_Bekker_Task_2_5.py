prices = [57.8, 46.51, 97, 45.24, 28.9, 31, 99, 9.99, 87.1, 12.36]
print('Задание A')
for price in prices:
    if prices.index(price) == len(prices) - 1:
        print(f'{int(price)} руб {int((100 * price) % 100):02d} коп.')
    else:
        print(f'{int(price)} руб {int((100 * price) % 100):02d} коп,', end=' ')
print('-' * 35)
print('Задание B')
print(id(prices), prices)
prices.sort()
print(id(prices), prices)
for price in prices:
    if prices.index(price) == len(prices) - 1:
        print(f'{int(price)} руб {int((100 * price) % 100):02d} коп.')
    else:
        print(f'{int(price)} руб {int((100 * price) % 100):02d} коп,', end=' ')
print('-' * 35)
print('Задание C')
new_prices = prices[::-1]
print(new_prices)
print('-' * 35)
print('Задание D')
prices = [57.8, 46.51, 97, 45.24, 28.9, 31, 99, 9.99, 87.1, 12.36]
prices.sort()
for price in prices[:4:-1]:
    print(f'{int(price)} руб {int((100 * price) % 100):02d} коп|', end=' ')
