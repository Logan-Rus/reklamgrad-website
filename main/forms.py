# Импорт модуля forms из Django для создания форм
from django import forms
# Импорт модели ContactRequest для привязки формы к модели
from .models import ContactRequest

class ContactForm(forms.ModelForm):
    """
       Форма для обработки контактных запросов.
       Наследуется от ModelForm для автоматического создания формы на основе модели ContactRequest.

       Поля формы:
       - name: имя отправителя (CharField)
       - email: email отправителя (EmailField)
       - phone: телефон отправителя (CharField)
       - message: текст сообщения (TextField)
    """
    class Meta:
        model = ContactRequest
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }