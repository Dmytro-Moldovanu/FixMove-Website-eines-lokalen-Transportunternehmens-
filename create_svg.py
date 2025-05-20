import os

# SVG-файлы, которые нужно создать
svg_files = [
    'Bester_Ort.svg',
    'Lernen.svg',
    'Mein_Standort.svg',
    'Reisen.svg',
    'Vintage.svg'
]

# Путь к папке Aufkleber
aufkleber_dir = os.path.join('app', 'static', 'images', 'Aufkleber')

# Создаем файлы
for svg_file in svg_files:
    file_path = os.path.join(aufkleber_dir, svg_file)
    with open(file_path, 'w') as f:
        f.write(f'<!-- SVG for {svg_file} -->')
    print(f'Создан файл {file_path}')

print('SVG-файлы созданы успешно!') 