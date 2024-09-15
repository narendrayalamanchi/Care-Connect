from django.apps import AppConfig



class Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'receiptionist'
    
    def ready(self):
        import receiptionist.signals  
