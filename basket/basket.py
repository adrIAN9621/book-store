from store.models import Product


class Basket():
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product):
        """
        Add and update the basket
        """
        product_id = product.id
        if product_id not in self.basket:
            self.basket[product_id] = {'price': str(product_id.price)}
        
        self.session.modified = True