from django.shortcuts import render, get_object_or_404

from .models import Category, Product


def categories(request):
    return{
        'categories' : Category.objects.all()
        }
def all_products(request):
    product = Product.objects.all()
    return render(request, 'store/home.html', {'product' : product}) 



def products_detail(request, slug):
     product = get_object_or_404(Product, slug=slug, in_stock=True)
     return render(request, 'store/products/detail.html', {'products' : product})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    product = Product.objects.filter(category=category)
    return render(request, 'store/products/category.html', {'category' : category, 'products': product})

class SearchView(Product):
    model = products_detail
    template_name = 'search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = products_detail.objects.filter(title__contains=query)
          result = postresult
       else:
           result = None
       return result    