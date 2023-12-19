import math
def asktoexit():
  user_input = int(float(input('Ви хочете завершити операцію? 1. Так 2. Ні   ')))
  if user_input == 1:
    print('exiting')
    exit()
    
  else:
     print('Добре, продовжую роботу')
     n1 = int(input('Яку операцію ви хочете виконати? \n 1 Алгебра \n 2 Геометрія \n 3 Фізика '))


n1 = int(input('Яку операцію ви хочете виконати? \n 1 Алгебра \n 2 Геометрія \n 3 Фізика '))

if n1 ==1:
    g = int(input('1. Подивитися формули \n '))
    if g == 1:
        print('Какую формулу вы хотите ? \n 1 (a + b)**2 \n 2 (a - b)**2 \n 3 a**2 - b**2 \n 4 (a + b)*(a - b) \n 5 (a + b)**3 \n 6 (a - b)**3  \n 7 a**3 - b**3 \n  ' )
        z = int(input('>>> '))

        if z == 1:
            a = input("Введіть значення a: ")
            b = input("Введіть значення b: ")

            if a.isdigit():
                a = int(a)
                print(f'{a ** 2} + {2 * a}{b} + {b}**2')
                asktoexit()
            if b.isdigit():
                b = int(b)
                print(f'{a}  2 + {2 * b}{a} + {b ** 2}')
                asktoexit()
        elif z == 2:
            a = input("Введіть значення a: ")
            b = input("Введіть значення b: ")

            if a.isdigit():
                a = int(a)
                print(f'{a ** 2} - {2 * a}{b} + {b}**2')
                asktoexit()
            if b.isdigit():
                b = int(b)
                print(f'{a}  2 - {2 * b}{a} + {b **2}')
                asktoexit()
        elif z == 3:
            a = input("Введіть значення a: ")
            b = input("Введіть значення b: ")

            if a.isdigit():
                a = int(a)
                print(f'({a} - {b}) * ({a} + {b})')
                asktoexit()
            if b.isdigit():
                b = int(b)
                print(f'({a} - {b}) * ({a} + {b})')
                asktoexit()

        if z == 8:
            a = input("Введіть значення a: ")
            b = input("Введіть значення b: ")

            if a.isdigit():
                a = int(a)
                print(f'{a ** 2} + {2 * a}{b} + {b}**2 * ({a} + {b})')
                asktoexit()
            if b.isdigit():
                b = int(b)
                print(f'{a}  2 + {2 * b}{a} + {b **2} * ({a} + {b})')
                asktoexit()

        elif z == 9:

              print(f'Результат: {a - 3 * a * b + b}')
              asktoexit()
if n1 == 3:
    g = int(input('1. Подивитися формули \n2. Зробити розрахунки по формулам \n'))
    if g == 1:
        print('Формула тонкої лінзи                        F = 1 / (1/d+1/f)')
        print('Формула розсіювальної лінзи                 F = -1 / (1/d-1/f)')
        print('Формула ККД нагрівника                      n = (c * m1 * (t2 - t1)) / (q * m2)')
        print('Формула питомої теплоємності (ДЛЯ ЛР)       c = (c * m1 * (t - t1)) / (m2 * (t2 - t))')
        print('Формула питомої теплоємності                c = Q / (m * (t2 - t1)')
        print('Формула cили струму                         I = U / R')
        print('Формула напруги                             U = A / q')
        print('Оптична сила лінзи                          D = 1 / F')
        print('Збільшення лінзи ( перший варіант )         Г = H1 / h2')
        print('Збільшення лінзи ( другий варіант)          Г = f / d')


    if g == 2:
        z = int(input('Яка формула вас цікавить? \n 1. Формула тонкої лінзи \n 2. Формула розсіювальної лінзи \n 3. Формула ККД нагрівника \n 4. Формула питомої теплоємності (ДЛЯ ЛР) \n 5.Формула питомої теплоємності \n 6. Формула cили струму \n 7. Формула напруги \n 8. Оптична сила лінзи \n 9. Збільшення лінзи ( перший варіант )  \n 10. Збільшення лінзи ( другий варіант ) '))

        if z == 1:
            d = float(input('Введіть значення d: '))
            f = float(input('Введіть значення f: '))
            print('F =', 1 / (1 / d + 1 / f))
            asktoexit()

        elif z == 2:
            d = float(input('Введіть значення d: '))
            f = float(input('Введіть значення f: '))
            print('F =', -1 / (1 / d - 1 / f))
            asktoexit()
            

        elif z == 3:
            c = float(input('Введіть значення с: '))
            m1 = float(input('Введіть значення m1: '))
            t2 = float(input('Введіть значення t2: '))
            t1 = float(input('Введіть значення t1: '))
            q = float(input('Введіть значення q: '))
            m2 = float(input('Введіть значення m2: '))
            print('n =', (c * m1 * (t2 - t1)) / (q * m2))
            asktoexit()

        elif z == 4:
            c = float(input('Введіть значення с: '))
            m1 = float(input('Введіть значення m1: '))
            t = float(input('Введіть значення t: '))
            t1 = float(input('Введіть значення t1: '))
            m2 = float(input('Введіть значення m2: '))
            t2 = float(input('Введіть значення t2: '))
            print('с =', (c * m1 * (t - t1)) / (m2 * (t2 - t)))
            asktoexit()

        elif z == 5:
            Q = float(input('Введіть значення Q: '))
            m = float(input('Введіть значення m: '))
            t2 = float(input('Введіть значення t2: '))
            t1 = float(input('Введіть значення t1: '))
            print('c =', Q / (m * (t2 - t1)))
            asktoexit()

        elif z == 6:
            U = float(input('Введіть значення U: '))
            R = float(input('Введіть значення R: '))
            print('I =', U / R)
            asktoexit()

        elif z == 7:
            A = float(input('Введіть значення A: '))
            q = float(input('Введіть значення q: '))
            print('U =', A / q)
            asktoexit()

        elif z == 8:
            F = float(input('Введіть значення F: '))
            print('D =', 1 / F)
            asktoexit()

        elif z == 9:
            H1 = float(input('Введіть значення H1: '))
            h2 = float(input('Введите длину стороны h2: '))
            print('Г =', H1 / h2)
            asktoexit()

        elif z == 10:
            f = float(input('Введіть значення f: '))
            d = float(input('Введіть значення d: '))
            print('Г =', f / d)
            asktoexit()
        else:
            print('Ви, щось неправильно ввели')
            asktoexit()

