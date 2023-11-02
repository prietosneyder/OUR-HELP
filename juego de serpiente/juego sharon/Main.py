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
        
if __name__ == '__main__':
    main()