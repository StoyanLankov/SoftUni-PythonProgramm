change = float(input()) * 100  # преобразуваме сумата в стотинки
coins = [200, 100, 50, 20, 10, 5, 2, 1]  # списък с наличните монети
count = 0  # брояч на използваните монети

for coin in coins:
    count += change // coin  # добавяме броя пъти, в които можем да използваме монетата
    change %= coin  # изчисляваме новото ресто

print(int(count))  # отпечатваме броя на използваните монети
