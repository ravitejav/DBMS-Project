
from django.contrib import admin
from .models import User, Notif, Fee_pay, Compliant, Comp_match, Paying, Defuser
# Register your models here.

admin.site.register(User)
admin.site.register(Notif)
admin.site.register(Fee_pay)
admin.site.register(Compliant)
admin.site.register(Comp_match)
admin.site.register(Paying)
admin.site.register(Defuser)
