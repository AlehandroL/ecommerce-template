from store.models import Product

class Basket():
    """
    A base Basket class, providing some default behaviors that can be 
    inherited or overrided, as necesary.
    """


    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket


    def add(self, product, product_qty):
        """
        Adding and updating the users basket session data
        """
        product_id = str(product.id)
        
        if product_id not in self.basket:
            self.basket[product_id] = {'price': int(product.price), 'product_qty': int(product_qty)}
        else:
            self.basket[product_id]['product_qty'] = product_qty
        
        self.session.modified = True


    def __len__(self):
        """
        Get the basket data and count the qty of items
        """
        return sum(item['product_qty'] for item in self.basket.values())


    def __iter__(self):
        """
        This iter function returns an iterator for the Basket object
        Collect the product_id in the session data to query the database and return products
        """
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()
        
        for product in products:
            basket[str(product.id)]['product'] = product
        
        for item in basket.values():
            item['total_price'] = int(item['price']) * int(item['product_qty'])
            yield item


    def get_total_price(self):
        return sum(int(item['price'])*int(item['product_qty']) for item in self.basket.values())

    def delete(self, product):
        """
        Deleting a product from session data
        """
        product_id = str(product.id)
        
        if product_id in self.basket:
            del self.basket[product_id]
            self.session.modified = True

    def update(self, product, product_qty):
        """
        Adding and updating the users basket session data
        """
        product_id = str(product.id)
        price = product.price
        self.basket[str(product_id)] = {'product_qty': int(product_qty), 'price':price}
        
        self.session.modified = True
