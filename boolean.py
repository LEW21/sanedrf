from django.forms.widgets import Select
from django.forms.fields import NullBooleanField
from django_filters import Filter
from django.utils.translation import ugettext_lazy as _

class BooleanSelect(Select):
	"""
	A Select Widget intended to be used with NullBooleanField.
	"""
	def __init__(self, attrs=None):
		choices = (
			('', _('---')),
			('0', _('No')),
			('1', _('Yes')),
		)
		super().__init__(attrs, choices)

	def render(self, name, value, attrs=None):
		try:
			value = {True: '1', False: '0', '1': '1', '0': '0', 'true': '1', 'false': '0'}[value]
		except KeyError:
			value = ''
		return super().render(name, value, attrs)

	def value_from_datadict(self, data, files, name):
		value = data.get(name)
		return {
			'1': True,
			True: True,
			'True': True,
			'true': True,
			'0': False,
			False: False,
			'False': False,
			'false': False,
		}.get(value, None)

class BooleanField(NullBooleanField):
	widget = BooleanSelect

	def validate(self, value):
		if value is None and self.required:
			raise ValidationError(self.error_messages['required'], code='required')

class BooleanFilter(Filter):
    field_class = BooleanField
