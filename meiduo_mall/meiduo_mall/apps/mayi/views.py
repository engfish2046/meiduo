from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from .utils import Mayi


class MayiURLView(APIView):
    """
    提供支付宝登陆的网址
    """
    def get(self,request):
        # 提取state参数
        state = request.query_params.get('state')
        if not state:
            state = '/'
        #按说明文档拼接地址
        mayi = Mayi(state=state)
        login_url = mayi.generate_mayi_login_url()
        #返回链接地址
        return Response({"mayi_url":login_url})