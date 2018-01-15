---
title: MAX44009 光照传感器
tags: python,lib,sensor
author: [Huifeng](https://github.com/sgrrzhf)
---

# 类 MAX44009
## 初始化参数

``scl_pin`` I2C的scl引脚序号，默认为16

``sda_pin`` I2C的sda引脚序号，默认为17

``freq`` I2C的时钟频率，默认为100k

## 函数
`` get_lux() ``
功能: 获取光照强度数据
返回: 浮点数，光照强度

## 范例
```python
>>> from lux_max44009 import MAX44009
>>>
>>> device = MAX44009()
>>> lux = device.get_lux()
>>> print("lux:",lux)
lux: 92.16
>>>
```
