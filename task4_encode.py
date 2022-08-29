def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1

    if not data:
        return ''

    for char in data:
        # Если предыдущий и текущий символы
        # не совпадают
        if char != prev_char:
            # то добавляем посчитнное количество символов
            # и сам символ в расшифровку
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            # Иначе инкрементируем счетчик
            # (если символы совпадают)
            count += 1
    else:
        # Завершение расшифровки
        encoding += str(count) + prev_char
        return encoding


with open("encode.txt", "r") as file:
    readfile = file.read()
encoded_val = rle_encode(readfile)
print(encoded_val)
