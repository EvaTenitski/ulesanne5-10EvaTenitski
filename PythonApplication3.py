print("Hello world!")

#5
import math
# Küsime kasutajalt ristkülikukujulise maatüki mõõtmeid
N = float(input("Sisestage maatüki pikkus meetrites (N): "))
M = float(input("Sisestage maatüki laius meetrites (M): "))
# Arvutame ristkülikukujulise maatüki diagonaali pikkuse
diagonaali_pikkus = math.sqrt(N**2 + M**2)
print(f"Ristkülikukujulise maatüki diagonaali pikkus on {diagonaali_pikkus} meetrit")
#6
time = float(input("Сколько часов ушло на поездку?"))
distance = float(input("Сколько километров вы проехали?"))
speed = distance / time
print("Ваша скорость была " + str(speed) + " км/ч")
#7 
numbers = []
for i in range(5):
    number = int(input(f"Введите целое число {i+1}: "))
    numbers.append(number)
    total = sum(numbers)
    average = total / 5
print(f"Среднее арифметическое введенных чисел: {average}")
#8 import turtle

#9 
a = 5
b = 7
c = 8
perimeter = a + b + c
print(f"Периметр треугольника со сторонами {a}, {b} и {c} равен {perimeter}")
# Pitsa maksumus
pitsa_hind = 12.90
# Jootraha protsent
jootraha_protsent = 0.10  # 10%
# Arvutame jootraha summa
jootraha_summa = pitsa_hind * jootraha_protsent
# Kogu maksmise summa
kogu_makse = pitsa_hind + jootraha_summa
# Inimeste arv, kes maksavad
inimeste_arv = 2  # Teie ja teie sõber
# Arvutame, kui palju igaüks peab maksma
igaühe_makse = kogu_makse / inimeste_arv
print(f"Igaüks teist peab maksma {igaühe_makse:.2f} eurot")

