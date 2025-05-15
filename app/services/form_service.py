"""
Сервис для обработки данных форм
"""
from typing import Dict, Any, List
from app.models.form_data import ContactFormData


class FormService:
    """
    Сервис для обработки данных форм
    """
    
    @staticmethod
    def process_form_data(form_data: ContactFormData) -> bool:
        """
        Обрабатывает данные формы, например сохраняет в базу данных
        или отправляет уведомление
        
        Args:
            form_data: Данные из формы
            
        Returns:
            bool: Результат обработки
        """
        # Здесь можно реализовать:
        # - сохранение в базу данных
        # - отправку email уведомления
        # - логирование
        # и т.д.
        
        # Временная заглушка для проверки
        print(f"Получены данные от {form_data.name} ({form_data.phone})")
        print(f"Перевозка от {form_data.pickup_address} до {form_data.delivery_address}")
        print(f"Дата и время: {form_data.pickup_date} {form_data.pickup_time}")
        
        # В реальном приложении здесь будет настоящая бизнес-логика
        return True 