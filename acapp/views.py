from django.http import HttpResponse
def page_view_ND(request):
    html = "NeatDataset"
    return HttpResponse(html)
