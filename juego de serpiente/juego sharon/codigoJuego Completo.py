import pygame, sys
from pygame.locals import *
import time

pygame.init()
pygame.display.set_caption("Math Cubes")
pantalla = pygame.display.set_mode((600, 848))

fondoPortada = pygame.image.load('img/Niveles/Portada.jpg').convert()

fondoNivel_1 = pygame.image.load('img/Niveles/Nivel 1.jpg').convert()
fondoNivel_1_Completado = pygame.image.load('img/Niveles/Nivel 1 COMPLETADO.jpg').convert()

fondoNivel_2 = pygame.image.load('img/Niveles/Nivel 2.jpg').convert()
fondoNivel_2_Completado = pygame.image.load('img/Niveles/Nivel 2 COMPLETADO.jpg').convert()

fondoNivel_3 = pygame.image.load('img/Niveles/Nivel 3.jpg').convert()
fondoNivel_3_Completado = pygame.image.load('img/Niveles/Nivel 3 COMPLETADO.jpg').convert()

fondoNivel_4 = pygame.image.load('img/Niveles/Nivel 4.jpg').convert()
fondoNivel_4_Completado = pygame.image.load('img/Niveles/Nivel 4 COMPLETADO.jpg').convert()

fondoNivel_5 = pygame.image.load('img/Niveles/Nivel 5.jpg').convert()
fondoNivel_5_Completado = pygame.image.load('img/Niveles/Nivel 5 COMPLETADO.jpg').convert()

imgBtnJugar = pygame.image.load('img/Fondos Principales/Boton Jugar.png')
imgBtnSalir = pygame.image.load('img/Fondos Principales/Boton Salir.png')

clickJugar = False

tiempo = pygame.time.Clock()

def Numeros(numero):
    
    if numero == 2:
        return pygame.image.load('img/Fondos Principales/NUM2.png')
        
    elif numero == 4:
        return pygame.image.load('img/Fondos Principales/NUM4.png')
        
    elif numero == 8:
        return pygame.image.load('img/Fondos Principales/NUM8.png')
    
    elif numero == 16:
        return pygame.image.load('img/Fondos Principales/NUM16.png')
        
    elif numero == 32:
        return pygame.image.load('img/Fondos Principales/NUM32.png')
        
    elif numero == 64:
        return pygame.image.load('img/Fondos Principales/NUM64.png')
    
    elif numero == 128:
        return pygame.image.load('img/Fondos Principales/NUM128.png')
    
    elif numero == 0:
        return pygame.image.load('img/Fondos Principales/Simbolo Suma.png')
    
    elif numero == 1: 
        return pygame.image.load('img/Fondos Principales/Simbolo Igual.png')
    
    elif numero == 3:
        return pygame.image.load('img/Fondos Principales/Simbolo Incorrecto.png')
    
class Personaje():

    def __init__(self, nivel):
        
        if nivel == 1:
            self.imgIzq = pygame.image.load('img/Personajes/JasonIzq.png')
            self.imgDer = pygame.image.load('img/Personajes/JasonDer.png')

        elif nivel == 2:
            self.imgIzq = pygame.image.load('img/Personajes/LotzoIzq.png')
            self.imgDer = pygame.image.load('img/Personajes/LotzoDer.png')
            
        elif nivel == 3:
            self.imgIzq = pygame.image.load('img/Personajes/SawIzq.png')
            self.imgDer = pygame.image.load('img/Personajes/SawDer.png')
        
        elif nivel == 4:
            self.imgIzq = pygame.image.load('img/Personajes/PrincesaIzq.png')
            self.imgDer = pygame.image.load('img/Personajes/PrincesaDer.png')
            
        elif nivel == 5:
            self.imgIzq = pygame.image.load('img/Personajes/MarioIzq.png')
            self.imgDer = pygame.image.load('img/Personajes/MarioDer.png')
        
        self.posX = 100
        self.posY = 440
        self.contDer = 0
        self.contIzq = 2
        self.contArriba = 1
        self.contAbajo = 0

    def movIzquierda(self):
        self.contIzq += 1 
        
        if self.contIzq >= 1 and self.contIzq <= 2:
            self.contDer -= 1
            self.posX -= 130
            return self.posX
        
        else:
            self.contIzq -= 1 
            return self.posX
    
    def movDerecha(self):
        self.contDer += 1
        
        if self.contDer >= 1 and self.contDer <= 2:
            self.contIzq -= 1
            self.posX += 130
            return self.posX
    
        else:
            self.contDer -= 1
            return self.posX
    
    def movArriba(self):
        self.contArriba += 1
        
        if self.contArriba == 1:
            self.contAbajo -= 1
            self.posY -= 130
            return self.posY
        
        else: 
            self.contArriba -= 1
            return self.posY
            
    def movAbajo(self):
        self.contAbajo += 1
        
        if self.contAbajo == 1:
            self.contArriba -= 1
            self.posY += 130
            return self.posY
        
        else: 
            self.contAbajo -= 1
            return self.posY
        
