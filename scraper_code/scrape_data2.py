import requests
import lxml.html
html = requests.get('http://local-weewx:8099')
doc = lxml.html.fromstring(html.content)
current = doc.xpath('/div[@id="current_widget"]')
for mything in current:
    print(mything)
# contents = current.xpath('.//div[@class="widget_contents"]/table/tbody')

tree.xpath('/html/body/div[@id="contents"]/div[@id="widget_group"]/div[@id="current_widget"]/div[@class="widget_contents"]/table/tbody')

/html/body/div[@id="contents"]/div[@id="widget_group"]/div[@id="current_widget"]/div[@class="widget_contents"]/table/tbody/tr/td[@class="label"][text() = "Outside Temperature"]

//div[@class="widget_contents"]/table/tbody/tr/td[@class="label"][text() = "Outside Temperature"]

//div[@class="widget_contents"]/table/tbody/tr/td[@class="label"][text() = "Outside Temperature"]/../td[@class="data"]

//div[@class="widget_contents"]/table/tbody/tr/td[@class="label"][text() = "Outside Temperature"]/../td[@class="data"]/text()