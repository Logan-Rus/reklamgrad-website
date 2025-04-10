# main/context_processors.py

from .models import MainPage, Service, Work, MenuItem, Footer

def common_context(request):
    return {
        'main_page': MainPage.objects.first(),
        'services': Service.objects.all(),
        'latest_works': Work.objects.all().order_by('id'),
        'menu_items': MenuItem.objects.all().order_by('order'),
        'footer': Footer.load(),
    }