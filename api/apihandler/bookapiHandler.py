
from piston.handler import BaseHandler, AnonymousBaseHandler
from piston.utils import rc, throttle, validate
from django.core.exceptions import ObjectDoesNotExist

import logging
from api.bookapi.models import Book, BookCategory

from api.utility import errorCodes
from api.utility.apiUtility import ApiUtility, Error, Success

class BookApiHandler(BaseHandler):
    allowed_methods = ('GET')
    model = Book
    fields=("id","publish_data", "book_title","name","author")


    @throttle(10, 1*60) # 10 call per minute
    def read(self, request, book_id=None,*args, **kwargs):
        try:
            if "allbook" in request.path:
                return Book.objects.all()

            if "getbook" in request.path:
                return Book.objects.get(pk=book_id)

            return Error(errorCodes.NOT_FOUND, 'request not found').__dict__()
        except ObjectDoesNotExist:
            return Error(errorCodes.BAD_REQUEST, 'bad request').__dict__()



class BookApiCatHandler(BaseHandler):
    allowed_methods = ('GET')
    model = BookCategory
    fields=("id","publish_data", "book_title","name","author")

    def read(self, request,*args, **kwargs):
        try:
            #user = kwargs['cat_id']
            #start = kwargs.get('start', 0)
            return Book.objects.filter(book_cat=BookCategory.objects.get(pk=kwargs['cat_id']))
            #return {"error":"Error"}
        except ObjectDoesNotExist:
            return {"error":"not found"}