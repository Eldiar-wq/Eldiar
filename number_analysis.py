num = input("Кез келген санды енгізіңіз: ")

# Цифрлар саны
print(f"Цифрлар саны: {len(num)}")

# Цифрлар қосындысы
sum_digits = sum(int(digit) for digit in num)
print(f"Цифрлар қосындысы: {sum_digits}")

# Палиндром тексеру
if num == num[::-1]:
    print("Бұл сан палиндром!")
else:
    print("Бұл сан палиндром емес.")
