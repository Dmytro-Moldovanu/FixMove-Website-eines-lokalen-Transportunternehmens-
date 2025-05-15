"""
Контроллер для обработки отправленных форм
"""
from flask import Blueprint, request, current_app, redirect, url_for, flash, render_template
from app.models.form_data import ContactFormData
from app.utils.file_handlers import save_uploaded_files
from app.services.form_service import FormService

# Создаем Blueprint для обработки форм
form_bp = Blueprint('form', __name__)

@form_bp.route('/submit', methods=['POST'])
def submit():
    """
    Обработчик отправки формы
    
    Returns:
        str: Сообщение об успешной отправке
    """
    if request.method == 'POST':
        # Получаем данные формы
        name = request.form.get('name')
        phone = request.form.get('phone')
        description = request.form.get('description')
        pickup_address = request.form.get('pickup_address')
        delivery_address = request.form.get('delivery_address')
        pickup_date = request.form.get('pickup_date')
        pickup_time = request.form.get('pickup_time')
        loader = bool(request.form.get('loader'))
        notes = request.form.get('notes')
        
        # Обрабатываем загруженные файлы
        photos = request.files.getlist('photos')
        uploaded_files = save_uploaded_files(photos, current_app.config['UPLOAD_FOLDER'])
        
        # Создаем объект данных формы
        form_data = ContactFormData(
            name=name,
            phone=phone,
            description=description,
            pickup_address=pickup_address,
            delivery_address=delivery_address,
            pickup_date=pickup_date,
            pickup_time=pickup_time,
            loader=loader,
            notes=notes,
            photo_paths=uploaded_files
        )
        
        # Обрабатываем данные формы через сервисный слой
        success = FormService.process_form_data(form_data)
        
        if success:
            return 'Anfrage erfolgreich gesendet!'
        else:
            return 'Bei der Bearbeitung Ihrer Anfrage ist ein Fehler aufgetreten. Bitte versuchen Sie es später erneut.' 