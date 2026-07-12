from selenium import webdriver
# 设置Edge WebDriver的路径（如果你的WebDriver在系统路径中，则不需要这行代码）
# driver_path = 'path/to/msedgedriver.exe'
# webdriver.Edge.set_service(driver_path)
# 创建一个Edge WebDriver实例
driver = webdriver.Edge()
# 打开一个网页
driver.get('https://www.example.com')
# 打印页面标题
print(driver.title)
