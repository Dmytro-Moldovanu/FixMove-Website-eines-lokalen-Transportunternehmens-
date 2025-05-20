import os
import re

# Соответствия старых и новых путей к файлам
replacements = {
    # Файлы изображений
    'images/фон.jpg': 'images/Hintergrund.jpg',
    'images/maps.jpg': 'images/Karte.jpg',
    'images/машина1.jpg': 'images/Fahrzeug1.jpg',
    'images/машина2.png': 'images/Fahrzeug2.png',
    'images/чистота машины и вспомогательные девайсы.png': 'images/Sauberes_Fahrzeug_und_Zubehoer.png',
    'images/транспортировка мотоцикла 1.jpg': 'images/Motorradtransport1.jpg',
    'images/транспортировка мотоцикла 3.jpg': 'images/Motorradtransport3.jpg',
    'images/транспортировка мотоцикла 4.jpg': 'images/Motorradtransport4.jpg',
    'images/транспортировка мотоцикла 5.jpg': 'images/Motorradtransport5.jpg',
    
    # Файлы в Motorradausruestung
    'images/оборудование мотоциклы/крепление переднее картинка.jpg': 'images/Motorradausruestung/Vordere_Befestigung_Bild.jpg',
    'images/оборудование мотоциклы/рампа.jpg': 'images/Motorradausruestung/Rampe.jpg',
    'images/оборудование мотоциклы/крепление зааднее.jpg': 'images/Motorradausruestung/Hintere_Befestigung.jpg',
    'images/оборудование мотоциклы/крепление переднее фото.jpg': 'images/Motorradausruestung/Vordere_Befestigung_Foto.jpg',
    
    # Файлы в Umzug
    'images/Umzug/транспортировка мебели 2.jpg': 'images/Umzug/Moebeltransport2.jpg',
    'images/Umzug/транспортировка мебели 3.jpeg': 'images/Umzug/Moebeltransport3.jpeg',
    'images/Umzug/ящики, надёжно.jpg': 'images/Umzug/Sichere_Boxen.jpg',
    'images/Umzug/транспортировка большого груза.jpg': 'images/Umzug/Grossfrachttransport.jpg',
    
    # SVG файлы
    'images/Stickers/undraw_traveling_c18z.svg': 'images/Aufkleber/Reisen.svg',
    'images/Stickers/undraw_best-place_dhzp.svg': 'images/Aufkleber/Bester_Ort.svg',
    'images/Stickers/undraw_learning_qt7d.svg': 'images/Aufkleber/Lernen.svg',
    'images/Stickers/undraw_my-location_dcug.svg': 'images/Aufkleber/Mein_Standort.svg',
    'images/Stickers/undraw_vintage_q09n.svg': 'images/Aufkleber/Vintage.svg'
}

# Путь к HTML-файлу
html_file = os.path.join('app', 'templates', 'index.html')

# Чтение HTML-файла
with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Обработка файла
for old_path, new_path in replacements.items():
    pattern = f'static\', filename=\'({old_path})'
    replacement = f'static\', filename=\'{new_path}'
    content = re.sub(pattern, replacement, content)

# Запись обновленного HTML-файла
with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"HTML-файл {html_file} обновлен с новыми путями к файлам.") 