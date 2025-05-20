import os

# Путь к директории
motorrad_dir = os.path.join('app', 'static', 'images', 'Motorradausruestung')

# Файлы, которые нужно создать
files_to_create = [
    'Vordere_Befestigung_Foto.jpg',
    'Vordere_Befestigung_Bild.jpg',
    'Rampe.jpg'
]

# Создаем пустые файлы (можно использовать для отладки)
for file_name in files_to_create:
    file_path = os.path.join(motorrad_dir, file_name)
    if not os.path.exists(file_path):
        # Создаем пустой файл минимального размера
        with open(file_path, 'wb') as f:
            # Записываем минимальные данные для JPEG
            f.write(b'\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46\x00\x01\x01\x01\x00\x48\x00\x48\x00\x00\xFF\xDB\x00\x43\x00\xFF\xC0\x00\x11\x08\x00\x01\x00\x01\x03\x01\x22\x00\xFF\xC4\x00\x1F\x00\xFF\xDA\x00\x0C\x03\x01\x00\x02\x11\x03\x11\x00\x3F\x00\xFF\xD9')
        print(f'Создан файл {file_path}')
    else:
        print(f'Файл {file_path} уже существует')

print('Файлы созданы!') 