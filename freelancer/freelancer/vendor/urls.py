from django.urls import path
from django.http import HttpResponse


def vendor_list(request):
    return HttpResponse("""
<h1>Vendors List</h1>
""")


app_name = "vendor"

urlpatterns = [
    path('vendors-list', vendor_list, name="vendors-list")
]