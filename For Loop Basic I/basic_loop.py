# 1. Basic
from itertools import count 


for loop in range(151):
    print(loop)


# 2. Multiples of Five
for fiver in range(5, 1005):
    if fiver % 5 == 0:
        print(fiver)


# 3. Counting, the Dojo Way
for sprint in range(1, 105):
    if sprint % 10 == 0:
        print('Coding Dojo')
    elif sprint % 5 == 0:
        print('Dojo')
    else: print(sprint)


# 4. Whoa. That Sucker's Huge
odd_boi = 0
for sucka in range(500000):
    if sucka % 2 != 0:
        odd_boi += sucka
print(odd_boi)


# 5. Countdown by Fours
for countdown in range(2018, 0, -4):
    print(countdown)

# 6. Flexible Counter
lowNum = 4
highNum = 40
mult = 4

for flexCount in range(lowNum, highNum + 1):
    if flexCount % mult == 0:
        print(flexCount)


