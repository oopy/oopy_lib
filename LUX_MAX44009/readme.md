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
### 功能: 获取光照强度数据
### 参数: 
`accuracy` 设置读取的精度
`accuracy = True`时，读取的数据为高精度，反之为低精度，默认为`False`
### 返回: 浮点数，光照强度


## 范例
```python
>>> from lux_max44009 import MAX44009
>>>
>>> device = MAX44009()
>>> lux = device.get_lux()
>>> print("lux:",lux)
lux: 63.36
>>> accuracy_lux = device.get_lux(accuracy=True)
>>> print("lux:",accuracy_lux)
lux: 64.08
>>>

```
