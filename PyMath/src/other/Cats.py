#!/usr/bin/env python
# encoding: utf-8
'''
other.Cat3 -- shortdesc

other.Cat3 is a description

It defines classes_and_methods

@author:     user_name

@copyright:  2019 organization_name. All rights reserved.

@license:    license

@contact:    user_email
@deffield    updated: Updated
'''
# coding:utf-8
from turtle import*
import turtle
def whiteCat():
    color("black")
    pu()
    goto(0,0)
    seth(0)
   
#     begin_fill()
    seth(200)
    #　調整起點
    circle(200,-20)
    pd()
    #　給小黑貓的舌頭預留
    #pu()
    fd(-30)
    #åpd()
    #　小白貓的頭頂（右）
    circle(150,-65)
    #　給小黑貓的爪子預留
    #pu()
    rt(16)
    fd(-20)
    #pd()
     #　小白貓的右邊臉
    circle(150,-5)
    lt(50)
    circle(50,-130)
    circle(150,-5)
     #　小白貓的下巴
    circle(700,-20)
     #　小白貓的左邊臉
    circle(50,-80)
    #rt(30)
    circle(180,-20)
    
    #pu()
    #小白貓的左耳
    lt(70)
    fd(-40)
    rt(100)
    circle(150,-30)
    lt(40)
    fd(10)
    #小白貓的頭頂（左）
    circle(130,-50)
    pu()
    goto(185,-15)
    pd()
     #小白貓的右耳（左）
    circle(150,-30)
    lt(80)
    fd(40)
     #小白貓的身體
    pu()
    goto(-80,-70)
    pd()
    rt(40)
    circle(120,70)
    #小白貓的腳腳
    rt(30)
    fd(20)
    circle(15,150)
    #fd(20)
    circle(-165,20)
     #小白貓的爪子）
    pu()
    goto(-75,-160)
    rt(160)
    pd()
    circle(120,20)
    circle(15,150) 
    circle(150,20)
     #小白貓的尾巴
    pu()
    goto(-150,-105)
    lt(90)
    pd()
    circle(30,100) 
    circle(50,30) 
    circle(10,160) 
    circle(50,10) 
    circle(-30,20) 
    #circle(-30,20) 
    circle(-10,60) 
    circle(-15,50) 
    #　小白貓的眼睛
    pu()
    goto(30,-125)
    rt(20)
    pd()
    circle(15,180) 
    pu()
    goto(150,-125)
    rt(180)
    pd()
    circle(15,180) 
    
    #　小白貓的嘴巴
    color("black",'pink')
    begin_fill()
    pu()
    goto(90,-135)
    rt(150)
    pd()
    pensize(4)
    circle(5,100) 
    fd(5)
    rt(70)
    fd(5)
    circle(5,100) 
    #color("black",'pink')
    pu()
    goto(95,-138)
    rt(150)
    pd()
    begin_fill()
    circle(300,5) 
    circle(2,155) 
    circle(300,5)
    end_fill()
    
    #　小白貓的內耳（左）
    color("pink",'pink')
    
    pu()
    goto(-40,-42)
    lt(115)
    pd()
    begin_fill()
    circle(130,17) 
    lt(110)
    fd(20)
    end_fill()
    #　小白貓的內耳（右）
    pu()
    goto(208,-30)
    lt(25)
    pd()
    begin_fill()
    circle(-90,22) 
    rt(103)
    fd(18)
    end_fill()

def setting():          #参数设置
    pensize(6)
    hideturtle()
    colormode(255)
    setup(900,900)
    speed(10)
setting()
whiteCat()   
turtle.mainloop()
turtle.done()