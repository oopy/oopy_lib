--- 
title: minimalmodbus
tags: micropython,lib
author: [Jonas Berg](https://github.com/pyhys/minimalmodbus)
author: [Huifeng](https://github.com/sgrrzhf)
--- 
#  类Instrument

## 初始化参数
`port` UART模块号
`slaveaddress` 从机地址，范围1~247
`stopbits` UART停止位，默认1
`bytesizes` UART数据位，默认8
`parity` UART校验位，默认None
`baudrate` UART波特率，默认9600
`timeout` UART读超时时间，默认1000 ms

## 函数
`write_register()` : 写单个寄存器
参数：	
`registeraddress` 寄存器地址
`value` 待写入的值
返回值： 
None

`read_registers()` : 读寄存器
参数：	
`registeraddress` ：起始地址
`numberOfRegisters` ： 待读取的数量
`functioncode`：功能码，可选3,4，默认3
返回值： 
读取的一组寄存器值，list类型

`write_registers()` : 写多个寄存器
参数：
`registeraddress`： 起始地址
`values` ： 一组待写入的数据，list类型
返回值：
None

## 范例
```
>>> from minimalmodbus import Instrument
>>> device = Instrument(3,2)
>>> registers = device.read_registers(0,2,functioncode = 4)
>>> temperature = registers[0]/10
>>> r_humidity = registers[1]/10
>>> print('\rtemperature: %0.1f, r_humidity: %0.1f%%'%(temperature,r_humidity))
temperature: 29.6, r_humidity: 47.9%

>>> device.write_register(1,2468)
>>> print(device.read_registers(1,1))
[2468]

>>> value = [1,2,3,4,1122,3344]
>>> device.write_registers(4,value)
>>> print(device.read_registers(4,6))
[1, 2, 3, 4, 1122, 3344]
```