class CrearNivel():
    
    listaPosCubos = [(110, 460), (240, 460), (370, 460), (110, 590), (240, 590), (370, 590)]
    listaSumaPos = [(25, 210), (150, 232), (225, 210), (360, 232), (450, 210)]
    
    def __init__(self, objetivo, fondo, fondoCompletado, numIn):
        
        self.objetivo = objetivo
        self.fondo = fondo
        self.fondoCompletado = fondoCompletado
        self.listaNumeros = [numIn, numIn, numIn, numIn, numIn, numIn] 
        self.listaCubos = [Numeros(numIn), Numeros(numIn), Numeros(numIn), Numeros(numIn), Numeros(numIn), Numeros(numIn)] 
        self.listaPosCubos = CrearNivel.listaPosCubos 
        self.listaSuma = [] 
        self.listaSumaPos = CrearNivel.listaSumaPos 
        self.valoresSuma = [] 
        self.contSuma = 0
        self.suma = 0
        self.respuesta = ""
        self.graficarSuma = True
        self.graficarIgual = True
                
    def BorrarOperacion(self, resultado, posNumero):
        
        if resultado == True:

            time.sleep(0.5)
            self.listaNumeros.pop(posNumero)
            self.listaCubos.pop(posNumero)
            
            self.listaNumeros.insert(posNumero, self.suma)
            self.listaCubos.insert(posNumero, Numeros(self.suma))
            
            self.valoresSuma.clear()
            self.listaSuma.clear()
            
            self.respuesta = ""
            self.contSuma = 0
            self.graficarSuma = True
            self.graficarIgual = True
            
        elif resultado == False:

            time.sleep(0.5)            
            self.valoresSuma.clear()
            self.listaSuma.clear()
            self.respuesta = ""
            self.contSuma = 0
            self.graficarSuma = True
            self.graficarIgual = True
            
    def VerificarSuma(self):
        
        self.suma = self.valoresSuma[0] + self.valoresSuma[1]

        if self.suma == 2 or self.suma == 4 or self.suma == 8 or self.suma == 16 or self.suma == 32 or self.suma == 64 or self.suma == 128:
            self.listaSuma.append(Numeros(self.suma))
            self.respuesta = "Correcta"

        else:
            self.listaSuma.append(Numeros(3))
            self.respuesta = "Incorrecta"
  
def main():
    
    global clickJugar
    
    listaNiveles = [CrearNivel(8, fondoNivel_1, fondoNivel_1_Completado, 2), 
                    CrearNivel(16, fondoNivel_2, fondoNivel_2_Completado, 2), 
                    CrearNivel(32, fondoNivel_3, fondoNivel_3_Completado, 4), 
                    CrearNivel(64, fondoNivel_4, fondoNivel_4_Completado, 4), 
                    CrearNivel(128, fondoNivel_5, fondoNivel_5_Completado, 16)]
    
    botonJugar = pygame.Rect(200, 280, 200, 60)
    botonSalir = pygame.Rect(225, 360, 150, 60)
       
    while True:
        
        pantalla.blit(fondoPortada, (0, 0))
        
        mx, my = pygame.mouse.get_pos();
        
        for event in pygame.event.get():
            
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
           
        if event.type == MOUSEBUTTONDOWN:
            
            if event.button == 1 and botonJugar.collidepoint((mx, my)):
                clickJugar = True
            
            elif event.button == 1 and botonSalir.collidepoint((mx, my)):
                pygame.quit()
                sys.exit(0)
            
        if botonJugar.collidepoint((mx, my)):
            
            if clickJugar:
                clickJugar = False
                
                for i in range(len(listaNiveles)):
                    abandonar = Nivel(listaNiveles[i], i + 1)
                    time.sleep(0.3)
                                     
                    if abandonar == True:
                        break
                                   
                listaNiveles = [CrearNivel(8, fondoNivel_1, fondoNivel_1_Completado, 2), 
                                CrearNivel(16, fondoNivel_2, fondoNivel_2_Completado, 2), 
                                CrearNivel(32, fondoNivel_3, fondoNivel_3_Completado, 4), 
                                CrearNivel(64, fondoNivel_4, fondoNivel_4_Completado, 4), 
                                CrearNivel(128, fondoNivel_5, fondoNivel_5_Completado, 16)]
                time.sleep(0.3)

        pantalla.blit(imgBtnJugar, (200, 280))
        pantalla.blit(imgBtnSalir, (200, 360))
        
        pygame.display.update()
        
        tiempo.tick(60)
           