if n1 == 2:
    b1 = int(input('Тобі потрібна формула чи розвязок? 1.Формула 2.Розвязок'))
    if b1 == 2:
     z = int(input('Яку формулу ви хочете використовувати? \n 1 Площа прямокутника \n 2. Площа трикутника через основу та висоту \n 3. Формула Піфагора (для прямокутного трикутника) \n 4. Формула для площі кола \n 5. Довжина кола \n 6. Обєм прямокутного паралелепіпеда \n 7. Формула Герона для площі трикутника \n 8. Теорема косинусів \n 9. Формула для знаходження кута в середині трикутника (з використанням тангенса) \n 10. Формула для обєму конуса'))

     if z == 1:
        z2 = float(input('Введіть значення a: '))
        z3 = float(input('Введіть значення b: '))
        print('S =', z2 * z3)
        asktoexit()

     elif z == 2:
        z4 = float(input('Введіть значення a (основи) : '))
        z5 = float(input('Введіть значення h (висоти) : '))
        print('S =', z4 * z5 * 0.5)
        asktoexit()

     elif z == 3:
        a = float(input('Введіть довжину катета a: '))
        b = float(input('Введіть довжину катета b: '))
        c = math.sqrt(a**2 + b**2)
        print('Гіпотенуза c =', c)
        asktoexit()

     elif z == 4:
        r = float(input('Введіть радіус кола: '))
        S = math.pi * r**2
        print('Площа кола: ', S)
        asktoexit()

     elif z == 5:
        r = float(input('Введіть радіус кола: '))
        C = 2 * math.pi * r
        print('Довжина кола: ', C)
        asktoexit()

     elif z == 6:
        a = float(input('Введіть довжину сторони a: '))
        b = float(input('Введіть довжину сторони b: '))
        h = float(input('Введіть висоту h: '))
        V = a * b * h
        print('Об\'єм прямокутного паралелепіпеда: ', V)
        asktoexit()

     elif z == 7:
        a = float(input('Введіть довжину сторони a: '))
        b = float(input('Введіть довжину сторони b: '))
        c = float(input('Введіть довжину сторони c: '))
        p = (a + b + c) / 2
        S = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print('Площа трикутника: ', S)
        asktoexit()

     elif z == 8:
        a = float(input('Введіть довжину сторони a: '))
        b = float(input('Введіть довжину сторони b: '))
        C = float(input('Введіть кут C в градусах: '))
        c_squared = a**2 + b**2 - 2 * a * b * math.cos(math.radians(C))
        print('Квадрат довжини сторони c: ', c_squared)
        asktoexit()

     elif z == 9:
        a = float(input('Введіть довжину сторони a: '))
        b = float(input('Введіть довжину сторони b: '))
        A = math.degrees(math.atan(a / b))
        print('Кут A в градусах: ', A)
        asktoexit()


     elif z == 10:
        r = float(input('Введіть радіус конуса: '))
        h = float(input('Введіть висоту конуса: '))
        V = (1/3) * math.pi * r**2 * h
        print('Об\'єм конуса: ', V)
        asktoexit()

     else:
        print('Невірний вибір формули.')
        asktoexit()

    elif b1 == 1:

      b01 = int(input('Яку формулу ти хочеш? \n 1 Площа прямокутника \n 2. Площа трикутника через основу та висоту \n 3. Формула Піфагора (для прямокутного трикутника) \n 4. Формула для площі кола \n 5. Довжина кола \n 6. Обєм прямокутного паралелепіпеда \n 7. Формула Герона для площі трикутника \n 8. Теорема косинусів \n 9. Формула для знаходження кута в середині трикутника (з використанням тангенса) \n 10. Формула для обєму конуса' ))

      if b01 == 1:
        print('S = довжина * ширина')
        asktoexit()

      elif b01 == 2:
        print('S = 0.5 * основа * висота')
        asktoexit()

      elif b01 == 3:
        print('гіпотенуза = корінь (катет_1**2 + катет_2**2)')
        asktoexit()

      elif b01 == 4:
        print('S = Пі * радіус**2')
        asktoexit()

      elif b01 == 5:
        print('C = 2 * Пі * радіус')
        asktoexit()

      elif b01 == 6:
        print('V = довжина * ширина * висота')
        asktoexit()

      elif b01 == 7:
        print('S= корінь s⋅(s−a)⋅(s−b)⋅(s−c)')
        asktoexit()

      elif b01 == 8:
        print('root a^2+b^2﹣2abcosγ')
        asktoexit()

      elif b01 == 9:
        print('12(a+b+c)a')
        asktoexit()

      elif b01 == 10:
        print('V = (1/3) * Пі * радіус основи^2 * висота')
        asktoexit()
