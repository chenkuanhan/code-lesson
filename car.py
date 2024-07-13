# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:30:51 2024

@author: teacher
"""


class Car:
    #描述車子特性
    def __init__(self, car_num, carType, color):
        self.brand = 'Toyota'
        self.number = car_num
        self.carType = carType
        self.color = color
        
    #車子功能性
    #發動引擎
    def start(self, method):
        if method == "鑰匙":
            print("轉動鑰匙啟動")
        elif method == "遙控器":
            print("逼逼 啟動中...")
        elif method == "按鈕" :
            print("點亮啟動中...")
        else:
            print("啟動方法錯誤")
            
    #踩油門
    def acce(self):
        print("現在加速中")
        
    #剎車
    def stop(self):
        print("煞車中....")
        
    #喇叭
    def banban(self):
        print("ban ban ...")
        
    #轉彎
    def turn(self, direction):
        if direction == "向前":
            print("前行...")
        elif direction == "左轉":
            print("左轉...")
        elif direction == "右轉" :
            print("右轉...")
            

if __name__ == "__main__":
    
    print(__name__)
    car1 = Car("ASD-123456", "休旅車", "blue")
    
    print(car1.brand)
    print(car1.number)
    
    print(car1.start("按鈕"))
    print(car1.acce())
    print(car1.turn("右轉"))
    print(car1.stop())
    
    car2 = Car(color="red", carType="跑車", car_num='QW-123')