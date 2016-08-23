from django.db.utils import IntegrityError
from rest_framework.views import exception_handler as drf_exception_handler
from .exceptions import Conflict

def exception_handler(exc, context):
	if isinstance(exc, IntegrityError):
		exc = Conflict()

	return drf_exception_handler(exc, context)
