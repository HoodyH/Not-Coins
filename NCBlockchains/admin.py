from django.contrib import admin
from .models import (
    Block,
    Chain,
)


admin.site.register([
    Block,
    Chain,
])
