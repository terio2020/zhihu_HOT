# 通过Python爬取知乎热点信息，结合PushPlus+今天推送到个人微信

 - 知乎一般爬虫无法直接爬取，设置UA-header，使用自己的cookie即可爬取

 - PushPlus+推送参考：https://blog.csdn.net/weixin_43820324/article/details/115454877

 - 由于PushPlus+的推送模式，content有长度限制，因此分成了两次发送（比较简易实现）