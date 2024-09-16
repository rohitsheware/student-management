from django.apps import AppConfig


class StudentManagementSystemAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "student_management_system_app"


class YourAppConfig(AppConfig):
    name = "student_management_system_app"

    def ready(self):
        import student_management_system_app.signals  # Import the signals module
