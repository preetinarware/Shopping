from django.contrib import admin

# Register your models here.

from home.models import More_Products,enquiries,mycart,Oders,abouts,Book_testdrive,product_specif,product_access,product_key,profile

# Register your models here.

admin.site.register(enquiries)
admin.site.register(More_Products)
admin.site.register(mycart)
admin.site.register(Oders)
admin.site.register(abouts)
admin.site.register(Book_testdrive)
admin.site.register(product_specif)
admin.site.register(product_key)
admin.site.register(product_access)
admin.site.register(profile)