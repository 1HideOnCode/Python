#1在游戏初始化定义一个pygame.Rect的变量记录英雄的初始位置
#2在游戏循环中让每次英雄的y = -1 -------向上移动
#3y<=0将英雄移动到屏幕的底部

#注意：每次调用update（）之前，需要把所有的游戏图像都重新绘制一遍，而且最应该先重新绘制背景图像
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
screen.blit(hero,(150,300))
pygame.display.update()


#创建时钟对象
clock = pygame.time.Clock()

#1.定义rect记录飞机的初始位置
hero_rect = pygame.Rect(150,300,102,126)
#设置游戏循环，意味着游戏正式开始：
#i = 0


while True:
    #可以控制游戏循环内部的代码执行频率
    clock.tick(60)
    #捕获事件
    
    #监听事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("游戏退出")
            #调用quit 卸载所有的模块
            pygame.quit()
            exit()
    #2修改飞机的位置
    hero_rect.y -=1
    #判断飞机的位置
    if hero_rect.y <= -126:
        hero_rect.y = 700
    #3.调用screen.blit（）方法绘制图像
    screen.blit(bg,(0,0))#应该先把背景图像重新绘制
    screen.blit(hero,hero_rect)
    #4.更新图像
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            






