from random import*
from turtle import*

setup(1350,690,0,0)
delay(0)


lista_de_tartarugas = []
global valor

def criador_de_tartarugas():
    T = Turtle()
    T.hideturtle()
    T.penup()
    T.left(90)
    lista_de_tartarugas.append(T)

def criar_novas_tartarugas():

    while (len(lista_de_tartarugas) <= 29):
        criador_de_tartarugas()
        
def estah_perto(lista,y1, y2, i):

    
        Y = abs(y1 - y2)
        print("y1:   ", y1)
        print("y2:   ", y2)
        
        
        if (i==0):
            tart_0 = lista[i]
            tart_0.setheading(90)
        else:
            if Y > 40:
                valor = 1
                return valor
            else:
                valor = 0
                #print("Valor:  ",valor)
                return valor
                
        
def andar_tartaruga(lista):
    
    criar_novas_tartarugas()
    
    for k in range(len(lista)):
        global tart_anterior, tart_atual, y_anterior, y_atual, Y
        tart_anterior = lista[k-1]
        tart_atual = lista[k]
        y_anterior = tart_anterior.ycor()
        y_atual = tart_atual.ycor()
        
        estah_perto(lista_de_tartarugas, y_anterior, y_atual, k)
        
        while (estah_perto(lista_de_tartarugas, y_anterior, y_atual, k) == 0):
            tart_anterior.showturtle()
            tart_anterior.fd(randint(0,10))
            estah_perto(lista_de_tartarugas, y_anterior, y_atual, k)

            if (estah_perto(lista_de_tartarugas, y_anterior, y_atual, k) == 1):
                tart_atual.showturtle()
                tart_atual.fd(randint(0,10))
                return 1
    
def chegou_no_fim():
    
    andar_tartaruga(lista_de_tartarugas)
    while True:

        if (y_atual < 100):
            andar_tartaruga(lista_de_tartarugas)
            
            
        elif (y_anterior > 100):
            tart_anterior.hideturtle()
            lista_de_tartarugas.remove(lista_de_tartarugas[0])
            criador_de_tartarugas()
            
            
            
        else:
            tart_atual.hideturtle()
            lista_de_tartarugas.remove(tart_atual)
            criador_de_tartarugas()
            
    

def mudar_indice(tart):
    tart = lista_de_tartarugas[0]
        

chegou_no_fim()
