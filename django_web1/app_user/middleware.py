# -*- coding: utf-8 -*-


class UrlMiddleware(object):
    """处理用户请求的url地址的中间件类"""

    def process_request(self, request):
        """
        处理url请求前：在每个url请求上调用，返回None或HttpResponse对象
        :param request: HttpRequest对象
        将当前的页面url存在session中
        """
        if request.path not in [
            '/user/login/',
            '/user/logout/',
            '/user/login_handle/',
            '/user/register/',
            '/user/register_handle/',
            '/user/register_valid'
        ]:
            request.session['url_path'] = request.get_full_path()

        # 如果请求的地址满足下列列表，则写入一个值存在session中
        if request.path in [
            '/',
            '/goods/'
        ]:
            request.session['is_dis'] = '1'

