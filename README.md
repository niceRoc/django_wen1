# 利用Django框架创建一个web小项目(django_web1) <br/>


### 用户模块			app_user

1. app_user models.py 模型类创建		

    +1. UserInfo - 用户基本信息

2. templates app_user 模板页

    +1. 用户注册

        1. register.html - 注册页

    +2. 用户登录

        1. login.html  - 登录页

    +3. 用户中心  

        1. info.html - 用户中心-个人信息

        2. order.html - 用户中心-我的订单

        3. site.html - 用户中心-收货地址

3. app_user views.py 视图,功能实现

	+1. 注册页  

		1. 通过js的正则匹配完成页面的表单数据验证,让用户按照定义的格式进行填写信息.

		2. 完成注册后,跳转到登录页进行登录

	+2. 登录页

		1. 通过数据查询判断用户是否存在,提示用户对应的友好信息,协助登录.

		2. 记住用户名: 让用户选择是否勾选,勾选时就将用户名存在cookies中,设置过期时间7天.

		3. 往session中记录一个用户id的值,方便后期的操作.

	+3. 用户中心

		1. 是否登录: 当用户直接请求用户中心得视图时,判断之前在session中存的id值是否存在,只有登录才能访问.定义在一个装饰器中,方便调用

		2. 展示页面: 通过数据查询将数据传递到模板中,让浏览器渲染对应的模板,展示给用户.

		3. 历史浏览: 将用户最新访问的5条商品记录在cookies中,显示在个人中心页面中.

### 商品模块			app_goods

1. app_goods models.py 模型类创建

    +1. GoodsType - 商品分类

    +2. GoodsInfo - 商品信息

2. templates app_goods  模板页

    +1. index.html - 网站首页

    +2. detail.html - 商品详情页

    +3. list.html - 商品列表页

3. app_goods views.py 视图,功能实现

    +1. 网站首页

        1. 用户登录显示登录后的信息,可以查看自己的状态.

        2. 点击商品,可以进入商品的详情页进行查看以及购买.

        3. 商品分类以及更多查看,可以进入对应的商品分类列表.

    +2. 商品详情页

        1. 点击对应的商品进入同一个页面,展示不同商品的详情,通过url传递商品id值来进行判断查询对应的商品信息,然后展示.

        2. 可以在详情页购买商品,添加商品到购物车.

        3. 加入js对于购物车商品输入的判断,通过ajax查询商品库存是否足够.

    +3. 商品列表页

        1. 通过url传递的商品分类id,查询不同商品分类下的所有商品,默认按照最新商品来排序,还可以通过价格高低,以及人气值来进行排序.可以添加商品到购物车.

        2. 加入了分页查询,利用Django内置的方法和对象来查询的.

        3. 通过在视图中加入的逻辑判断, 实现了页码多时一致显示5个页码,当前页码,以及之前2个和之后2个页码的显示.

    +4. 第三方和富文本

        1. 通过haystack内的whoosh引擎加上jieba中文分词实现了全文检索.

        2. 加入了富文本tinymce编辑器

### 购物车模块		app_cart
1. app_goods models.py 模型类创建

	+1. CartInfo - 购物车数据模型类

2. templates app_cart  模板页

	+1. cart.html - 我的购物车页面

	+2. place_order.html - 购物车提交订单页面

3. app_cart views.py 视图,功能实现

	+1. 我的购物车

		1. 通过js实现了购物车中商品数量、价格的统计,以及商品数量更改时的验证.

		2. 通过ajax实现了购物车中商品数量对应数据库的更改,库存的判断.

		3. 提交订单时将选中的商品都传递到购物车订单提交页面做处理.

	+2. 订单提交处理

		1. 通过js实现了购物车中商品数量、价格的统计,以及商品数量更改时的验证.

		2. 通过ajax将数据传递到订单模块后台进行数据操作处理

		4. 提交订单成功后转到个人订单页面展示刚才的购物商品信息.

### 订单模块			app_order

1. app_order models.py 模型类创建

	+1. OrderMain - 订单主表,记录订单信息

	+2. OrderDetail - 订单从表,记录订单中商品详情

2. templates app_order  模板页

	+1. 无具体展示的模板页,都在视图中实现的逻辑操作,进行数据处理.

3. app_order views.py 视图,功能实现

	+1. 提交订单
		1. 后台加入事务同时操作多张表.判断库存,将选中的商品添加到订单中,删除购物车中记录.其中任何一步异常,就回滚事务放弃之前所有的操作,只有所有商品添加成功,才提交事务,更改表中记录.
