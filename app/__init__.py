from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()  # Загрузка переменных окружения

def create_app():
    app = Flask(__name__)
    app.secret_key = os.getenv('SECRET_KEY', os.urandom(24).hex())

    # Конфигурация приложения
    app.config['TELEGRAM_BOT_TOKEN'] = os.getenv('TELEGRAM_BOT_TOKEN')
    app.config['TELEGRAM_CHAT_ID'] = os.getenv('TELEGRAM_CHAT_ID')
    app.config['DATABASE'] = 'instance/applications.db'
    app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
    app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', 587))
    app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
    app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
    app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'true').lower() == 'true'
    app.config['ADMIN_EMAIL'] = os.getenv('ADMIN_EMAIL')
    app.config['SUBMISSION_LIMIT_MINUTES'] = 15

    # Импорт и регистрация модулей
    from . import models, routes
    models.init_app(app)
    routes.init_app(app)

    return app