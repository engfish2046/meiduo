from urllib.parse import urlencode

from django.conf import settings
import datetime
class Mayi(object):
    """
    用于支付宝登陆的工具类
    提供了支付宝登陆可能使用的方法
    """
    def __init__(self,app_id=None, method=None, charset=None, state=None):
        self.app_id = app_id or settings.MAYI_ID
        self.method = method or settings.METHOD
        self.charset = charset or settings.CHARSET
        self.sign_type = settings.SIGN_TYPE
        self.sign = settings.SIGN
        self.timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.state = state or settings.MYSTATE

    def generate_mayi_login_url(self):

        url = 'https://openapi.alipay.com/gateway.do'
        data = {
            "version":'1.0',
            "biz_content":None,
            "scopes":'auth_base',
            "state":self.state,
            "app_id":self.app_id,
            "method	":self.method,
            "charset":self.charset,
            "sign_type":self.sign_type,
            "sign":self.sign,
            "timestamp":self.timestamp

        }
        query_string = urlencode(data)
        url += query_string

        return url