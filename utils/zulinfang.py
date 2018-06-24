from splinter import Browser
import time
import sys
import codecs
import importlib
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

## Set config
url='http://select.pdgzf.com/Room/List'
usr='15021557056'
psw='janny123'
texts = ['上南路3323弄（仁文公寓）/2号/22楼/2202','枣庄路1029弄/3号/3楼/301','浦东大道1623弄/6号/4楼/405','浦东大道1700弄/3号/3楼/302']
wait_time = 10


browser = Browser(driver_name='chrome', executable_path='/Users/zj/Documents/bak/chromedriver', user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36")
browser.visit(url)
while browser.is_text_not_present('登录'):
	time.sleep(1)
# login
browser.find_by_xpath('//*[@id="global-navbar"]/div/div/ul[2]/li[1]/a').click()
browser.find_by_xpath('//*[@id="LoginName"]').fill(usr)
browser.find_by_xpath('//*[@id="Pwd"]').fill(psw)
while browser.is_text_not_present('稍后再说'):
	time.sleep(1)
if browser.is_text_present('稍后再说'):
	browser.find_by_xpath('//*[@id="layui-layer1"]/div[2]/a[2]').click()

while browser.is_text_not_present('条件找房'):
	time.sleep(1)

browser.find_by_xpath('//*[@id="filterserarch"]').click()
while browser.is_text_not_present('区域：'):
	time.sleep(1)

for text in texts:
	browser.find_by_id('txtKey').fill(text)
	browser.find_by_xpath('/html/body/header/div[2]/div/div[2]/div[2]/a').click()
	
	if browser.is_text_not_present('暂无数据'):
		browser.find_by_xpath('/html/body/div[4]/div[2]/div/div[1]/div/div[2]/p/a').click()
		while browser.is_text_present('立即选房',wait_time=wait_time):
			browser.find_by_xpath('//*[@id="rentBtn"]').click()
	else:
		print('over')
		browser.quit()

browser.quit()