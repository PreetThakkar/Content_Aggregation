
def update_db(objects)
	from django.conf import settings
	import django
	from Content_Aggregation.settings import DATABASES, INSTALLED_APPS

	settings.configure(DATABASES=DATABASES, INSTALLED_APPS=INSTALLED_APPS)
	django.setup()

	from Congregate.models import *
	for obj in objects:
		obj.save()
	print("success")