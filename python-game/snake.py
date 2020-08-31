import pygame
import time
import random

pygame.init()                                               #Khởi tạo

#pygame.display.update()                                     #update() cập nhật bất kì 'thay đổi' nào trên màn hình
pygame.display.set_caption('Snake game by Thu')

white = (255,255,255)
yellow = (255,255,102)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

dis_width = 600
dis_height = 400

snake_block = 10
snake_speed = 10

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

dis = pygame.display.set_mode((dis_width,dis_height))
clock = pygame.time.Clock()


def ourSnake(snake_block, snake_list,snake_head):
    #1 object cuar snake_list có 2 tọa độ x,y
    #nhiều object taoj thành độ dài con rắn
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
        pygame.draw.rect(dis, red, [snake_head[0], snake_head[1], snake_block, snake_block])


def message(msg,x,y,color):
    mess = font_style.render(msg, True, color)
    dis.blit(mess,[x,y])

def score(score):
    value = score_font.render("Score:  " + str(score), True, yellow)
    dis.blit(value,[int(dis_width/3),0])

def gameLoop():
    game_over = False
    game_close = False
    #vị trí ban đầu
    x1 = int(dis_width/2)
    y1 = int(dis_height/2)
    x1_change = 0
    y1_change = 0

    snake_list = []
    lengthOfSnake = 1
    #vị trí con mồi ngẫu nhiên 
    foodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
    foody = int(round(random.randrange(30, dis_height - snake_block) / 10.0) * 10.0)
    print(foodx,foody)

    while not game_over:
        while game_close == True:
            dis.fill(blue)
            score(lengthOfSnake-1)
            message("Game Over!", 250, 120, red)
            message("Nhấn [Q - Thoát] hoặc nhấn [C - Chơi lại]", 150, 200, red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            #print(event)                                        #In ra tất cả các hành động trên màn hình
            if event.type == pygame.QUIT:                        #Khi nhấn 'x' sẽ thoát
                game_over = True
            
            #Thiết lập giá trị hướng => cứ loop là tự động trừ
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN:
                    x1_change = 0
                    y1_change = snake_block
        
        #Chạm tường thì chuyển đến game_close window
        
        if x1 >= dis_width or x1 < 0 or y1>=dis_height or y1<0:
            game_close = True

        #di chuyển vị trí khi loop
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        pygame.draw.rect(dis,green,[foodx,foody,snake_block,snake_block])
        #vị trí đầu rắn
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        #Cả con rắn
        snake_list.append(snake_head)

        #print(snake_list)
        
        if len(snake_list) >lengthOfSnake:
             del snake_list[0]
        #print(snake_list)
        #Khi đầu chạm rắn thì chuyển đến vòng lặp game_close
        for x in snake_list[:-1]:
            if x== snake_head:
                game_close = True
                print("ahiiii")
        
        #vẽ con rắn ra
        ourSnake(snake_block,snake_list,snake_head)
        score(lengthOfSnake-1)
        pygame.display.update()

        #tạo mồi mới và tăng chiều dài con rắn
        if x1 == foodx and y1 == foody:
            foodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
            foody = int(round(random.randrange(30, dis_height - snake_block) / 10.0) * 10.0)
            lengthOfSnake += 1

        clock.tick(snake_speed)                                          #speed snake

    pygame.quit()                                               
    quit()                                                      #Hủy khời tạo

gameLoop()