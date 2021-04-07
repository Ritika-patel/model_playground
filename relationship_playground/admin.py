from django.contrib import admin
from django.db import models
from relationship_playground import models

# Register your models here.

admin.site.register([
    models.Article,
    models.Author
])