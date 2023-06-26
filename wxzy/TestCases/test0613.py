from appium import webdriver

# 设置Desired Capabilities
desired_caps = {
  "platformName": "iOS",
  "platformVersion": "13.6",
  "deviceName": "iPhone X",
  "udid": "9e0534e6dfc329bd0129c8c7c276b3eb0af169ea",
  "bundleId": "com.facebook.IntegrationApp1118999"
}

# 连接到Appium服务器
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 执行自动化测试操作
# ...

# 关闭连接
driver.quit()
