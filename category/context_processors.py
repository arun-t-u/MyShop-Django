from .models import Category

def menu_links(request):
    links = Category.objects.all()
    print(dict(links=links))
    return dict(links=links)