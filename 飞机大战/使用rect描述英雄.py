#定义hero_rect矩形描述英雄的位置和大小
#输出英雄的坐标（x和y）
#输出英雄的尺寸（宽度和高度）
import pygame
pygame.init()
hero_rect = pygame.Rect(100,500,120,125)
print("英雄的原点 %d--%d"%(hero_rect.x,hero_rect.y))

print("英雄的尺寸 %d--%d"%(hero_rect.width,hero_rect.height))
pygame.quit()
