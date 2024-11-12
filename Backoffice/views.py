from django.shortcuts import render

# Create your views here.
def Backoffice (request):
    return render(request,'be_pages_dashboard.html')


def Backofficetable (request):
    return render(request,'be_tables_datatables.html')

def Backofficetable2 (request):
    return render(request,'be_tables_datatables.html')

