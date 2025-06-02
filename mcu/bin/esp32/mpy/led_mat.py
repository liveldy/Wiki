'''
LED点阵驱动程序
作者：哀歌殇年
版本：V1.0.0（2024/4/14）
使用范围：8*8 LED点阵（后期会完善）
使用说明：
1.定义LED点阵对象：led_8(行引脚列表,列引脚列表)
2.内置行显示函数、列显示函数，流水灯演示和箭头演示
'''
from machine import Pin
import time

class led_8:
    
    def __init__(self,rows,cols):
        self.led_row = []
        self.led_col = []
        for r in rows:
            self.led_row.append(Pin(r,Pin.OUT))
        for c in cols:
            self.led_col.append(Pin(c,Pin.OUT))
    
    def set_power_row(i):
        for row in self.led_row:
            row.value(0)
        if 0 <= i <= 7:
            self.led_row[i].value(1)


    def set_earth_col(i):
        for col in self.led_col:
            col.value(1)
        if 0 <= i <= 7:
            self.led_col[i].value(0)
            
    def show_led():
        for row in range(8):
            set_power_row(row)
            for col in range(8):
                set_earth_col(col)
                time.sleep_ms(100)

    def show_arrow():
        img_list = [
            (1, 4),
            (2, 5),
            (3, 6),
            (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7),
            (5, 6),
            (6, 5),
            (7, 4)
        ]
        for x, y in img_list:
            set_power_row(x)
            set_earth_col(y)
            time.sleep_ms(1)
