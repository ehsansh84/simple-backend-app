from handlers.handlers import Product
from handlers.upload import Upload

url_patterns = [
    ("/v1/product", Product, None, "product"),
    ("/v1/upload", Upload, None, "upload"),
]
