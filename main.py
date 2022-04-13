#导入第三方库
import requests
url  = "https://www.sohu.com/"

#使用get()方法操作,获取一个响应
resource = requests.get(url=url)
#获取resource 对象中的数据
page_text = resource.text
print(page_text)