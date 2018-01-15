
# -*- coding: utf-8 -*-

from machine import Pin, I2C


MAX44009_ADDRESS = 74
MAX44009_CONFIG = 0x00


class MAX44009(object):

    """ MAX44009 光照传感器 """

    def __init__(self, scl_pin=16, sda_pin=17, freq=400000):
        """ 初始化i2c及max44009 """
        self._address = MAX44009_ADDRESS
        self.scl = Pin(scl_pin)
        self.sda = Pin(sda_pin)
        self.freq = freq
        self._max44009_config = bytearray()
        self._max44009_config.append(MAX44009_CONFIG)
        self._i2c = I2C(scl=self.scl, sda=self.sda, freq=self.freq)
        self._i2c.writeto(self._address, self._max44009_config)

    def get_origin_data(self):
        """ 获取原始数据 """
        origin_data = bytearray()
        self._i2c.writeto(self._address, b'\x03')
        origin_data += self._i2c.readfrom(self._address, 1)

        return origin_data

    def get_lux(self):
        """ 转换为单位为lux的自然数 """
        origin_data = self.get_origin_data()
        exponent = (origin_data[0] & 0xf0) >> 4
        mantissa = origin_data[0] & 0x0f

        return (2**exponent) * 0.72 * mantissa
