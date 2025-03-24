# Импорт функций render и get_object_or_404 из django.shortcuts.
# - render: используется для рендеринга HTML-шаблонов с передачей контекста.
# - get_object_or_404: используется для получения объекта из базы данных или вызова ошибки 404, если объект не найден.
from django.shortcuts import render, get_object_or_404

# Импорт моделей из текущего приложения (файл models.py).
# Эти модели представляют данные, с которыми будут работать представления (views).
from .models import Work, Service, MainPage, PageService, PageWork


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
    main_page = MainPage.objects.first()
    services = Service.objects.all()
    works = Work.objects.all()
    latest_works = Work.objects.all().order_by('id')
    return render(request, 'main/home.html', {

        'main_page': main_page,
        'services': services,
        'works': works,
        'latest_works': latest_works,

    })

def service_detail(request, service_id):
    """
    Функция service_detail отображает детальную страницу для конкретной услуги.

    Аргументы:
        - request: Объект запроса.
        - service_id: ID услуги, которую нужно отобразить.

    Контекст:
        - service: Объект услуги, найденный по ID.
        - latest_works: Все работы, отсортированные по ID.
        - services_page (PageService): Данные страницы услуг

    Возвращает:
        HttpResponse: Рендерит шаблон 'main/service_detail.html' с переданным контекстом.
    """
    service = get_object_or_404(Service, id=service_id)
    latest_works = Work.objects.all().order_by('id')
    services_page = PageService.objects.first()
    return render(request, 'main/service_detail.html', {'service': service, 'latest_works': latest_works, 'services_page': services_page,})


def all_services(request):
    """
    Функция all_services отображает страницу со всеми услугами.

    Контекст:
        - service2: Все услуги из модели Service.
        - latest_works: Все работы, отсортированные по ID.
        - services_page (PageService): Данные страницы услуг

    Возвращает:
        HttpResponse: Рендерит шаблон 'main/all_Services.html' с переданным контекстом.
    """
    service2 = Service.objects.all()
    latest_works = Work.objects.all().order_by('id')
    services_page = PageService.objects.first()
    return render(request, 'main/all_Services.html', {'service2': service2, 'latest_works': latest_works, 'services_page': services_page, })


def work_detail(request, work_id):
    """
    Функция work_detail отображает детальную страницу для конкретной работы.

    Аргументы:
        - request: Объект запроса.
        - work_id: ID работы, которую нужно отобразить.

    Контекст:
        - work: Объект работы, найденный по ID.
        - latest_works: Все работы, отсортированные по ID.
        - page_work (PageWork): Данные страницы работ

    Возвращает:
        HttpResponse: Рендерит шаблон 'main/work_detail.html' с переданным контекстом.
    """
    latest_works = Work.objects.all().order_by('id')
    work = get_object_or_404(Work, id=work_id)
    page_work = PageWork.objects.first()
    return render(request, 'main/work_detail.html', {'work': work, 'latest_works': latest_works, 'page_work': page_work,})


def all_works(request):
    """
    Функция all_works отображает страницу со всеми работами.

    Контекст:
        - work2: Все работы из модели Work.
        - latest_works: Все работы, отсортированные по ID.
        - page_work (PageWork): Данные страницы работ

    Возвращает:
        HttpResponse: Рендерит шаблон 'main/all_works.html' с переданным контекстом.
    """
    latest_works = Work.objects.all().order_by('id')
    work2 = Work.objects.all()
    page_work = PageWork.objects.first()
    return render(request, 'main/all_works.html', {'work2': work2, 'latest_works': latest_works, 'page_work': page_work,})

