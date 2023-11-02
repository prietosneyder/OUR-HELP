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