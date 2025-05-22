"""
Initialisierung der Flask-Anwendung
"""
from flask import Flask
from app.config import Config, ProductionConfig
import os

def create_app(config_class=Config):
    """
    Fabrikmethode zur Erstellung der Flask-Anwendung
    """
    # Wir verwenden jetzt interne app-Ordner
    app = Flask(__name__)
                
    app.config.from_object(config_class)
    
    # Upload-Ordner erstellen, falls er nicht existiert
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Registrierung von Routen aus den Controllern
    from app.controllers.main_controller import main_bp
    from app.controllers.form_controller import form_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(form_bp)
    
    return app

# Создаем экземпляр приложения по умолчанию для Gunicorn
app = create_app(ProductionConfig) 