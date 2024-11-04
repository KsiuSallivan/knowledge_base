running = True

while running:
    word = input("Введите слово (или 'exit' для выхода): ")

    if word == 'exit': # Если пользователь ввел "exit", то выходим из цикла
        running = False
    else:
        reversed_word = word[::-1] # Создаем переменную, которая содержит перевернутое слово
        if word == reversed_word: # Если введенное и перевернутое слова совпадают, выводим сообщение о том, что это палиндром
            print(f"Слово '{word}' - 🎉 палиндром! 🎉")
        else:
            print(f"Слово '{word}' - ❌ не палиндром! ❌")