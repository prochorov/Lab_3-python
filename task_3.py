import os


def rename_files(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)

        # Открываем файл в бинарном режиме и считываем первые 8 байт
        with open(file_path, 'rb') as f:
            signature = f.read(8)

        # Проверяем сигнатуру файла
        if signature.startswith(b'\xFF\xD8\xFF'):
            new_name = file + '.jpg'
        elif signature.startswith(b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'):
            new_name = file + '.png'
        elif signature.startswith(b'\x25\x50\x44\x46\x2D'):
            new_name = file + '.pdf'
        elif signature.startswith(b'\x4F\x54\x54\x4F'):
            new_name = file + '.otf'
        elif signature.startswith(b'\x52\x61\x72\x21\x1A\x07'):
            new_name = file + '.rar'
        elif signature.startswith(b'\x37\x7A\xBC\xAF\x27\x1C'):
            new_name = file + '.7z'
        elif signature.startswith(b'\x50\x4B'):
            new_name = file + '.zip'
        elif signature.startswith(b'\xFF\xFE'):
            new_name = file + '.pdf'
        else:
            # Неизвестный тип файла, не меняем имя
            new_name = file
            print('Неизвестный тип файла!')

        # Переименовываем файл
        os.rename(file_path, os.path.join(path, new_name))


# Пример использования:
rename_files('D:/институт/Питон/Lab_3/lab3_files/BinaryFiles')
