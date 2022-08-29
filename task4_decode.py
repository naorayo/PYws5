def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        # Если символ - число
        if char.isdigit():
            # присоединяем его к счетчику
            count += char
        else:
            # Иначе (если символ НЕ число
            # печатаем необходимое количество символов
            # в расшифровку
            decode += char * int(count)
            count = ''
    return decode


decoded_val = rle_decode('4W4A4S4D4E4R4T4Y6E9R8T16U')
print(decoded_val)
with open("decode.txt", "a") as file:
    file.write(f'{decoded_val}\n')
