from base_handler import BaseHandler


class Product(BaseHandler):
    def init_method(self):
        self.required = {
            'post': ['name']
        }
        self.multilingual = ['field2']
        self.casting['ints'] = ['price']
        self.inputs = {
            'post': ['name', 'price', 'image']
        }
        self.tokenless = True

