"""
Скрипт настройки проекта
"""
import os
import shutil

def setup_project():
    """
    Копирует шаблоны и статические файлы в соответствующие директории
    """
    print("Настройка проекта...")
    
    # Создаем необходимые директории
    dirs = [
        'app/templates',
        'app/static',
        'app/static/css',
        'app/static/js',
        'app/static/images',
        'app/static/uploads'
    ]
    
    for d in dirs:
        os.makedirs(d, exist_ok=True)
        print(f"Создана директория: {d}")
    
    # Копируем шаблоны
    if os.path.exists('templates'):
        for file in os.listdir('templates'):
            src = os.path.join('templates', file)
            dst = os.path.join('app/templates', file)
            if os.path.isfile(src):
                shutil.copy2(src, dst)
                print(f"Скопирован шаблон: {file}")
    
    # Копируем статические файлы
    if os.path.exists('static'):
        # CSS
        if os.path.exists('static/css'):
            copy_recursive('static/css', 'app/static/css')
        
        # JS
        if os.path.exists('static/js'):
            copy_recursive('static/js', 'app/static/js')
        
        # Images - рекурсивное копирование с подпапками
        if os.path.exists('static/images'):
            copy_recursive('static/images', 'app/static/images')

    print("Настройка завершена!")

def copy_recursive(src_dir, dst_dir):
    """
    Рекурсивно копирует содержимое директории src_dir в dst_dir
    """
    if not os.path.exists(dst_dir):
        os.makedirs(dst_dir)
    
    for item in os.listdir(src_dir):
        src_item = os.path.join(src_dir, item)
        dst_item = os.path.join(dst_dir, item)
        
        if os.path.isdir(src_item):
            copy_recursive(src_item, dst_item)
            print(f"Скопирована директория: {src_item} -> {dst_item}")
        else:
            shutil.copy2(src_item, dst_item)
            print(f"Скопирован файл: {item}")

if __name__ == "__main__":
    setup_project() 