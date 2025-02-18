
class ConfigDebug():
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:password@localhost/shop20220128'    # File-based SQL database
    SECRET_KEY = 'SDFA11#'

 # Flask-Mail SMTP server settings
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 1025
    MAIL_USE_TLS = False
    MAIL_USE_SSL = False
    MAIL_USERNAME = None
    MAIL_PASSWORD = None
    MAIL_DEFAULT_SENDER = 'noreply@StefansSupershop.com'

    # Flask-User settingsa
    USER_APP_NAME = "Flask-User Basic App"      # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = True        # Enable email aution
    USER_ENABLE_USERNAME = False    # Disable username authentication
    USER_EMAIL_SENDER_NAME = USER_APP_NAME
    USER_EMAIL_SENDER_EMAIL = "noreply@example.com"    

    SECURITY_PASSWORD_SALT = "341231232"


    