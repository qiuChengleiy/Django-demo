http协议（超文本传输协议)
定义： http是浏览器与万维网服务器之间相互通信的规则
特点： 1.基于请求/响应模式  2.无状态协议，ftp是有状态
url 统一资源定位符： 协议名：//域名：端口/路径

二 请求协议

请求协议的格式如下：

请求首行；  // 请求方式 请求路径 协议和版本，例如：GET /index.html HTTP/1.1
请求头信息；// 请求头名称:请求头内容，即为key:value格式，例如：Host:localhost
空行；     // 用来与请求体分隔开
请求体。   // GET没有请求体，只有POST有请求体。
浏览器发送给服务器的内容就这个格式的，如果不是这个格式服务器将无法解读！在HTTP协议中，请求有很多请求方法，其中最为常用的就是GET和POST。不同的请求方法之间的区别，后面会一点一点的介绍。

2.1　GET请求

HTTP默认的请求方法就是GET
     * 没有请求体
     * 数据必须在1K之内！
     * GET请求数据会暴露在浏览器的地址栏中

GET请求常用的操作：
       1. 在浏览器的地址栏中直接给出URL，那么就一定是GET请求
       2. 点击页面上的超链接也一定是GET请求
       3. 提交表单时，表单默认使用GET请求，但可以设置为POST

