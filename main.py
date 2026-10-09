# Class work
# 1. Добавление элемента
# Дан список:
# numbers = [10, 20, 30, 40]
# Добавь число 50 в конец списка с помощью append().
# lst=[10,20,30,40]
# lst.append(50)
# print(lst)
# 2. Добавление нескольких элементов
# Дан список:
# languages = ["Python", "C++"]
# Добавь "Java", "Go" и "Rust" с помощью extend().
# lst=["Python", "C++"]
# lst2=["Java", "Go","Rust"]
# lst.extend(lst2)
# print(lst)
# 3. Вставка элемента
# Дан список:
# students = ["Ali", "Muhammad", "John"]
# Вставь "Alijon" на позицию с индексом 1 с помощью insert().
# students = ["Ali", "Muhammad", "John"]
# students.insert(1,"Alijon")
# print(students)
# 4. Удаление последнего элемента
# Дан список:
# numbers = [10, 20, 30, 40, 50]
# Удали последний элемент с помощью pop() и выведи удалённое значение.
# numbers = [10, 20, 30, 40, 50]
# numbers.pop(-1)
# print(numbers)
# 5. Удаление конкретного элемента
# Дан список:
# fruits = ["apple", "banana", "orange", "banana"]
# Удали первое "banana" с помощью remove().
# fruits = ["apple", "banana", "orange", "banana"]
# fruits.remove("banana")
# print(fruits)
# 6. Подсчёт элементов
# Дан список:
# numbers = [1, 2, 3, 2, 4, 2, 5, 2]
# С помощью count() узнай, сколько раз встречается число 2.
# numbers = [1, 2, 3, 2, 4, 2, 5, 2]
# c= numbers.count(2)
# print(c)
# 7. Поиск позиции
# Дан список:
# students = ["Ali", "John", "Muhammad", "Said"]
# С помощью index() найди индекс "Muhammad".
# students = ["Ali", "John", "Muhammad", "Said"]
# c=students.index("Muhammad")
# print(c)
# 8. Копирование списка
# Дан список:
# numbers = [1, 2, 3, 4, 5]
# Создай его независимую копию с помощью copy(). Измени копию и докажи, что оригинальный список не изменился.
# numbers = [1, 2, 3, 4, 5]
# numbers2=numbers.copy()
# print(numbers2)
# 9. Очистка списка
# Дан список:
# Полностью очисти корзину с помощью clear().
# cart = ["phone", "laptop", "mouse", "keyboard"]
# cart = ["phone", "laptop", "mouse", "keyboard"]
# cart.clear()
# print(cart)
# 10. Разворот списка
# Дан список:
# numbers = [1, 2, 3, 4, 5]
# Разверни его в обратном порядке с помощью reverse().
# numbers = [1, 2, 3, 4, 5]
# numbers.reverse()
# print(numbers)
# 11. Сортировка чисел
# Дан список:
# numbers = [45, 12, 78, 3, 29, 10]
# Отсортируй список по возрастанию с помощью sort().
# numbers = [45, 12, 78, 3, 29, 10]
# numbers.sort()
# print(numbers)
# 12. Сортировка по убыванию
# Дан список:
# numbers = [15, 4, 89, 32, 7, 21]
# Отсортируй его по убыванию, используя sort().
# numbers = [45, 12, 78, 3, 29, 10]
# numbers.sort()
# print(numbers)
# 13. Работа с двумя списками
# Даны:
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# Добавь все элементы list2 в list1 с помощью extend().
# Затем добавь число 7 с помощью append().
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# list1.extend(list2)
# list1.append(7)
# print(list1)
# 14. Управление очередью
# Дан список:
# queue = ["Ali", "John", "Muhammad", "Said"]
# Удали первого человека с помощью pop().
# Добавь "Rustam" в конец.
# Добавь "Karim" в начало списка с помощью insert().
# Выведи итоговый список.
# queue = ["Ali", "John", "Muhammad", "Said"]
# queue.pop(0)
# queue.append("Rustam")
# queue.insert(0,"Karim")
# print(queue)
# 15. Работа с оценками
# Дан список оценок:
# grades = [75, 90, 60, 90, 85, 70, 90]
# Выполни следующие действия:
# Узнай, сколько раз встречается 90 с помощью count().
# Найди индекс первой оценки 85 с помощью index().
# Добавь оценку 95 через append().
# Удали одну оценку 60 через remove().
# Отсортируй оценки по возрастанию через sort().
# Разверни список через reverse().
# Выведи итоговый список.
# grades = [75, 90, 60, 90, 85, 70, 90]
# grades.count
# grades.index(85)
# grades.append(95)
# grades.remove(60)
# grades.sort
# grades.reverse
# print(grades)

