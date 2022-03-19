from django.http import HttpResponse
def page_view_ND(request):
    html = "<h1>NeatDataset url和视图函数测试</h1>"
    return HttpResponse(html)