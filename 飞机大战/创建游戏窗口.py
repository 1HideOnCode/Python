import pygame
pygame.init()
#创建游戏窗口480*700
scream = pygame.display.set_mode((480,700))#set_mode()返回创建的游戏屏幕
#set_mode(resolution=(0,0),flags = 0,depth=0)->surface
#resolution是一个元组类型，第一个值是希望建立的窗口宽度，第二个值是窗口高度
#flags可以指定一些创建窗口的附加选项，例如是否需要全屏，是否需要边框
#depth表示颜色的位数，默认会自动匹配
#set_mode一般就只要吧窗口的宽和高设置好就行了
while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

