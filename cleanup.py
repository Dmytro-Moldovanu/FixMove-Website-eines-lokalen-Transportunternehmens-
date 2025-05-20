import os
import shutil

# Основной путь к изображениям
image_path = os.path.join('app', 'static', 'images')

# Файлы для удаления (с кириллическими названиями)
files_to_remove = [
    'maps.jpg',
    'deny-hill-L6bSCwg_gT8-unsplash.jpg',
    'общие размеры машины.jpg',
    'машина1.jpg',
    'транспортировка мотоцикла 1.jpg',
    'транспортировка мотоцикла 5.jpg',
    'транспортировка мотоцикла 4.jpg',
    'транспортировка мотоцикла 3.jpg',
    'чистота машины и вспомогательные девайсы.png',
    'машина2.png',
    'фон.jpg'
]

# Папки для удаления
folders_to_remove = [
    'оборудование мотоциклы',
    'Stickers'
]

# Удаление файлов
for file_name in files_to_remove:
    file_path = os.path.join(image_path, file_name)
    if os.path.exists(file_path):
        try:
            os.remove(file_path)
            print(f"Удален файл {file_path}")
        except Exception as e:
            print(f"Ошибка при удалении файла {file_path}: {e}")

# Удаление папок
for folder_name in folders_to_remove:
    folder_path = os.path.join(image_path, folder_name)
    if os.path.exists(folder_path):
        try:
            shutil.rmtree(folder_path)
            print(f"Удалена папка {folder_path}")
        except Exception as e:
            print(f"Ошибка при удалении папки {folder_path}: {e}")

print("Очистка завершена") 