# Homework
# 16. Список покупок
# shopping = ["bread", "milk", "eggs", "cheese"]
# Добавь "butter" через append().
# Добавь "juice" и "water" через extend().
# Вставь "meat" на индекс 1 через insert().
# Удали "eggs" через remove().
# Отсортируй список через sort().
# shopping = ["bread", "milk", "eggs", "cheese"]
# shopping.append("butter")
# shopping.extend(["juice","water"])
# shopping.insert(1,"meat")
# shopping.remove("eggs")
# shopping.sort
# print(shopping)
# 17. Баллы студентов
# scores = [85, 70, 95, 60, 85, 75]
# Узнай количество 85 через count().
# Найди индекс 95 через index().
# Добавь 100 через append().
# Удали 60 через remove().
# Отсортируй список по возрастанию.
# scores = [85, 70, 95, 60, 85, 75]
# print(scores.count(85))
# print(scores.index(95))
# scores.append(100)
# scores.remove(60)
# print(scores)
# 18. Имена студентов
# students = ["Ali", "John", "Said", "Ali", "Karim"]
# Узнай количество "Ali".
# Найди индекс "Said".
# Добавь "Muhammad" в конец.
# Вставь "Rustam" на индекс 2.
# Удали первое "Ali".
# students = ["Ali", "John", "Said", "Ali", "Karim"]
# print(students.count("Ali"))
# print(students.index("Said"))
# students.append("Muhammad")
# students.insert(2,"Rustam")
# students.remove("Ali")
# print(students)
# 19. Очередь клиентов
# queue = ["Client1", "Client2", "Client3", "Client4"]
# Удали первого клиента через pop().
# Добавь "Client5" через append().
# Добавь "Client6" и "Client7" через extend().
# Вставь "VIP" в начало.
# Удали "Client3".
# queue = ["Client1", "Client2", "Client3", "Client4"]
# queue.pop(0)
# queue.append("Client5")
# queue.extend(["Client6","Client7"])
# queue.insert(0,"VIP")
# print(queue)
# 20. Цены товаров
# prices = [120, 450, 300, 150, 450, 200]
# Узнай количество цены 450.
# Найди индекс цены 300.
# Добавь 500.
# Удали 120.
# Отсортируй цены по возрастанию.
# prices = [120, 450, 300, 150, 450, 200]
# print(prices.count(450))
# print(prices.index(300))
# prices.append(500)
# prices.pop(0)
# print(prices)
# 21. Языки программирования
# languages = ["Python", "C++", "Java"]
# Добавь "Go" в конец.
# Добавь "Rust" и "JavaScript" через extend().
# Вставь "C" на индекс 1.
# Удали "Java".
# Разверни список через reverse().
# languages = ["Python", "C++", "Java"]
# languages.extend("Go")
# languages.extend(["Rust" , "JavaScript"])
# languages.insert(1,"C")
# languages.remove("Java")
# languages.reverse()
# print(languages)
# 22. Копия списка
# numbers = [10, 20, 30, 40, 50]
# Создай копию через copy().
# Добавь 60 в копию.
# Удали 20 из копии.
# Отсортируй копию.
# Выведи оригинал и копию и сравни их.
# numbers = [10, 20, 30, 40, 50]
# numbers2=numbers.copy()
# numbers2.append(60)
# numbers2.pop(1)
# numbers2.sort()
# print(numbers2)
# 23. Корзина интернет-магазина
# cart = ["phone", "mouse", "keyboard"]
# Добавь "monitor".
# Добавь "headphones" и "webcam".
# Вставь "laptop" на индекс 0.
# Удали "mouse".
# Удали последний товар через pop().
# cart = ["phone", "mouse", "keyboard"]
# cart.append("monitor")
# cart.extend(["headphones" , "webcam"])
# cart.remove("mouse")
# cart.pop(-1)
# print(cart)
# 24. Номера
# numbers = [5, 10, 15, 10, 20, 10]
# Посчитай количество 10.
# Найди индекс первого 20.
# Добавь 25.
# Удали одно число 10.
# Отсортируй список по убыванию.
# numbers = [5, 10, 15, 10, 20, 10]
# print(numbers.count(10))
# print(numbers.index(20))
# numbers.append(25)
# numbers.remove(10)
# numbers.sort()
# print(numbers)
# 25. Игроки
# players = ["Messi", "Ronaldo", "Neymar", "Mbappe"]
# Добавь "Haaland".
# Вставь "Salah" на индекс 2.
# Удали "Neymar".
# Найди индекс "Ronaldo".
# Разверни список.
# players = ["Messi", "Ronaldo", "Neymar", "Mbappe"]
# players.append("Haaland")
# players.insert(2,"Salah")
# players.remove("Neymar")
# print(players.index("Ronaldo"))
# players.reverse()
# print(players)
# 26. Задачи Todo
# tasks = ["study", "work", "sleep"]
# Добавь "exercise".
# Добавь "read" и "code".
# Вставь "eat" на индекс 1.
# Удали "sleep".
# Отсортируй список.
# tasks = ["study", "work", "sleep"]
# tasks.append("exercise")
# tasks.extend(["read" , "code"])
# tasks.pop(-1)
# tasks.sort()
# print(tasks)
# 27. Температура
# temperatures = [25, 30, 28, 25, 32, 25]
# Посчитай количество 25.
# Найди индекс 32.
# Добавь 35.
# Удали одну 28.
# Отсортируй список по возрастанию.
# temperatures = [25, 30, 28, 25, 32, 25]
# print(temperatures.count(25))
# print(temperatures.index(32))
# temperatures.append(35)
# temperatures.remove(28)
# temperatures.sort()
# print(temperatures)
# 28. Города
# cities = ["Dushanbe", "Khujand", "Bokhtar"]
# Добавь "Kulob".
# Добавь "Tursunzoda" и "Istaravshan".
# Вставь "Hisor" на индекс 1.
# Удали "Bokhtar".
# Разверни список.
# cities = ["Dushanbe", "Khujand", "Bokhtar"]
# cities.append("Kulob")
# cities.extend(["Tursunzoda" , "Istaravshan"])
# cities.insert(1,"Hisor")
# cities.remove("Bokhtar")
# cities.reverse()
# print(cities)
# 29. Работники
# employees = ["Ali", "Said", "John", "Karim"]
# Добавь "Rustam".
# Вставь "Muhammad" на индекс 2.
# Найди индекс "John".
# Удали "Said".
# Создай копию списка через copy().
# employees = ["Ali", "Said", "John", "Karim"]
# employees.append("Rustam")
# employees.insert(2,"Muhammad")
# print(employees.index("John"))
# employees.pop(1)
# employees2=employees.copy()
# print(employees2)
# 30. Числа и копия
# numbers = [9, 3, 7, 3, 5, 3]
# Создай копию списка.
# Посчитай количество 3 в оригинале.
# Добавь 10 в копию.
# Удали одну 3 из копии.
# Отсортируй копию.
# numbers = [9, 3, 7, 3, 5, 3]
# numbers2=numbers.copy()
# print(numbers.count(3))
# numbers2.append(10)
# numbers2.remove(3)
# numbers2.sort()
# print(numbers2)
# print(numbers)
# 31. Музыка
# songs = ["Song A", "Song B", "Song C", "Song A"]
# Посчитай количество "Song A".
# Найди индекс "Song C".
# Добавь "Song D".
# Вставь "Song E" на индекс 1.
# Удали одну "Song A".
# songs = ["Song A", "Song B", "Song C", "Song A"]
# print(songs.count("Song A"))
# print(songs.index("Song C"))
# songs.append("Song D")
# songs.insert(1,"Song E")
# songs.remove("Song A")
# print(songs)
# 32. Очередь заказов
# orders = [101, 102, 103, 104]
# Удали первый заказ через pop().
# Добавь заказ 105.
# Добавь заказы 106 и 107.
# Вставь заказ 100 в начало.
# Отсортируй список.
# orders = [101, 102, 103, 104]
# orders.pop(0)
# orders.append(105)
# orders.extend([106 , 107])
# orders.insert(0,100)
# print(orders)
# 33. Рейтинг
# rating = [5, 4, 3, 5, 2, 5, 4]
# Посчитай количество 5.
# Найди индекс 2.
# Добавь 1.
# Удали одну оценку 3.
# Отсортируй список по убыванию.
# rating = [5, 4, 3, 5, 2, 5, 4]
# print(rating.count(5))
# print(rating.index(2))
# rating.append(1)
# rating.remove(3)
# rating.sort()
# print(rating)
# 34. Инвентарь
# inventory = ["laptop", "phone", "tablet"]
# Добавь "monitor".
# Добавь "mouse" и "keyboard".
# Вставь "printer" на индекс 2.
# Удали "tablet".
# Удали последний элемент через pop().
# inventory = ["laptop", "phone", "tablet"]
# inventory.append("monitor")
# inventory.extend(["mouse" , "keyboard"])
# inventory.insert(2,"printer")
# inventory.remove("tablet")
# inventory.pop(-1)
# print(inventory)
# 35. Полная очистка
# data = [10, 20, 30, 40, 50]
# Создай копию через copy().
# Добавь 60 в копию.
# Удали 30 из копии.
# Разверни копию.
# Полностью очисти оригинальный список через clear().
# data = [10, 20, 30, 40, 50]
# data2 = data.copy()
# data2.append(60)
# data2.remove(30)
# data2.reverse()
# data.clear()
# print(data)
# print(data2)