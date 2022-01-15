from .models import Category

def menu_links(request):
    links = Category.objetcs.all()
    return dict(links = links)