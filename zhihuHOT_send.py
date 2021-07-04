# %%
import smtplib
from email.header import Header
from email.mime.text import MIMEText
import zhihuHOT_acq
import requests

def send_wechat():
    
    all = zhihuHOT_acq.get_zhihu_hot()

    for j in range(2):
        if(j == 0):
            content_wechat = "<h3>知乎热点[Top 1 ~ 20]</h3><br/>"
            for i in range(20):
                content_wechat = content_wechat + ("Top" + str(i + 1) + " <a href=\"" + all[i][1][0] + "\">" + all[i][0][
                        0] + "</a>" + "<br/>")

            url = "{}".format(
                content_wechat)
            reqp = requests.get(url)
        else:
            content_wechat = "<h3>知乎热点[Top 20 ~ 40]</h3><br/>"
            for i in range(20, 40):
                content_wechat = content_wechat + ("Top" + str(i + 1) + " <a href=\"" + all[i][1][0] + "\">" + all[i][0][
                        0] + "</a>" + "<br/>")

            url = "{}".format(
                content_wechat)
            reqp = requests.get(url)


if __name__ == '__main__':
    send_wechat()