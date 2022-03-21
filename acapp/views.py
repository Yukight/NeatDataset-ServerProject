import json
import uuid

from django.core.cache import cache
from django.http import HttpResponse
from django.views import View

from app import models


def page_view_ND(request):
    html = "NeatDataset"
    return HttpResponse(html)


class BaseView(View):
    def successData(data, msg='处理成功'):
        resl = {'code': 0, 'msg': msg, 'data': data}
        return HttpResponse(json.dumps(resl), content_type='application/json; charset=utf-8')

    def error(msg='系统异常'):
        resl = {'code': 1, 'msg': msg}
        return HttpResponse(json.dumps(resl), content_type='application/json; charset=utf-8')


'''
系统处理
'''


class SysView(BaseView):

    def get(self, request, module, *args, **kwargs):

        if module == 'info':
            pass
            # TODO

    def post(self, request, module, *args, **kwargs):

        if module == 'login':
            return SysView.login(request)

    def as_View(self, request, module, **initkwargs):
        SysView.get()
        SysView.post()

    '''
    请求函数
    '''

    def login(request):
        userName = request.POST.get('userName')
        passWord = request.POST.get('passWord')

        user = models.Users.objects.filter(userName=userName)
        if user.exists():
            user = user.first()
            if user.passWord == passWord:
                token = uuid.uuid4()

                login_user = {
                    'id': user.id,
                    'userName': user.userName,
                    'passWord': user.passWord,
                    'name': user.name,
                    'age': user.age,
                    'gender': user.gender,
                    'phone': user.phone,
                    'email': user.email,
                    'type': user.type
                }
                resl = {

                }
                cache.set(token, login_user, 60 * 60 * 60 * 48)
                return SysView.successData(resl)
            else:
                return SysView.error('用户密码输入错误')
        else:
            return SysView.error('用户名输入错误')



