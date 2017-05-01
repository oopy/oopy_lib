---
title: SHT20
tags: python,lib,sensor
---

# 类SHT20
## 初始化参数

``scl_pin`` I2C的scl引脚序号，默认为16

``sda_pin`` I2C的sda引脚序号，默认为17

``clk_freq`` I2C的时钟频率，默认为100k

## 函数
`` get_temperature()``
功能：获取温度数据
返回：float型变量，温度

``get_relative_humidity()``
功能：获取相对湿度
返回值：float型变量，相对湿度

## 范例
```python
>>> from sht20 import SHT20
>>> sht_sensor = SHT20()
>>> T = sht_sensor.get_temperature()
>>> RH = sht_sensor.get_relative_humidity()
>>> print('temperature:', T)
temperature: 26.423867
>>> print('relative_humidity:', RH)
relative_humidity: 45.738740
```
