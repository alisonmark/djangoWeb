import os
import django
from Book.models import Book, Category

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoWebsite.settings")
django.setup()
print(DJANGO_SETTINGS_MODULE)

# Hiển thị tất cả các record có trong DB
print('==================All Records inDB==================')
Category.objects.all()
