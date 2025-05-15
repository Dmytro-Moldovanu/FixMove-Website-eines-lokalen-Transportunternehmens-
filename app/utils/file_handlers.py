"""
Утилиты для обработки загружаемых файлов
"""
import os
import uuid
from typing import List, Tuple
from werkzeug.datastructures import FileStorage

def save_uploaded_files(files: List[FileStorage], upload_folder: str) -> List[str]:
    """
    Сохраняет загруженные файлы в указанную директорию
    
    Args:
        files: Список загруженных файлов
        upload_folder: Путь к директории для сохранения файлов
        
    Returns:
        List[str]: Список путей к сохраненным файлам
    """
    uploaded_file_paths = []
    
    # Создаем директорию, если она не существует
    os.makedirs(upload_folder, exist_ok=True)
    
    for file in files:
        if file and file.filename:
            # Генерируем уникальное имя файла, чтобы избежать конфликтов
            filename = str(uuid.uuid4()) + "_" + file.filename
            file_path = os.path.join(upload_folder, filename)
            try:
                file.save(file_path)
                uploaded_file_paths.append(file_path)
            except Exception as e:
                print(f"Ошибка при сохранении файла {filename}: {str(e)}")
    
    return uploaded_file_paths


def validate_file(file: FileStorage, allowed_extensions: List[str] = None) -> Tuple[bool, str]:
    """
    Проверяет загруженный файл на корректность
    
    Args:
        file: Загруженный файл
        allowed_extensions: Список разрешенных расширений файлов
        
    Returns:
        Tuple[bool, str]: (результат проверки, сообщение об ошибке)
    """
    if not file or not file.filename:
        return False, "Файл не выбран"
    
    if allowed_extensions:
        extension = file.filename.rsplit('.', 1)[1].lower() if '.' in file.filename else ""
        if extension not in allowed_extensions:
            return False, f"Недопустимый формат файла. Разрешены только: {', '.join(allowed_extensions)}"
    
    return True, "" 