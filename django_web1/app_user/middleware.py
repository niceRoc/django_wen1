# -*- coding: utf-8 -*-


class UrlMiddleware(object):
    """处理用户请求的url地址的中间件类"""

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        处理url请求前：在每个url请求上调用，返回None或HttpResponse对象
        :param request: HttpRequest对象
        :view_func: 视图函数
        :view_args: 视图函数中获取到url传来的位置参数
        :view_kwargs: 视图函数中获取到rul传来的关键字参数
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
