import pygame
# Os pega as imagens na pasta imgs
import os
import random

# Constante em python é com a letra maiúscula
TELA_ALTURA = 500
TELA_LARGURA = 800

IMAGEM_CANO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'pipe.png')))
IMAGEM_CHAO = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'base.png')))
IMAGEM_BACKGROUND = pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bg.png')))
IMAGEM_PASSARO = [
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird1.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird2.png'))),
    pygame.transform.scale2x(pygame.image.load(os.path.join('imgs', 'bird3.png')))
]
# Fonte do jogo
pygame.font.init()
FONTE_PONTUACAO = pygame.font.SysFont('arial', 50)

class Passaro:
    IMGS = IMAGEM_PASSARO
    # Rotação do passaro
    ROTACAO_MAXIMA = 25
    VELOCIDADE_ROTACAO = 20
    TEMPO_ANIMACAO = 5

    def __init__(self, x, y):
        # Posição inicial do passaro
        self.x = x
        self.y = y
        # Inicializa o passaro parado
        self.angulo = 0
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.contagem_imagem = 0
        self.imagem = self.IMGS[0]

    def pular(self):
        # Pulo do passaro
        self.velocidade = -10.5
        self.tempo = 0
        self.altura = self.y
    
    def mover(self):
        # Monimento do passaro
        self.tempo += 1
        # Deslocamento
        deslocamento = 1.5 * (self.tempo**2) + self.velocidade * self.tempo
        # Restrição de deslocamento
        if deslocamento > 16:
            deslocamento = 16
        elif deslocamento < 0:
            deslocamento -= 2
        # Movimenta o passaro
        self.y += deslocamento
        # Rotação do passaro
        # Deslocamento < 0 significa que o passaro está subindo
        if deslocamento < 0 or self.y < (self.altura + 50):
            # Rotação máxima
            if self.angulo < self.ROTACAO_MAXIMA:
                self.angulo = self.ROTACAO_MAXIMA
        # Deslocamento > 0 significa que o passaro está descendo
        else:
            # Rotação máxima
            if self.angulo > -90:
                self.angulo -= self.VELOCIDADE_ROTACAO

        def desenhar(self, tela):
            # Animação do passaro
            self.contagem_imagem += 1
            
            if self.contagem_imagem < self.TEMPO_ANIMACAO:
                self.imagem = self.IMGS[0]
            elif self.contagem_imagem < self.TEMPO_ANIMACAO*2:
                self.imagem = self.IMGS[1]
            elif self.contagem_imagem < self.TEMPO_ANIMACAO*3:
                self.imagem = self.IMGS[2]
            elif self.contagem_imagem < self.TEMPO_ANIMACAO*4:
                self.imagem = self.IMGS[1]
            elif self.contagem_imagem >= self.TEMPO_ANIMACAO*4 + 1:
                self.imagem = self.IMGS[0]
                self.contagem_imagem = 0
            # Se o passaro estiver caindo, não bate as asas
            if self.angulo <= -80:
                self.imagem = self.IMGS[1]
                self.contagem_imagem = self.TEMPO_ANIMACAO*2

            # Desenha o passaro
            imagem_rotacionada = pygame.transform.rotate(self.imagem, self.angulo)
            pos_centro_imagem = self.imagem.get_rect(topleft = (self.x, self.y)).center
            retangulo = imagem_rotacionada.get_rect(center=self.imagem.get_rect(center = pos_centro_imagem))
            tela.blit(imagem_rotacionada, retangulo.topleft)

        def get_mask(self):
            return pygame.mask.from_surface(self.imagem)    

class Cano:
    pass

class Chao:
    pass

