import pygame
from pygame.locals import *
from random import randint

# improta o personagem principal
from character import elegy

# inicia o pygame
pygame.init()

# seta o tamanho da tela e o nome do jogo
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("RPG")

fonte = pygame.font.SysFont('arial', 50, False, False)

musica = pygame.mixer.music.load('Beneath Cowdenbeath.mp3')
pygame.mixer.music.play(-1)

pygame.mixer.music.set_volume(0.01)

sound_colision = pygame.mixer.Sound("smw_lava_bubble.wav")

x_player = 600/2 - 50/2
y_player = 600/2 - 50/2
velocidade = 3
clock = pygame.time.Clock()

x_enemy = randint(50,500)
y_enemy = randint(50,500)

pontuação = 0

# ultima direção olhada
last_direction = "up"

running = True

while running:
    clock.tick(100)

    mensagem_pontos = f'Pontos: {pontuação}'

    texto_pontos = fonte.render(mensagem_pontos, True, (0,0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        keys = pygame.key.get_pressed()  # Verificar o estado das teclas
    if keys[K_w]:
        y_player -= velocidade
        last_direction = "up"
            
    if keys[K_a]:
        x_player -= velocidade  
        last_direction = "left"

    if keys[K_s]:
        y_player += velocidade
        last_direction = "down"

    if keys[K_d]:
        x_player += velocidade
        last_direction = "right"

    screen.fill(((34,139,34)))
    
    # enemy
    enemy = pygame.draw.rect(screen, (178,34,34), (x_enemy, y_enemy, 50, 50)) # tela / cor / posição, proporção

    # player
    player = pygame.draw.circle(screen, (245,222,179), (x_player, y_player), 30) # tela / cor / posição, proporção

    if last_direction == "up":
        espada = pygame.draw.rect(screen, (139, 69, 19), (x_player - 1, y_player - 100, 5, 70))
        grip = pygame.draw.rect(screen, (128, 128, 128), (x_player - 5, y_player - 40, 13, 5))

    elif last_direction == "down":
        espada = pygame.draw.rect(screen, (139, 69, 19), (x_player - 1, y_player + 30, 5, 70))
        grip = pygame.draw.rect(screen, (128, 128, 128), (x_player - 5, y_player + 35, 13, 5))

    elif last_direction == "left":
        espada = pygame.draw.rect(screen, (139, 69, 19), (x_player - 100, y_player - 1, 70, 5))
        grip = pygame.draw.rect(screen, (128, 128, 128), (x_player - 40, y_player - 5, 5, 13))

    elif last_direction == "right":
        espada = pygame.draw.rect(screen, (139, 69, 19), (x_player + 30, y_player - 1, 70, 5))
        grip = pygame.draw.rect(screen, (128, 128, 128), (x_player + 35, y_player - 5, 5, 13))

    # Interface
    pygame.draw.line(screen, (255,255,255), (0,0), (600,0), (100))

    if x_player > 600:
        x_player = 0

    if x_player < 0:
        x_player = 600

    if y_player > 600:
        y_player = 50
    
    if y_player < 50:
        y_player = 600

    if espada.colliderect(enemy):
        x_enemy = randint(50,500)
        y_enemy = randint(50,500)
        pontuação += 1
        sound_colision.play()

    screen.blit(texto_pontos,(50,0))

    pygame.display.update()

pygame.quit()