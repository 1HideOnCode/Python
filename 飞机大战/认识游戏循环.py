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


#创建时钟对象
clock = pygame.time.Clock()

#设置游戏循环，意味着游戏正式开始：
i = 0

while True:
    #可以控制游戏循环内部的代码执行频率
    clock.tick(1)
    print(i)
    i +=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()




