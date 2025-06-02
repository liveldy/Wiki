'''
数码管驱动程序
作者：哀歌殇年
版本：V1.0.0(2024/4/13)
使用范围：兼容任意位数的八段数码管
使用说明：
1.定义数码管对象：seg_8(共极类型,段管脚号,位管脚号,扫描速度)
    其中：共极类型分为共阴极（0）和共阴极（1），段管脚号和位管脚号请使用列表传入，段管脚号必须8个元素，位管脚号任意个数元素，如果只有1位，则省略（None）
        扫描速度单位为ms，默认值5ms
2.成员函数：
    clear()：全部清空
    full()：全部填充
    detec()：检查，即将所有数码都显示一遍，用于检测数码管是否有损坏等
    bshow(位号，需显示的字符)：位显示，位号由定义数码管对象时指定引脚顺序排列0，1，2……，目前支持数字和部分大小写英文字符
    show(需显示的字符串)：全显示
    
    以上函数请按规范使用，如果使用错误会出现异常或报错，下面是一个简单的用例：
    from common.seg import seg_8
    
    segs = seg_8(0,[5,16,9,18,17,6,46,8],[4,7,15,3])
    while True:
        segs.show('nb66')

'''
from machine import Pin
import time

class seg_8:
    
    def __init__(self,common_pole,pins,bits=None,speed=5):
        self.seg_pin=[]
        self.seg_bit=[]
        for pnum in pins:
            self.seg_pin.append(Pin(pnum,Pin.OUT))
        if bits != None:
            for bnum in bits:
                self.seg_bit.append(Pin(bnum,Pin.OUT))
        else:
            self.seg_bit=None
        self.dicts = {
            #    [a, b, c, d, e, f, g, dp]
            '0': [1, 1, 1, 1, 1, 1, 0, 0],
            '1': [0, 1, 1, 0, 0, 0, 0, 0],
            '2': [1, 1, 0, 1, 1, 0, 1, 0],
            '3': [1, 1, 1, 1, 0, 0, 1, 0],
            '4': [0, 1, 1, 0, 0, 1, 1, 0],
            '5': [1, 0, 1, 1, 0, 1, 1, 0],
            '6': [1, 0, 1, 1, 1, 1, 1, 0],
            '7': [1, 1, 1, 0, 0, 0, 0, 0],
            '8': [1, 1, 1, 1, 1, 1, 1, 0],
            '9': [1, 1, 1, 1, 0, 1, 1, 0],
            'a': [1, 1, 1, 1, 1, 0, 1, 0],
            'b': [0, 0, 1, 1, 1, 1, 1, 0],
            'c': [0, 0, 0, 1, 1, 0, 1, 0],
            'd': [0, 1, 1, 1, 1, 0, 1, 0],
            'e': [1, 1, 0, 1, 1, 1, 1, 0],
            'g': [1, 1, 1, 1, 0, 1, 1, 0],
            'h': [0, 0, 1, 0, 1, 1, 1, 0],
            'l': [0, 1, 1, 0, 0, 0, 0, 0],
            'n': [0, 0, 1, 0, 1, 0, 1, 0],
            'o': [0, 0, 1, 1, 1, 0, 1, 0],
            'p': [1, 1, 0, 0, 1, 1, 1, 0],
            'q': [1, 1, 1, 0, 0, 1, 1, 0],
            'r': [0, 0, 0, 0, 1, 0, 1, 0],
            'u': [0, 0, 1, 1, 1, 0, 0, 0],
            'y': [0, 1, 1, 1, 0, 1, 1, 0],
            'A': [1, 1, 1, 0, 1, 1, 1, 0],
            'C': [1, 0, 0, 1, 1, 1, 0, 0],
            'E': [1, 0, 0, 1, 1, 1, 1, 0],
            'F': [1, 0, 0, 0, 1, 1, 1, 0],
            'G': [1, 0, 1, 1, 1, 1, 0, 0],
            'H': [0, 1, 1, 0, 1, 1, 1, 0],
            'J': [0, 1, 1, 1, 0, 0, 0, 0],
            'L': [0, 0, 0, 1, 1, 1, 0, 0],
            'O': [1, 1, 1, 1, 1, 1, 0, 0],
            'P': [1, 1, 0, 0, 1, 1, 1, 0],
            'R': [1, 1, 1, 0, 1, 1, 1, 0],
            'S': [1, 0, 1, 1, 0, 1, 1, 0],
            'U': [0, 1, 1, 1, 1, 1, 0, 0],
            'X': [0, 1, 1, 0, 1, 1, 1, 0],
        }
        
        if common_pole == 0:
            newdict = {}
            for key, value in self.dicts.items():
                newdict[key] = [1 - x for x in value]
            self.dicts = newdict

        self.count = speed
        self.pole = common_pole
        self.clear()
        
    def clear(self):
        for p in self.seg_pin:
            p.value(self.pole)
        for b in self.seg_bit:
            b.value(not self.pole)
    
    def full(self):
        for p in self.seg_pin:
            p.value(not self.pole)
        for b in self.seg_bit:
            b.value(self.pole)
    
    def detec(self):
        for b in self.seg_bit:
            b.value(self.pole)
        for d in self.dicts.values():
            time.sleep_ms(500)
            for i in range(len(d)):
                self.seg_pin[i].value(not d[i])
        self.clear()
    
    def bshow(self,strm,bits=None):
        gstr = self.dicts.get(strm)
        if bits == None:
            for i in range(len(gstr)):
                self.seg_pin[i].value(not gstr[i])
            return
        if gstr and 0 <= bits < len(self.seg_bit):
            self.clear()
            self.seg_bit[bits].value(self.pole)
            for i in range(len(gstr)):
                self.seg_pin[i].value(not gstr[i])
    
    def show(self,strs):
        for ds in range(len(strs)):
            self.bshow(strs[ds],ds)
            time.sleep_ms(self.count)