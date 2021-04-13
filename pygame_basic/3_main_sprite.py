import pygame

pygame.init() # 초기화 작업(반드시 필요)

#화면 크기 설정
screen_width = 480 #가로 크기
screen_height = 640 #세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Gnadi Game")#게임이름

#배경 이미지 불러오기
background = pygame.image.load("/Users/inwon/Desktop/python_workspace/Python/pygame_basic/background.jpeg")

#스프라이트 불러오기(캐릭터)

# gnadi - 임의로 추가 그림 크기 바꾸는거 연습
# character = pygame.image.load("/Users/inwon/Desktop/python_workspace/Python/pygame_basic/pikachu.png")
# character_scale = pygame.transform.scale(character, (40,40))
# pygame.image.save(character_scale, "/Users/inwon/Desktop/python_workspace/Python/pygame_basic/pikachu2.png")
character = pygame.image.load("/Users/inwon/Desktop/python_workspace/Python/pygame_basic/pikachu2.png")
character_size = character.get_rect().size # 이미지 크기를 구해옴
character_width = character_size[0]#캐릭터 가로
character_height = character_size[1]#캐릭터 세로
character_x_pos = screen_width/2 - character_width/2 # 화면 가로의 절반 크기에 해당하는 곳에 위치
character_y_pos = screen_height-character_height # 화면 세로 크기 가장 아래에 해당하는 곳에 위치

# 이벤트 루프 (창이 꺼지지 않도록...)
running = True #게임이 진행중인지 확인
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생하였는가
        if event.type == pygame.QUIT: #창이 닫히는 이벤트가 발생 하였는가
            running = False #게임이 진행중이 아니다

    #screen.blit(background, (0,0)) #배경 그리기
    screen.fill((0,0,255)) #RGB 값으로 채우기

    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기

    pygame.display.update()#게임 화면 다시 그리기

#pygame 종료
pygame.quit()