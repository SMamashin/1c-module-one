try:
    num1 = float(input("Введите число: "))
    num2 = float(input("Введите ещё одно число: "))
    result = num1 + num2
    print(f"Сумма ваших чисел: {result}")

except ValueError:
    print('Я могу принимать только целые и дробные числа!')
    
finally:
    print('Завершение работы.')