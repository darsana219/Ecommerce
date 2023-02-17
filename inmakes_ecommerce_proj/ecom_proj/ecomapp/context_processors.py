from .models import Category

# to store all links of category
def menu_links(request):
    link = Category.objects.all()
    return dict(links=link)