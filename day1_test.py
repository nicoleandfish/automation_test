'''
name = input("请输入你的名字: ")
print("你好，" + name + "！欢迎进入自动化测试训练营！")
'''

'''
fruits = ["苹果", "香蕉", "橘子"]
for fruit in fruits:
    print("我喜欢吃 " + fruit)
'''

# 模拟测试设备返回值
devices = {"DeviceA": "PASS", "DeviceB": "FAIL", "DeviceC": "PASS"}

for device, status in devices.items():
    print(f"{device} 测试结果: {status}")