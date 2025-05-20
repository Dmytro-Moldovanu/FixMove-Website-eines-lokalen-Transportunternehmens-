import os
import shutil

# Пути к директориям
images_dir = os.path.join('app', 'static', 'images')
old_motorrad_dir = os.path.join(images_dir, 'оборудование мотоциклы')
motorrad_dir = os.path.join(images_dir, 'Motorradausruestung')
umzug_dir = os.path.join(images_dir, 'Umzug')

# Создаем директорию Motorradausruestung, если ее нет
if not os.path.exists(motorrad_dir):
    os.makedirs(motorrad_dir)
    print(f'Создана директория {motorrad_dir}')

# Файлы, которые должны быть в Motorradausruestung
motorrad_files = {
    'крепление переднее фото.jpg': 'Vordere_Befestigung_Foto.jpg',
    'крепление переднее картинка.jpg': 'Vordere_Befestigung_Bild.jpg',
    'рампа.jpg': 'Rampe.jpg',
    'крепление зааднее.jpg': 'Hintere_Befestigung.jpg'
}

# Копируем недостающие файлы из старой папки (если она существует)
if os.path.exists(old_motorrad_dir):
    for old_name, new_name in motorrad_files.items():
        old_path = os.path.join(old_motorrad_dir, old_name)
        new_path = os.path.join(motorrad_dir, new_name)
        if os.path.exists(old_path) and not os.path.exists(new_path):
            try:
                shutil.copy2(old_path, new_path)
                print(f'Скопирован файл из {old_path} в {new_path}')
            except Exception as e:
                print(f'Ошибка при копировании {old_path}: {e}')
else:
    print(f'Папка {old_motorrad_dir} не существует')

# Удаляем старые файлы с кириллическими названиями из Umzug
old_files_in_umzug = [
    'транспортировка большого груза.jpg',
    'транспортировка мебели 3.jpeg',
    'транспортировка мебели.jpg',
    'ящики, надёжно.jpg',
    'транспортировка мебели 2.jpg'
]

for file_name in old_files_in_umzug:
    file_path = os.path.join(umzug_dir, file_name)
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f'Удален файл {file_path}')
        except Exception as e:
            print(f'Ошибка при удалении {file_path}: {e}')

print('Операция завершена!') 