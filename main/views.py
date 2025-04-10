# Импорт функций render и get_object_or_404 из django.shortcuts.
# - render: используется для рендеринга HTML-шаблонов с передачей контекста.
# - get_object_or_404: используется для получения объекта из базы данных или вызова ошибки 404, если объект не найден.
from django.shortcuts import render, get_object_or_404

from django.http import JsonResponse, HttpResponse, Http404  # Декоратор для ограничения типа запроса
from django.views.decorators.http import require_POST # Класс для возврата JSON-ответов
# Импорт моделей из текущего приложения (файл models.py).
# Эти модели представляют данные, с которыми будут работать представления (views).
from .models import Work, Service, MainPage, ContactRequest, MenuItem, Footer, StaticPage

def static_page_view(request, slug):
    """
    Универсальное представление для отображения статических страниц.

    Параметры:
    - slug (str): уникальный идентификатор страницы

    Возвращает:
    - Рендеринг шаблона static_page.html с контекстом страницы
    - 404 ошибку, если страница не найдена
    """
    try:
        page = StaticPage.objects.get(slug=slug)
    except StaticPage.DoesNotExist:
        raise Http404("Страница не найдена")

    context = {
        'page': page,
    }

    return render(request, 'main/static_page.html', context)

@require_POST  # Разрешаем только POST-запросы
def contact_submit(request):
    """
    Функция для обработки данных контактной формы.

    Принимает POST-запрос с параметрами:
    - email (строка): email пользователя
    - message (строка): текст сообщения

    Возвращает JSON-ответ:
    - При успехе: {'status': 'success'}
    - При ошибке: {'status': 'error', 'message': 'Текст ошибки'} с кодом 400
    """
    email = request.POST.get('email')
    message = request.POST.get('message')

    # Проверяем, что оба поля заполнены
    if not email or not message:
    # Возвращаем ответ об ошибке в JSON-формате
    # status=400 означает "Bad Request" - некорректный запрос
        return JsonResponse(
            {'status': 'error', 'message': 'Заполните все поля!'},
            status=400
        )

    # Сохраняем заявку в базу
    ContactRequest.objects.create(email=email, message=message)

    return JsonResponse({'status': 'success'})

def home(request):
    """
    Функция home отображает главную страницу сайта.

    Получает:
    - Основные данные главной страницы (первый объект MainPage)
    - Все услуги (для блока услуг)
    - Все работы (для блока работ)
    - Последние работы (сортировка по ID)

    Контекст:
       - main_page (MainPage): Данные главной страницы
       - services (QuerySet): Все доступные услуги
       - works (QuerySet): Все работы
       - latest_works (QuerySet): Работы, отсортированные по ID

    """
    works = Work.objects.all()

    return render(request, 'main/home.html', {

        'works': works,

    })


def detail_view(request, object_id, model_name):
    if model_name == 'service':
        obj = get_object_or_404(Service, id=object_id)
        template = 'main/service_detail.html'
    elif model_name == 'work':
        obj = get_object_or_404(Work, id=object_id)
        template = 'main/work_detail.html'
    else:
        raise Http404("Страница не найдена")

    context = {
        'service': obj if model_name == 'service' else None,
        'work': obj if model_name == 'work' else None,
    }
    return render(request, template, context)


def list_view(request, model_name):
    if model_name == 'services':
        template = 'main/all_services.html'
    elif model_name == 'works':
        works = Work.objects.all()
        template = 'main/all_works.html'
    else:
        raise Http404("Страница не найдена")

    context = {
        'works': works if model_name == 'works' else None,
    }
    return render(request, template, context)