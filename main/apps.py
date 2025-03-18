# Импорт класса AppConfig из django.apps.
# AppConfig — это базовый класс для конфигурации приложений в Django.
# Он позволяет настраивать поведение приложения, например, указывать имя приложения
# или тип автоматически создаваемого первичного ключа.
from django.apps import AppConfig

class MainConfig(AppConfig):
    """
    Класс конфигурации для приложения 'main'.

    Атрибуты:
        - default_auto_field (str): Указывает тип автоматически создаваемого первичного ключа.
          По умолчанию используется 'django.db.models.BigAutoField', который представляет
          собой 64-битное целое число.
        - name (str): Имя приложения. Указывает Django, к какому приложению относится
          эта конфигурация. В данном случае это 'main'.
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'