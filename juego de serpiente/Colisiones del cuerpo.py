#Colisiones del cuerpo
for segmento in segmentos:
        if segmento.distance(cabeza) < 20:
            time.sleep
            cabeza.goto(0,0)
            cabeza.direction = "stop"

            #Esconder los segmentos
            for segmento in segmentos:
                segmento.goto(1000,1000)

            segmentos.clear()

            score = 0
            texto.clear()   
            texto.write("Score: {}    High Score: {}".format(score, high_score), 
                align = "center", font =("Courier", 24, "normal"))
        time.sleep(posponer)