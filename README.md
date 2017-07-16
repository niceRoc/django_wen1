# 利用Django框架创建一个web小项目(django_wen1) <br/>


### 用户模块			app_user
1. app_user models.py 模型类创建		UserInfo - 用户基本信息

2. templates app_user 模板页
	
	+1. 用户注册  <br/>
		-1.register.html - 注册页

	+2. 用户登录  <br/>
		-1. login.html  - 登录页

	+3. 用户中心  
		a. info.html - 用户中心-个人信息
		b. order.html - 用户中心-我的订单 
		c. site.html - 用户中心-收货地址 

3. app_user views.py 视图,功能实现

	+1. 注册页  <br/>
		-1. 通过js的正则匹配完成页面的表单数据验证,让用户按照定义的格式进行填写信息,
		-2. 完成注册后,跳转到登录页进行登录

	+2. 登录页
		-1. 通过数据查询判断用户是否存在,提示用户对应的友好信息,协助登录.
		-2. 记住用户名: 让用户选择是否勾选,勾选时就将用户名存在cookies中,设置过期时间7天.
		-3. 往session中记录一个用户id的值,方便后期的操作.

	+3. 用户中心
		-1. 是否登录: 当用户直接请求用户中心得视图时,判断之前在session中存的id值是否存在,只有登录才能访问.定义在一个装饰器中,方便调用
		-2. 展示页面: 通过数据查询将数据传递到模板中,让浏览器渲染对应的模板,展示给用户.
		-3. 历史浏览: 将用户最新访问的5条商品记录在cookies中,显示在个人中心页面中.

### 商品模块			app_goods
1. app_goods models.py 模型类创建		 	GoodsType - 商品分类   GoodsInfo - 商品信息

2. 需求分析

### 购物车模块		app_cart

### 订单模块			app_order
