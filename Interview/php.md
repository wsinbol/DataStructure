# PHP QA

## HTTP Status Code

- 200 OK 请求成功顺利返回
- 202 Accepted 请求已经接受，但处理尚未完成
- 204 No Content 请求成功处理，但没有资源可以返回
- 301 Moved Permanently 永久重定向 表示之后的请求应使用更改后的URL
- 302 Found 临时性重定向 表示本次请求临时使用新的URL
- 303 See Other 表示应使用GET方法请求新的URL
- 400 Bad Request 表示请求中存在语法错误
- 401 Unauthorized 未经许可，未授权
- 403 Forbidden 拒绝访问
- 404 Not Found 文件缺失
- 500 Inter Server Error 服务器内部错误
- 503 Server Unavaliable 服务器处于超负载或维护阶段，无法处理请求

## PHP 自动加载机制

https://www.zybuluo.com/phper/note/66447

> 自动加载的原理，就是在我们new一个class的时候，PHP系统如果找不到你这个类，就会去自动调用本文件中的__autoload($class_name)方法，我们new的这个class_name 就成为这个方法的参数。所以我们就可以在这个方法中根据我们需要new class_name的各种判断和划分就去require对应的路径类文件，从而实现自动加载。

> 小的项目，用__autoload($class_name)就能实现基本的自动加载了。但是如果一个项目过大，或者需要不同的自动加载来加载不同路径的文件，这个时候__autoload就悲剧了，原因是一个项目中仅能有一个这样的 __autoload($class_name) 函数，因为 PHP 不允许函数重名，也就是说你不能声明2个__autoload($class_name)函数文件，否则会报致命错误，我了个大擦，那怎么办呢？放心，你想到的，PHP开发大神早已经想到。所以spl_autoload_register()这样又一个牛逼函数诞生了，并且取而代之它。它执行效率更高，更灵活。

```php
sql_autoload_resister('load_function'); //函数名，非函数类的调用方式
sql_autoload_resister(array('load_object', 'load_function')); //类和静态方法，类加载的方式
sql_autoload_resister('load_object::load_function'); //类和方法的静态调用，类加载的方式

//php 5.3之后，也可以像这样支持匿名函数了。
spl_autoload_register(function($className){
    if (is_file('./lib/' . $className . '.php')) {
        require './lib/' . $className . '.php';
    }
});
```

> spl_autoload_register是可以多次重复使用的，这一点正是解决了__autoload的短板，那么如果一个页面有多个，执行顺序是按照注册的顺序，一个一个往下找，如果找到了就停止。