复制代码
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding:gzip, deflate, sdch
Accept-Language:zh-CN,zh;q=0.8
Cache-Control:no-cache
Connection:keep-alive
Cookie:csrftoken=z5H43ZwARx7AIJ82OEizBOWbsAQA2LPk
Host:127.0.0.1:8090
Pragma:no-cache
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36
Name
login/
1 requests ❘ 737 B transferred ❘ Finish: 5 ms ❘ DOMContentLoaded: 14 ms ❘ Load: 14 ms
复制代码
GET 127.0.0.1:8090/login  HTTP/1.1：GET请求，请求服务器路径为  127.0.0.1:8090/login ，协议为1.1；
Host:localhost：请求的主机名为localhost；
*User-Agent: Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0：与浏览器和OS相关的信息。有些网站会显示用户的系统版本和浏览器版本信息，这都是通过获取User-Agent头信息而来的；
 Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8：告诉服务器，当前客户端可以接收的文档类型，其实这里包含了*/*，就表示什么都可以接收；
Accept-Language: zh-cn,zh;q=0.5：当前客户端支持的语言，可以在浏览器的工具选项中找到语言相关信息；
Accept-Encoding: gzip, deflate：支持的压缩格式。数据在网络上传递时，可能服务器会把数据压缩后再发送；
Accept-Charset: GB2312,utf-8;q=0.7,*;q=0.7：客户端支持的编码；
Connection: keep-alive：客户端支持的链接方式，保持一段时间链接，默认为3000ms；
Cookie: JSESSIONID=369766FDF6220F7803433C0B2DE36D98：因为不是第一次访问这个地址，所以会在请求中把上一次服务器响应中发送过来的Cookie在请求中一并发送去过；这个Cookie的名字为JSESSIONID。
注意

 View Code
2.2　POST请求

(1). 数据不会出现在地址栏中
(2). 数据的大小没有上限
(3). 有请求体
(4). 请求体中如果存在中文，会使用URL编码！

1
username=%E5%BC%A0%E4%B8%89&password=123
 为什么要进行URL编码
使用表单可以发POST请求，但表单默认是GET

1
2
3
4
<form action="" method="post">
  关键字：<input type="text" name="keyword"/>
  <input type="submit" value="提交"/>
</form>
输入yuan后点击提交，查看请求内容如下：

复制代码
Request Headers
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding:gzip, deflate
Accept-Language:zh-CN,zh;q=0.8
Cache-Control:no-cache
Connection:keep-alive
Content-Length:13
Content-Type:application/x-www-form-urlencoded
Cookie:csrftoken=z5H43ZwARx7AIJ82OEizBOWbsAQA2LPk
Host:127.0.0.1:8090
Origin:http://127.0.0.1:8090
Pragma:no-cache
Referer:http://127.0.0.1:8090/login/
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1)
           AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36

Form Data
username:yuan
复制代码
POST请求是可以有体的，而GET请求不能有请求体。

Referer: http://localhost:8080/hello/index.jsp：请求来自哪个页面，例如你在百度上点击链接到了这里，那么Referer:http://www.baidu.com；如果你是在浏览器的地址栏中直接输入的地址，那么就没有Referer这个请求头了；
Content-Type: application/x-www-form-urlencoded：表单的数据类型，说明会使用url格式编码数据；url编码的数据都是以“%”为前缀，后面跟随两位的16进制。
Content-Length:13：请求体的长度，这里表示13个字节。
keyword=hello：请求体内容！hello是在表单中输入的数据，keyword是表单字段的名字。
 Referer的应用
三　响应协议

3.1　响应内容

响应协议的格式如下：

响应首行；
响应头信息；
空行；
响应体。
响应内容是由服务器发送给浏览器的内容，浏览器会根据响应内容来显示。遇到<img src=''>会开一个新的线程加载，所以有时图片多的话，内容会先显示出来，然后图片才一张张加载出来。

复制代码
Request URL:http://127.0.0.1:8090/login/
Request Method:GET
Status Code:200 OK
Remote Address:127.0.0.1:8090
Response Headers
view source
Content-Type:text/html; charset=utf-8
Date:Wed, 26 Oct 2016 06:48:50 GMT
Server:WSGIServer/0.2 CPython/3.5.2
X-Frame-Options:SAMEORIGIN

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<form action="/login/" method="post">
  用户名：<input type="text" name="username"/>
  <input type="submit" value="提交"/>
</form>
</body>
</html>
复制代码
HTTP/1.1 200 OK：响应协议为HTTP1.1，状态码为200，表示请求成功，OK是对状态码的解释；
Server:WSGIServer/0.2 CPython/3.5.2：服务器的版本信息；
Content-Type: text/html;charset=UTF-8：响应体使用的编码为UTF-8；
Content-Length: 724：响应体为724字节；
Set-Cookie: JSESSIONID=C97E2B4C55553EAB46079A4F263435A4; Path=/hello：响应给客户端的Cookie；
Date: Wed, 25 Sep 2012 04:15:03 GMT：响应的时间，这可能会有8小时的时区差；
3.2　状态码

响应头对浏览器来说很重要，它说明了响应的真正含义。例如200表示响应成功了，302表示重定向，这说明浏览器需要再发一个新的请求。

200：请求成功，浏览器会把响应体内容（通常是html）显示在浏览器中；
404：请求的资源没有找到，说明客户端错误的请求了不存在的资源；
500：请求资源找到了，但服务器内部出现了错误；
302：重定向，当响应码为302时，表示服务器要求浏览器重新再发一个请求，服务器会发送一个响应头Location，它指定了新请求的URL地址；
304：
复制代码
  当用户第一次请求index.html时，服务器会添加一个名为Last-Modified响应头，这个头说明了
  index.html的最后修改时间，浏览器会把index.html内容，以及最后响应时间缓存下来。当用户第
  二次请求index.html时，在请求中包含一个名为If-Modified-Since请求头，它的值就是第一次请
  求时服务器通过Last-Modified响应头发送给浏览器的值，即index.html最后的修改时间，
  If-Modified-Since请求头就是在告诉服务器，我这里浏览器缓存的index.html最后修改时间是这个,
  您看看现在的index.html最后修改时间是不是这个，如果还是，那么您就不用再响应这个index.html
  内容了，我会把缓存的内容直接显示出来。而服务器端会获取If-Modified-Since值，与index.html
  的当前最后修改时间比对，如果相同，服务器会发响应码304，表示index.html与浏览器上次缓存的相
  同，无需再次发送，浏览器可以显示自己的缓存页面，如果比对不同，那么说明index.html已经做了修
  改，服务器会响应200。
复制代码


3.3　其他响应头

告诉浏览器不要缓存的响应头：

Expires: -1；
Cache-Control: no-cache；
Pragma: no-cache；
自动刷新响应头，浏览器会在3秒之后请求http://www.baidu.com：

Refresh: 3;url=http://www.baidu.com
3.4　HTML中指定响应头

在HTMl页面中可以使用<meta http-equiv="" content="">来指定响应头，例如在index.html页面中给出<meta http-equiv="Refresh" content="3;url=http://www.baidu.com">，表示浏览器只会显示index.html页面3秒，然后自动跳转到http://www.baidu.com.




