def Nivel(nivel, nivelPersonaje):
    CorrerNivel = True
    
    personaje = Personaje(nivelPersonaje)
    imgPersonaje = personaje.imgDer
    posX = personaje.posX
    posY = personaje.posY
       
    cubos = [pygame.Rect(110, 460, 120, 120), 
             pygame.Rect(240, 460, 120, 120), 
             pygame.Rect(370, 460, 120, 120),
             pygame.Rect(110, 590, 120, 120),
             pygame.Rect(240, 590, 120, 120),
             pygame.Rect(370, 590, 120, 120)]
    
    posNumero = 6
        
    while CorrerNivel:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
                
            elif event.type == KEYDOWN:
                           
                if event.key == K_LEFT:
                    posX = personaje.movIzquierda()
                    imgPersonaje = personaje.imgIzq
        
                elif event.key == K_RIGHT:
                    posX = personaje.movDerecha()
                    imgPersonaje = personaje.imgDer
        
                elif event.key == K_UP:
                    posY = personaje.movArriba()
        
                elif event.key == K_DOWN:
                    posY = personaje.movAbajo()
                    
                elif event.key == K_ESCAPE:
                        CorrerNivel = False
                        return True
                    
                    
        teclaPresionada = pygame.key.get_pressed()
        for i in range(len(cubos)):
            if cubos[i].collidepoint((posX + 15, posY + 25)):
                if teclaPresionada[pygame.K_RETURN]:
                        
                        if i != posNumero:
                            posNumero = i
                            nivel.listaSuma.append(nivel.listaCubos[i])
                            nivel.valoresSuma.append(nivel.listaNumeros[i])
                            
                            nivel.contSuma += 1
                        else:
                            pass
                        
                        time.sleep(0.3)
                                
        if nivel.contSuma == 1 and nivel.graficarSuma == True:
            nivel.listaSuma.append(Numeros(0))
            nivel.graficarSuma = False
            
        elif nivel.contSuma == 2 and nivel.graficarIgual == True:
            
            nivel.listaSuma.append(Numeros(1))
            nivel.graficarIgual = False
            
            nivel.VerificarSuma()
            
            
        pantalla.blit(nivel.fondo, (0, 0)) #dibuja el fondo
        
        for i in range(len(nivel.listaCubos)): 
            pantalla.blit(nivel.listaCubos[i], nivel.listaPosCubos[i]) #Dibuja los 6 cubos principales
        
        for i in range(len(nivel.listaSuma)):
            pantalla.blit(nivel.listaSuma[i], nivel.listaSumaPos[i]) #Dibuja los cubos de operacion
        
        pantalla.blit(imgPersonaje, (posX, posY)) #Dibuja el personaje
        
        pygame.display.update() 

        if nivel.respuesta == "Correcta":
            nivel.BorrarOperacion(True, posNumero)
            posNumero = 6
            
        elif nivel.respuesta == "Incorrecta":
            nivel.BorrarOperacion(False, posNumero)
            posNumero = 6
            
        if nivel.suma == nivel.objetivo:
            CorrerNivel = False
            pantalla.blit(nivel.fondoCompletado, (0, 0))
            pygame.display.update() 
            time.sleep(1)
            
        tiempo.tick(60)
        
if __name__ == '__main__':
    main()
    
