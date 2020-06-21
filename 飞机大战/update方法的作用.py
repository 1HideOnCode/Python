#可以在screen对象完成所有的blit方法之后，统一调用一次display.update()方法，同样可以在屏幕上看到最终的结果
#——使用display.set_mode()创建的screen对象是一个内存中屏幕数据对象，可以理解为油画的画布
#——screen.bllit()方法可在画布上绘制很多的图像，例如英雄、子弹，这而图像可能会彼此重叠或者覆盖
#——display.update()会将画布的最终结果绘制在屏幕上，这样可以提高屏幕的绘制效率，增加游戏的流畅度
import pygame
pygame.init()
#创建游戏窗口480*700
screen = pygame.display.set_mode((480,700))#set_mode()返回创建的游戏屏幕

#绘制背景图像
#1.加载图像数据
bg = pygame.image.load("./images/background.png")
#2.blit绘制图像
screen.blit(bg,(0,0))#（0，0）是指在哪个位置显示图片
#3.update更行屏幕显示
#pygame.display.update()#不调用update方法看不到显示的图片


#绘制英雄的飞机
hero = pygame.image.load("./images/me1.png")
screen.blit(hero,(100,100))
pygame.display.update()
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()




