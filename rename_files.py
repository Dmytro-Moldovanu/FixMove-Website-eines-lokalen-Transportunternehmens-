import os
import shutil

# Переименование папок
folder_mapping = {
    'оборудование мотоциклы': 'Motorradausruestung',
    'Stickers': 'Aufkleber'
}

# Переименование файлов в корне images
files_mapping = {
    'maps.jpg': 'Karte.jpg',
    'deny-hill-L6bSCwg_gT8-unsplash.jpg': 'Stadtbild.jpg',
    'общие размеры машины.jpg': 'Fahrzeug_Abmessungen.jpg',
    'машина1.jpg': 'Fahrzeug1.jpg',
    'транспортировка мотоцикла 1.jpg': 'Motorradtransport1.jpg',
    'транспортировка мотоцикла 5.jpg': 'Motorradtransport5.jpg',
    'транспортировка мотоцикла 4.jpg': 'Motorradtransport4.jpg',
    'транспортировка мотоцикла 3.jpg': 'Motorradtransport3.jpg',
    'чистота машины и вспомогательные девайсы.png': 'Sauberes_Fahrzeug_und_Zubehoer.png',
    'машина2.png': 'Fahrzeug2.png',
    'фон.jpg': 'Hintergrund.jpg'
}

# Переименование файлов в папке Motorradausruestung
motorrad_files_mapping = {
    'крепление зааднее.jpg': 'Hintere_Befestigung.jpg',
    'рампа.jpg': 'Rampe.jpg',
    'крепление переднее фото.jpg': 'Vordere_Befestigung_Foto.jpg',
    'крепление переднее картинка.jpg': 'Vordere_Befestigung_Bild.jpg'
}

# Переименование файлов в папке Umzug
umzug_files_mapping = {
    'транспортировка большого груза.jpg': 'Grossfrachttransport.jpg',
    'транспортировка мебели 3.jpeg': 'Moebeltransport3.jpeg',
    'транспортировка мебели.jpg': 'Moebeltransport.jpg',
    'ящики, надёжно.jpg': 'Sichere_Boxen.jpg',
    'транспортировка мебели 2.jpg': 'Moebeltransport2.jpg'
}

# Переименование SVG файлов
svg_files_mapping = {
    'undraw_best-place_dhzp.svg': 'Bester_Ort.svg',
    'undraw_learning_qt7d.svg': 'Lernen.svg',
    'undraw_my-location_dcug.svg': 'Mein_Standort.svg',
    'undraw_traveling_c18z.svg': 'Reisen.svg',
    'undraw_vintage_q09n.svg': 'Vintage.svg'
}

# Основной путь к изображениям
image_path = os.path.join('app', 'static', 'images')

# Функция для обработки переименования файлов
def rename_files_in_dir(directory, mapping):
    for old_name, new_name in mapping.items():
        old_path = os.path.join(directory, old_name)
        new_path = os.path.join(directory, new_name)
        if os.path.exists(old_path):
            # Если файл с новым именем уже существует, сохраняем копию
            if os.path.exists(new_path):
                print(f"Файл {new_path} уже существует, создаю копию")
            else:
                try:
                    shutil.copy2(old_path, new_path)
                    print(f"Файл {old_name} скопирован в {new_name}")
                except Exception as e:
                    print(f"Ошибка при копировании {old_name}: {e}")

# Создаем папки, если не существуют
for folder_name in ['Motorradausruestung', 'Aufkleber']:
    folder_path = os.path.join(image_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Создана папка {folder_path}")

# Копируем и переименовываем файлы в корневой папке изображений
rename_files_in_dir(image_path, files_mapping)

# Копируем и переименовываем файлы в папке Motorradausruestung
motorrad_dir = os.path.join(image_path, 'Motorradausruestung')
old_motorrad_dir = os.path.join(image_path, 'оборудование мотоциклы')
rename_files_in_dir(old_motorrad_dir, motorrad_files_mapping)

# Копируем и переименовываем файлы в папке Umzug
umzug_dir = os.path.join(image_path, 'Umzug')
rename_files_in_dir(umzug_dir, umzug_files_mapping)

# Копируем и переименовываем SVG файлы
stickers_dir = os.path.join(image_path, 'Stickers')
aufkleber_dir = os.path.join(image_path, 'Aufkleber')
rename_files_in_dir(stickers_dir, svg_files_mapping)

print("Переименование файлов завершено") 