from itertools import count
import random
import math

picked_numbers = []
all_numbers = []
random_numbers = []
is_six = False
count_numbers=0

for a in range(1,50):
    all_numbers.append(a)
random_numbers = random.sample(all_numbers, 6)
print(random_numbers)

while is_six==False:
    number = input("input number: ")
    result1 = number.isdigit()
    if result1 == True:
        number = int(number)
        if  number>=1 and number<50:
            picked_numbers.append(number)
            count_numbers+=1
            print('Dozwolona liczba!')
    if count_numbers == 6:
        is_six = True
hit = 0
for x in range(6):
    for y in range(6):
        if picked_numbers[x] == random_numbers[y]:
            hit+=1
if(hit==0):
    print('Nic nie trafiłeś ;(')
elif(hit>=1 and hit<6):
    print('Trafileś ', hit, ' liczb!')
else:
    print('Trafiłeś 6 woow!!')