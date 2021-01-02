from tkinter import *
import os
from threading import Thread
import threading
import time
import random
from random import shuffle 
from pygame import mixer
from PIL import ImageTk, Image
#Funcion que carga las imagenes, se le da la ruta actual. 
def cImagen(archivo):   
    ruta =os.path.join("Imgs",archivo)
    imagen=PhotoImage(file=ruta)
    return imagen
#Ventana y canvas principal
ventana=Tk()
ventana.title('Pantalla de incio')
ventana.minsize(1000,700)
ventana.resizable(width=NO, height=NO)

C_principal=Canvas(ventana,width=1000,height=700, bg='white')
C_principal.place(x=0,y=0)

Bullethead=Label(C_principal,text="BATTLE: AVATARS Vs ROOKS",width=30,height=5,bg='red',fg='white')
Bullethead.place(x=500,y=25)
#####################################################Ventana de ayuda##################################################################################
def abrirventaA():
    global top
    global TIME
    top= Toplevel()
    top.title('Ventana de highscore')
    top.minsize(1000,700)
    top.resizable(width=NO, height=NO)
    Canvas_creditos=Canvas(top,width=1000,height=700, bg='white')
    Canvas_creditos.place(x=0,y=0)
    Canvas_creditos.image2=cImagen("Wallpaper.png")
    imgcanvas2=Canvas_creditos.create_image(0,0,anchor=NW,image=Canvas_creditos.image2)
    boto=Button(top,text='volver a menu',command=c)
    def updatefile2():
        f1=open('scores.txt','r')
        file2=f1.readlines()
        last2=str(file2)
        x=sorted(file2,reverse=True)
        print(x)
        a=prod_escalar(x)
        a.sort(reverse=False)
        print(a)
        higscore=Label(top,text="High score1 :"+str(a[0]),bg="red",font=("Arial bold",15),fg='white')
        higscore.place(x=500,y=0)
        higscore1=Label(top,text="High score2:"+str(a[1]),bg="red",font=("Arial bold",15),fg='white')
        higscore1.place(x=500,y=100)
        higscore2=Label(top,text="High score3:"+str(a[2]),bg="red",font=("Arial bold",15),fg='white')
        higscore2.place(x=500,y=200)
        higscore3=Label(top,text="High score4:"+str(a[3]),bg="red",font=("Arial bold",15),fg='white')
        higscore3.place(x=500,y=300)
        higscore4=Label(top,text="High score5:"+str(a[4]),bg="red",font=("Arial bold",15),fg='white')
        higscore4.place(x=500,y=400)
    def prod_escalar(vec1):
        return prod_escalar_aux(vec1,0,len(vec1),[])

    def prod_escalar_aux(vec1,i,n,vecr):
        if i==n:
            return vecr
        else:
            vecr.append(int(vec1[i]))
            return prod_escalar_aux(vec1,i+1,n,vecr)
    updatefile2()
    boto.place(x=500,y=620)
    ventana.withdraw()
def c():
    ventana.deiconify()
    top.destroy()
    
#Ventana de ayuda
def abrirayuda():
    global top
    top= Toplevel()
    top.title('Ventana de ayuda')
    top.minsize(1000,700)
    top.resizable(width=NO, height=NO)
    Canvas_ayuda=Canvas(top,width=1000,height=700, bg='white')
    Canvas_ayuda.place(x=0,y=0)
    Canvas_ayuda.image2=cImagen("Wallpaper.png")
    imgcanvas2=Canvas_ayuda.create_image(0,0,anchor=NW,image=Canvas_ayuda.image2)
    boto=Button(top,text='volver a menu',command=close)
    boto.place(x=500,y=620)
    label1=Label(top,text="Instrucciones generales",bg="red",font=("Arial bold",10),fg='white')
    label1.place(x=400,y=35)
    label2=Label(top,text="Para escoger un Rook se debe primero hacer click izquierdo \n luego dejamos presionado el click y soltamos en la matriz que queramos ",bg="red",font=("Arial bold",10),fg='white')    
    label2.place(x=400,y=100)
    label3=Label(top,text="Nota: Centra bien la matriz en la casilla",bg="red",font=("Arial bold",10),fg='white')
    label3.place(x=400,y=200)
    label4=Label(top,text="El objetivo del juego es que los avatares no lleguen a la última fila del tablero",bg="red",font=("Arial bold",10),fg='white')          
    label4.place(x=400,y=300)
    label5=Label(top,text="Para mas información leer el README.TXT",bg="red",font=("Arial bold",10),fg='white')          
    label5.place(x=400,y=400)
    ventana.withdraw()
def close():#Cuando se quiere cerrar la ventana y devolverse a la pantalla de incio 
    ventana.deiconify()
    top.destroy()
    
#############################################################################Ventana de créditos#######################################################    
def abrircreditos():
    global top2
    top2=Toplevel()
    top2.title('Ventana de Créditos')
    top2.minsize(1000,700)
    top2.resizable(width=NO, height=NO)
    Canvas_creditos=Canvas(top2,width=1000,height=700, bg='white')
    Canvas_creditos.place(x=0,y=0)
    Canvas_creditos.image2=cImagen("Wallpaper.png")
    imgcanvas2=Canvas_creditos.create_image(0,0,anchor=NW,image=Canvas_creditos.image2)
    boto2=Button(top2,text='volver a menu',command=close_creditos)
    Canvas_creditos.image3=cImagen("foto.png")
    imgcanvas3=Canvas_creditos.create_image(0,100,anchor=NW,image=Canvas_creditos.image3)
    boto2.place(x=500,y=620)
    label1=Label(top2,text="Pais de produccíon:Costa Rica",bg="red",font=("Arial bold",10),fg='white')
    label1.place(x=400,y=35)
    label2=Label(top2,text="Universidad: Instituto Tecnológico de Costa Rica",bg="red",font=("Arial bold",10),fg='white')
    label2.place(x=400,y=100)
    label3=Label(top2,text="Carrera:Ingeniería en Computadores ",bg="red",font=("Arial bold",10),fg='white')
    label3.place(x=400,y=200)
    label4=Label(top2,text="Año:2020,Grupo:01,Versión=1.2del programa",bg="red",font=("Arial bold",10),fg='white')          
    label4.place(x=400,y=300)
    label5=Label(top2,text="Profesor:Jeff Schmidt Peralta",bg="red",font=("Arial bold",10),fg='white')
    label5.place(x=400,y=400)
    label6=Label(top2,text="Autor: Jose Pablo Ramos Madrigal",bg="red",font=("Arial bold",10),fg='white')
    label6.place(x=400,y=500)
    ventana.withdraw()   
def close_creditos():
    ventana.deiconify()
    top2.destroy()
###################################Ventana de login y registro y Funciones###################
def register():
    global username
    global username_entry
    register_screen = Toplevel(ventana) 
    register_screen.title("Register")
    register_screen.geometry("300x250")
    username = StringVar()
    Label(register_screen, text="Please enter details below").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    Button(register_screen, text="Register", width=10, height=1,command=register_user).pack()
#Esta obtiene el nombre del entry y crea un archivo txt 
def register_user():
    #global register_screen
    username_info = username.get()
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.close()
    username_entry.delete(0, END)
    Label_resgistro=Label(ventana,text="User name:"+ username_info,bg='red',font=('Calibri',10),fg='white')
    Label_resgistro.place(x=100,y=400)
 #Luego de hacer el register se debe hacer el login para que el nombre aparezca en la pantalla    
def login():
    global login_screen
    login_screen = Toplevel(ventana)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
    global username_verify
    username_verify = StringVar()
    global username_login_entry
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verify).pack()
def login_verification():
    print("working...")


def login_verify():
    global username1
    username1 = username_verify.get()
    username_login_entry.delete(0, END)
    list_of_files = os.listdir()  
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        L=Label(ventana,text="User name:"+username1,bg='red',font=('Calibri',10),fg='white')
        L.place(x=100,y=400)
        login_sucess()
    else:
        user_not_found()

def login_sucess():
    global login_success_screen   # make login_success_screen global
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()


def delete_login_success():
    login_success_screen.destroy()

def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()

def delete_user_not_found_screen():
    user_not_found_screen.destroy()
#################################################################################Fin de ventanas de login y registro################################################################
####################################################################################################################################################################################
#####################################################################Ventana de juego###############################################################################################
#Primero definimos el canvas la ventana y la variables globales
global coin
global TIME
coin=2000
TIME=0
def juego():
    global top3
    global a1
    global c
    top3=Toplevel()
    top3.title('Ventana de Juego')
    top3.minsize(1000,700)
    top3.resizable(width=NO, height=NO)
    c=Canvas(top3,width=1000,height=700,bg='white')
    c.place(x=0,y=0)
    b=Button(top3,text='volver a menu',command=close_juegos)
    b.place(x=500,y=650)
    Label23=Label(top3,text="User name:"+username1,bg='red',font=('Calibri',10),fg='white')
    Label23.place(x=875,y=65)
    #Variables 
    OPEN=True
    #Posiciones inciales tablero 
    y=135
    y2=232
    y3=315
    y4=410
    y5=486
    y6=565
    #Lista de posiciones en el tablero 
    list_posiciones=[y,y2,y3,y4,y5,y6]
    random.shuffle(list_posiciones)
    pos1=list_posiciones[0]
    pos2=list_posiciones[1]
    pos3=list_posiciones[2]
    pos4=list_posiciones[3]
    pos5=list_posiciones[4]
    pos6=list_posiciones[5]
    ##lISTA DE IMAGENES RANDOM
    lis_avatars=["avatar escudero.png","avatar caníbal.png","avatar leñador.png","avatar flechero.png"]
    random.shuffle(lis_avatars)
    ava=lis_avatars[0]
    ava2=lis_avatars[1]
    ava3=lis_avatars[2]
    ava4=lis_avatars[3]
    ###########################
    global img
    global water1
    global my_img1
    #Imagen del tablero
    Tablero=cImagen("t.png")
    Tablerol=c.create_image(0,0,anchor=NW,image=Tablero)
    #Imagen de torres
    img=PhotoImage(file="Imgs\\sand1.png")
    my_img1=c.create_image(100,5,anchor=NW,image=img)
    #------
    rock=cImagen("rock.png")
    rock1=c.create_image(300,5,anchor=NW,image=rock)
    #---
    global fire 
    fire=cImagen("fire.png")
    fire1=c.create_image(500,5,anchor=NW,image=fire)
    #-----
    water=cImagen("water.png")
    water1=c.create_image(700,5,anchor=NW,image=water,tags='rook1')
    global avatar55

    #Imagenes de avatars
    avatar=cImagen('avatar leñador.png')
    avatar1=c.create_image(900,pos1,anchor=CENTER,image=avatar,tags='f1')
    #--------
    avatar2=cImagen('avatar flechero.png')
    avatar22=c.create_image(900,pos2,anchor=CENTER,image=avatar2,tags='f2')
    #--------
    avatar3=cImagen('avatar escudero.png')
    avatar33=c.create_image(900,pos3,anchor=CENTER,image=avatar3,tags='f3')
    #----
    avatar4=cImagen('avatar caníbal.png')
    avatar44=c.create_image(900,pos4,anchor=CENTER,image=avatar4,tags='f4')
    #----
    avatar5=cImagen('avatar flechero.png')
    avatar55=c.create_image(900,pos6,anchor=CENTER,image=avatar5,tags='f5')

    #Cagar imagenes de monedas
    global coin50
    global coin25
    global coin100
    global monedas
    coin50=cImagen('50 coin.png')
    coin25=cImagen('25 coin.png')
    coin100=cImagen('100 coin.png')
    
    monedas=[coin50,coin25,coin100]
    def crearcoin():
        global coin50
        global coin25
        global coin100
        global monedas
        global imaggg
        random.shuffle(monedas)
        imaggg=c.create_image(random.randint(100,600),random.randint(300,600),anchor=CENTER,image=monedas[0],tags=str(monedas[0]))
        top3.after(10000,lambda:crearcoin())
    Thread(target=crearcoin).start()

    ####################################################################################
    global imaggg
    #Creear imagenes de proyectiles
    ########################################Puedo usar la misma variable###################################################################
    bala3=cImagen("axe.png")
    bala4=c.create_image(0,0,image=bala3,tags='B',state=HIDDEN)
    
    flecha=cImagen("arrow.png")
    flecha1=c.create_image(0,0,image=flecha,tags='flecha',state=HIDDEN)

    espada=cImagen("sword.png")
    espada1=c.create_image(0,0,image=espada,tags='espada',state=HIDDEN)
    
    garrote=cImagen("garrote.png")
    garrote1=c.create_image(0,0,image=garrote,tags='garrote',state=HIDDEN)
    
    ###############################################################################################
    bullet=cImagen("fire ball.png")
    #bullet1=c.create_image(0,0,image=bullet,tags='bullet',state=HIDDEN)

    proyectil=cImagen("spikeball.png")

    proyectil2=cImagen("Water ball.png")

    def printt(event):
        print(event.x,event.y)

    c.bind("<ButtonPress-2>",printt)
    #########################################################################################################################################
    #----------------------------------------------------------------IMGS------------------------------------------------------------------------
    global var
    #global coin
    global laelcoi
    #coin=1000
    var=0
    labelcoi=Label(top3,text="Coins" +str(coin))
    labelcoi.place(x=920,y=30)
    #Funcion que establece si el usuario hizo un click en la pantalla y esta cerca de los enemigos
    #Luego cambia la variable var al tipo de torre que es 
    def mouse_acc(event):
        global var
        global coin
        global imaggg
        rango=c.bbox(my_img1)#Sand rook
        rang=c.bbox(rock1)
        rang1=c.bbox(fire1)
        rang2=c.bbox(water1)
        rang3=c.bbox(imaggg)
        if event.x >=rango[0] and event.x < (rango[2]):
            if event.y >= rango[1] and event.y <(rango[3]):#Hago lo mismo nada mas que con otra imagen y con las variables 
                var=1
                coin=coin-50
                labelcoi.config(text="Coins"+str(coin))
        if event.x >=rang[0] and event.x < (rang[2]):#2
            if event.y >= rang[1] and event.y <(rang[3]):
                var=2
                coin=coin-100
                labelcoi.config(text="Coins"+str(coin))
        if event.x >=rang1[0] and event.x < (rang1[2]):#3
            if event.y >= rang1[1] and event.y <(rang1[3]):
                var=3
                coin=coin-150
                labelcoi.config(text="Coins"+str(coin))
        if event.x >=rang2[0] and event.x < (rang2[2]):#4
            if event.y >= rang2[1] and event.y <(rang2[3]):
                var=4
                coin=coin-200
                labelcoi.config(text="Coins"+str(coin))
        if event.x >=rang3[0] and event.x < (rang3[2]):#4
            if event.y >= rang3[1] and event.y <(rang3[3]):
                if str(monedas[0])==str(coin50):
                    coin=coin+50
                    labelcoi.config(text="Coins"+str(coin))
                    var=5
                if str(monedas[0])==str(coin25):
                    coin=coin+25
                    labelcoi.config(text="Coins"+str(coin))
                    var=5
                if str(monedas[0])==str(coin100):
                    coin=coin+100
                    labelcoi.config(text="Coins"+str(coin))
                    var=5    
    global listadetorres
    global listadetorres1
    global listadetorres2#Las listas donde se almacenan las posiciones e imagenes de la torres 
    listadetorres=[]
    listadetorres1=[]
    listadetorres2=[]
    def colocar_torre(event):#Para hacer otras imagenes cambio la variables 
        global var
        global coin
        global imgz
        if var==1:#Aqui la variable se compara y si es igual a 1,2,3,4 o 5 genera un diferente accion 
            c.create_image(event.x,event.y,anchor=CENTER,image=img,state=NORMAL,tags='aaa'+str(len(listadetorres)))
            listadetorres.append(c.create_image(event.x,event.y,anchor=CENTER,image=img,state=NORMAL,tags='aaa'+str(len(listadetorres))))
            proyectiles()
            c.update()
            var=0
        if var==2:
            c.create_image(event.x,event.y,anchor=CENTER,image=rock,state=NORMAL,tags='aaa'+str(len(listadetorres)))
            listadetorres.append(c.create_image(event.x,event.y,anchor=CENTER,image=rock,state=NORMAL,tags='aaa'+str(len(listadetorres))))
            proyectiles()
            c.update()
            var=0
        if var==3:
            c.create_image(event.x,event.y,image=fire,state=NORMAL,tags='ccc'+str(len(listadetorres1)))
            listadetorres1.append(c.create_image(event.x,event.y,image=fire,state=NORMAL,tags='ccc'+str(len(listadetorres1))))
            proyectiles2()
            c.update()
            var=0
        if var==4:
            c.create_image(event.x,event.y,anchor=CENTER,image=water,tags='torre'+str(len(listadetorres2)))
            listadetorres2.append(c.create_image(event.x,event.y,anchor=CENTER,image=water,tags='torre'+str(len(listadetorres2))))
            proyectiles3()
            c.update()
            var=0
        if var==5:
            c.delete(imaggg)
            c.update()
            var=0
    #Se define el evento en el canvas 
    c.bind("<ButtonPress-1>",mouse_acc)
    c.bind("<ButtonRelease-1>",colocar_torre)

    #Colisiones entre las torres
    global vida_torre
    global vida_torre2
    global vida_torres3 #Definimos la vida de las torres 
    vida_torre=20
    vida_torre2=16
    vida_torres3=25
    def eliminar():
        global vida_torre
        if len(listadetorres1)>=1:#Si el largo de la lista es mayor a 1 pues que empiece el recorrido del juego 
            for b in range(0,len(listadetorres1)):#El recorrido del la lista de torrres 
                bx=c.bbox("espada")
                bx1=c.bbox("garrote")
                bx2=c.bbox("B")
                bx3=c.bbox("flecha")
                bx4=c.bbox("flecha2")
                sbx=c.bbox(listadetorres1[b])
                if (bx1[2]in range ((sbx[0]),(sbx[2]-99))) and  ((bx1[1] in range(sbx[1],sbx[3]))):#Esto compara las posciones de la torres con los proyectiles de los avatars 
                    vida_torre-=4
                    vidas_torres()
                if (bx[2]in range ((sbx[0]),(sbx[2]-99))) and ((bx[1] in range(sbx[1],sbx[3]))):
                    vida_torre-=2
                    vidas_torres()
                if (bx2[2]in range ((sbx[0]),(sbx[2]-99))) and ((bx2[1] in range(c.bbox(listadetorres1[b])[1],c.bbox(listadetorres1[b])[3]))):
                    vida_torre-=3
                    vidas_torres()
                if (bx3[2]in range ((sbx[0]),(sbx[2]-98))) and ((bx3[1] in range(c.bbox(listadetorres1[b])[1],c.bbox(listadetorres1[b])[3]))):
                    vida_torre-=1
                    vidas_torres()
                if (bx4[2]in range ((sbx[0]),(sbx[2]-98))) and ((bx4[1] in range(c.bbox(listadetorres1[b])[1],c.bbox(listadetorres1[b])[3]))):
                    vida_torre-=1
                    vidas_torres()
                            
        if OPEN==TRUE:#esta variable hace que se haga la recursion con el after y el lambda 
            top3.after(1,lambda:eliminar())
    t1=Thread(target=eliminar)
    t1.start()#Iniciamos el thread
    
    def eliminar_torres():#Esta funcion es similar a la de eliminar() nada mas que se hace con otra lista de torres 
        global vida_torre2
        if len(listadetorres)>=1:
            for b in range(0,len(listadetorres)):
                bx=c.bbox("espada")
                bx1=c.bbox("garrote")
                bx2=c.bbox("B")
                bx3=c.bbox("flecha")
                bx4=c.bbox("flecha2")
                sbx=c.bbox(listadetorres[b])
                if (bx1[2]in range ((sbx[0]),(sbx[2]-99))) and  ((bx1[1] in range(sbx[1],sbx[3]))):
                    vida_torre2-=4
                    vidas_torres()
                if (bx[2]in range ((sbx[0]),(sbx[2]-99))) and ((bx[1] in range(sbx[1],sbx[3]))):
                    vida_torre2-=2
                    vidas_torres()
                if (bx2[2]in range ((sbx[0]),(sbx[2]-99))) and ((bx2[1] in range(c.bbox(listadetorres[b])[1],c.bbox(listadetorres[b])[3]))):
                    vida_torre2-=3
                    vidas_torres()
                if (bx3[2]in range ((sbx[0]),(sbx[2]-98))) and ((bx3[1] in range(c.bbox(listadetorres[b])[1],c.bbox(listadetorres[b])[3]))):
                    vida_torre2-=1
                    vidas_torres()
                if (bx4[2]in range ((sbx[0]),(sbx[2]-98))) and ((bx4[1] in range(c.bbox(listadetorres[b])[1],c.bbox(listadetorres[b])[3]))):
                    vida_torre2-=1
                    vidas_torres()
        if OPEN==TRUE:
            top3.after(1,lambda:eliminar_torres())
        
    t2=Thread(target=eliminar_torres)
    t2.start()#iniciamos el thread 
    def eliminar_torres2():#Esta funcion es similar a la de eliminar() nada mas que se hace con otra lista de torres 
        global vida_torres3
        if len(listadetorres2)>=1:
            for b in range(0,len(listadetorres2)):
                bx=c.bbox("espada")
                bx1=c.bbox("garrote")
                bx2=c.bbox("B")
                bx3=c.bbox("flecha")
                bx4=c.bbox("flecha2")
                sbx=c.bbox(listadetorres2[b])
                if (bx1[2]in range ((sbx[0]),(sbx[2]-99))) and  ((bx1[1] in range(sbx[1],sbx[3]))):
                    vida_torres3-=4
                    vidas_torres()
                if (bx[2]in range ((sbx[0]),(sbx[2]-99))) and ((bx[1] in range(sbx[1],sbx[3]))):
                    vida_torres3-=2
                    vidas_torres()
                if (bx2[2]in range ((sbx[0]),(sbx[2]-99))) and ((bx2[1] in range(c.bbox(listadetorres2[b])[1],c.bbox(listadetorres2[b])[3]))):
                    vida_torres3-=3
                    vidas_torres()
                if (bx3[2]in range ((sbx[0]),(sbx[2]-98))) and ((bx3[1] in range(c.bbox(listadetorres2[b])[1],c.bbox(listadetorres2[b])[3]))):
                    vida_torres3-=1
                    vidas_torres()
                if (bx4[2]in range ((sbx[0]),(sbx[2]-98))) and ((bx4[1] in range(c.bbox(listadetorres2[b])[1],c.bbox(listadetorres2[b])[3]))):
                    vida_torres3-=1
                    vidas_torres()
        if OPEN==TRUE:
            top3.after(1,lambda:eliminar_torres2())
    t3=Thread(target=eliminar_torres2)
    t3.start()
    def vidas_torres():#Si la vida de la torre es menor que cero pues que mueva ese elemento de la lista fuera del canvas. No se hizo un pop o eliminar la imagen, porque 
        global vida_torre# me causo problemas esa alternativa 
        global vida_torre2
        global vida_torres3
        if vida_torre<=0:
            c.move(c.gettags(listadetorres1[len(listadetorres1)-1]),40000,40000)
            vida_torre=10
            c.update()
        if vida_torre2<=0:
            c.move(c.gettags(listadetorres[len(listadetorres)-1]),20000,20000)
            vida_torre2=7
            c.update()
        if vida_torres3<=0:
            c.move(c.gettags(listadetorres2[len(listadetorres2)-1]),20000,20000)
            vida_torres3=12
            c.update()
            
    #Seccion de proyectiles 
    global listadeproyec
    global listadeproyec1
    global listadeproyec2
    listadeproyec=[]
    listadeproyec1=[]
    listadeproyec2=[]
    def proyectiles():#Estas 3 funciones hacen que cuando se crean nuevas imagenes de torres que creen sus respectivos proyectiles 

        if len(listadetorres)>=1:
            c.coords(listadetorres[len(listadetorres)-1])
            listadeproyec.append(c.create_image(c.coords(listadetorres[len(listadetorres)-1])[0],c.coords(listadetorres[len(listadetorres)-1])[1],
                                                image=bullet,state=NORMAL,tags='ff'+str(len(listadeproyec))))

    
    def proyectiles2():
        if len(listadetorres1)>=1:
            c.coords(listadetorres1[len(listadetorres1)-1])
            listadeproyec1.append(c.create_image(c.coords(listadetorres1[len(listadetorres1)-1])[0],c.coords(listadetorres1[len(listadetorres1)-1])[1],
                                                 image=proyectil,state=NORMAL,tags='aa'+str(len(listadeproyec1))))
            


    def proyectiles3():
        if len(listadetorres2)>=1:
            c.coords(listadetorres2[len(listadetorres2)-1])
            listadeproyec2.append(c.create_image(c.coords(listadetorres2[len(listadetorres2)-1])[0],c.coords(listadetorres2[len(listadetorres2)-1])[1],
                                                 image=proyectil2,state=NORMAL,tags='Img'+str(len(listadeproyec2))))
    #Vidas de los avatars
    global vida_avatar_lenandor
    global vida_avatar_escudero
    global vida_avatar_canibal
    global vida_avatar_flechero1
    global vida_avatar_flechero2
    
    vida_avatar_lenandor=10
    vida_avatar_escudero=8
    vida_avatar_canibal=12
    vida_avatar_flechero1=4
    vida_avatar_flechero2=4
    ########################################################
    mixer.init()
    impact_sound_effect=mixer.Sound("Impacto.wav")#Sonido de impacto de pygame 
    #########################################################
    #Colisiones de los proyectiles 
    def moverlistadeproyectiles():#Esta funcion recorre la lista de proyectiles compara si la posicion de los avatares es igual o esta en un cierto rango, entonces que
        global vida_avatar_lenandor# marque la colision como correcta y le resta vida a los avatares
        global vida_avatar_escudero
        global vida_avatar_canibal
        global vida_avatar_flechero1
        global vida_avatar_flechero2
        if len(listadeproyec)>=1:
            for j in range(0,len(listadeproyec)):
                c.coords((c.gettags(listadeproyec[j])),c.coords((listadeproyec[j]))[0]+1,c.coords((listadeproyec[j]))[1])#Esto se encarga de mover la lista de proyectiles
                #atraves de la pantalla 
                if c.bbox('f1')[0]<c.bbox(listadeproyec[j])[2]<c.bbox('f1')[2]-97 and c.bbox('f1')[1]<c.bbox(listadeproyec[j])[1]<c.bbox('f1')[3]:
                    vida_avatar_lenandor-=2
                    avatar_dead()
                    impact_sound_effect.play()
                if c.bbox('f3')[0]<c.bbox(listadeproyec[j])[2]<c.bbox('f3')[2]-97 and c.bbox('f3')[1]<c.bbox(listadeproyec[j])[1]<c.bbox('f3')[3]:
                    vida_avatar_escudero-=2
                    avatar_dead()
                    impact_sound_effect.play()
                if c.bbox('f4')[0]<c.bbox(listadeproyec[j])[2]<c.bbox('f4')[2]-97 and c.bbox('f4')[1]<c.bbox(listadeproyec[j])[1]<c.bbox('f4')[3]:
                    vida_avatar_canibal-=2
                    avatar_dead()
                    impact_sound_effect.play()
                if c.bbox('f2')[0]<c.bbox(listadeproyec[j])[2]<c.bbox('f2')[2]-97 and c.bbox('f2')[1]<c.bbox(listadeproyec[j])[1]<c.bbox('f2')[3]:
                    vida_avatar_flechero1-=2
                    avatar_dead()
                    impact_sound_effect.play()
                    
                if c.bbox('f5')[0]<c.bbox(listadeproyec[j])[2]<c.bbox('f5')[2]-97 and c.bbox('f5')[1]<c.bbox(listadeproyec[j])[1]<c.bbox('f5')[3]:
                    vida_avatar_flechero2-=2
                    avatar_dead()
                    impact_sound_effect.play()                    
                if c.coords((listadeproyec[j]))[0]>1000:
                    c.coords((c.gettags(listadeproyec[j])),c.coords((listadetorres[j]))[0],c.coords((listadetorres[j]))[1])
       
        if OPEN==TRUE:
            top3.after(10,lambda:moverlistadeproyectiles())
       
    a=Thread(target=moverlistadeproyectiles)
    a.start()#Iniciamos el thread
    #Esta funcion mueve la lista de los proyectiles del  ROCK ROOK 
    def moverlistadeproyectiles2():#Esta funcion es similar a la funcion de moverlistadeproyectiles nada mas que lo hace con otra lista de proyectiles 
        global vida_avatar_lenandor
        global vida_avatar_escudero
        global vida_avatar_canibal
        global vida_avatar_flechero1
        global vida_avatar_flechero2
        if len(listadeproyec1)>=1:
            for k in range(0,len(listadeproyec1)):
                           c.coords((c.gettags(listadeproyec1[k])),c.coords((listadeproyec1[k]))[0]+1,c.coords((listadeproyec1[k]))[1])
                           if c.bbox('f5')[0]<c.bbox(listadeproyec1[k])[2]<c.bbox('f5')[2]-97 and c.bbox('f5')[1]<c.bbox(listadeproyec1[k])[1]<c.bbox('f5')[3]:
                               vida_avatar_flechero2-=3
                               avatar_dead()
                               impact_sound_effect.play()             

                           if c.bbox('f2')[0]<c.bbox(listadeproyec1[k])[2]<c.bbox('f2')[2]-97 and c.bbox('f2')[1]<c.bbox(listadeproyec1[k])[1]<c.bbox('f2')[3]:
                                vida_avatar_flechero1-=3
                                avatar_dead()
                                impact_sound_effect.play()

                           if c.bbox('f4')[0]<c.bbox(listadeproyec1[k])[2]<c.bbox('f4')[2]-97 and c.bbox('f4')[1]<c.bbox(listadeproyec1[k])[1]<c.bbox('f4')[3]:
                               vida_avatar_canibal-=3
                               avatar_dead()
                               impact_sound_effect.play()
                           
                           if c.bbox('f1')[0]<c.bbox(listadeproyec1[k])[2]<c.bbox('f1')[2]-97 and c.bbox('f1')[1]<c.bbox(listadeproyec1[k])[1]<c.bbox('f1')[3]:
                               vida_avatar_lenandor-=3
                               avatar_dead()
                               impact_sound_effect.play()
                        
                           if c.bbox('f3')[0]<c.bbox(listadeproyec1[k])[2]<c.bbox('f3')[2]-97 and c.bbox('f3')[1]<c.bbox(listadeproyec1[k])[1]<c.bbox('f3')[3]:
                               vida_avatar_escudero-=3
                               avatar_dead()
                               impact_sound_effect.play()
                           elif c.coords((listadeproyec1[k]))[0]>1000:
                               c.coords((c.gettags(listadeproyec1[k])),c.coords((listadetorres1[k]))[0],c.coords((listadetorres1[k]))[1])
                        
        if OPEN==TRUE:
            top3.after(10,lambda:moverlistadeproyectiles2())
                           
                           
    a1=Thread(target=moverlistadeproyectiles2)
    a1.start()
    def avatar_dead():#Si la vida es menor que cero que mueva el avatar correspondiente
        global coin 
        if vida_avatar_lenandor<=0:
            coin=coin+75
            labelcoi.config(text="Coins"+str(coin))
            c.move('f1',8000,8000)
        if vida_avatar_escudero<=0:
            coin=coin+75
            labelcoi.config(text="Coins"+str(coin))
            c.move('f3',8000,8000)
        if vida_avatar_canibal<=0:
            coin=coin+75
            labelcoi.config(text="Coins"+str(coin))
            c.move('f4',8000,8000)
        if vida_avatar_flechero1<=0:
            coin=coin+75
            labelcoi.config(text="Coins"+str(coin))
            c.move('f2',8000,8000)
        if vida_avatar_flechero2<=0:
            coin=coin+75
            labelcoi.config(text="Coins"+str(coin))
            c.move('f5',8000,8000)
        if vida_avatar_lenandor<=0 and vida_avatar_escudero<=0 and vida_avatar_canibal<=0 and vida_avatar_flechero1<=0 and vida_avatar_flechero2<=0:
            win_game()

    def moverlistadeproyectiles3():#Esta funcion es similar a la funcion de moverlistadeproyectiles nada mas que lo hace con otra lista de proyectiles
        global vida_avatar_lenandor
        global vida_avatar_escudero
        global vida_avatar_canibal
        global vida_avatar_flechero1
        global vida_avatar_flechero2
        if len(listadeproyec2)>=1:
            for i in range(0,len(listadeproyec2)):
                           c.coords((c.gettags(listadeproyec2[i])),c.coords((listadeproyec2[i]))[0]+1,c.coords((listadeproyec2[i]))[1])
                           if c.bbox('f5')[0]<c.bbox(listadeproyec2[i])[2]<c.bbox('f5')[2]-97 and c.bbox('f5')[1]<c.bbox(listadeproyec2[i])[1]<c.bbox('f5')[3]:
                               vida_avatar_flechero2-=4
                               avatar_dead()
                               impact_sound_effect.play()
                           if c.bbox('f2')[0]<c.bbox(listadeproyec2[i])[2]<c.bbox('f2')[2]-97 and c.bbox('f2')[1]<c.bbox(listadeproyec2[i])[1]<c.bbox('f2')[3]:
                               vida_avatar_flechero1-=4
                               avatar_dead()
                               impact_sound_effect.play()
                           if c.bbox('f4')[0]<c.bbox(listadeproyec2[i])[2]<c.bbox('f4')[2]-97 and c.bbox('f4')[1]<c.bbox(listadeproyec2[i])[1]<c.bbox('f4')[3]:
                               vida_avatar_canibal-=4
                               avatar_dead()
                               impact_sound_effect.play()
                           if c.bbox('f1')[0]<c.bbox(listadeproyec2[i])[2]<c.bbox('f1')[2]-97 and c.bbox('f1')[1]<c.bbox(listadeproyec2[i])[1]<c.bbox('f1')[3]:
                               vida_avatar_lenandor-=4
                               avatar_dead()
                               impact_sound_effect.play()
                            
                           if c.bbox('f3')[0]<c.bbox(listadeproyec2[i])[2]<c.bbox('f3')[2]-97 and c.bbox('f3')[1]<c.bbox(listadeproyec2[i])[1]<c.bbox('f3')[3]:
                               vida_avatar_escudero-=4
                               avatar_dead()
                               impact_sound_effect.play()    
                       
                           if c.coords((listadeproyec2[i]))[0]>1000:
                               c.coords((c.gettags(listadeproyec2[i])),c.coords((listadetorres2[i]))[0],c.coords((listadetorres2[i]))[1])
        if OPEN==TRUE:
            top3.after(9,lambda:moverlistadeproyectiles3())

    a2=Thread(target=moverlistadeproyectiles3)
    a2.start()
############################################################################################################################################    
    def play_music():#Funcion de correr la musica 
        mixer.init()
        mixer.music.load("musica.wav")
        mixer.music.play(-1)
    def stop_music():
        mixer.music.stop()

    playBtn=Button(top3,text="Play Music",command=play_music)
    playBtn.place(x=100,y=655)
    stopBtn=Button(top3,text="Stop Music",command=stop_music)
    stopBtn.place(x=300,y=655)
    ####################################################################
    #MOVIMIENTO BÁSICO DE LOS ENEMIGOS     
    def mov():
        cord=c.coords('f1')
        cord1=c.coords('f2')
        cord2=c.coords('f3')
        cord3=c.coords('f4')
        cord4=c.coords('f5')
        
        if cord[0]!=150:#Si las coordenadas de la respectivos avatars es diferente a la primera columna pues que se sigan movimiendo  
            c.coords('f1',cord[0]-1.5,cord[1])
        if cord1[0]!=150:
            c.coords('f2',cord1[0]-1.5,cord1[1])
        if cord2[0]!=150:
            c.coords('f3',cord2[0]-1.5,cord2[1])
        if cord3[0]!=150:
            c.coords('f4',cord3[0]-1.5,cord3[1])
        if cord4[0]!=150:
            c.coords('f5',cord4[0]-1.5,cord4[1])
        else:
            game_over()
        if OPEN==True:
            top3.after(100,lambda:mov())               

    Thread(target=mov).start()#Iniciamos el thread
     
    def game_over():#Termina el juego si alguno de los avatares llega a la primera columna 
        top3.destroy()
        game_over=Toplevel()
        game_over.title("game_over")
        game_over.minsize(1000,700)
        game_over.resizable(width=NO,height=NO)
        game_over_canvas=Canvas(game_over,width=1000,height=700,bg='white')
        game_over_canvas.place(x=0,y=0)
        game_over_canvas.image2=cImagen("Wallpaper.png")
        imgcanvas2=game_over_canvas.create_image(0,0,anchor=NW,image=game_over_canvas.image2)
        Labe=Label(game_over,text="GAME OVer",bg="red",font=("Arial bold",10),fg='white')
        Labe.place(x=300,y=300)
    def win_game():#Si ganamos el juego pues que se pase al segundo nivel 
        top3.destroy()
        win_game1=Toplevel()
        win_game1.title("WIN LEVEL 1")
        win_game1.minsize(1000,700)
        win_game1.resizable(width=NO,height=NO)
        win_gamecanvas=Canvas(win_game1,width=1000,height=700,bg='white')
        win_gamecanvas.place(x=0,y=0)
        win_gamecanvas.image2=cImagen("Wallpaper.png")
        imgcanvas2=win_gamecanvas.create_image(0,0,anchor=NW,image=win_gamecanvas.image2)
        Labe=Label(win_game1,text="Nivel 1 completado",bg="red",font=("Arial bold",10),fg='white')
        Labe.place(x=300,y=300)
        boton_next_level=Button(win_gamecanvas,text='NEXT LEVEL 2',bg='red',fg='white',height=2,width=15,command=ventana_de_juego_2)
        boton_next_level.place(x=500,y=600)
    #---------------------------------------------------------------------------------------------------------------------------------
    #Crear balas de enemigos tengo que cambiar cosas animacion
    #-----------------------------------------------------------------Proyectiles-----------------------------------------------------
    #garrote=cImagen("garrote.png")
    #garrote1=c.create_image(0,0,image=garrote,tags='garrote',state=HIDDEN)    
    def crear():#Funcion de crear los proyectiles para luego moverlos se dan las coordenadas de los avatares respcectivos 
        global bala4
        global flecha1
        global espada1
        global garrote1
        global flecha2
       
        cords_alien=c.coords(avatar1)
        cords_bala=c.coords('B')
        #-------
        cord_av=c.coords(avatar22)
        cords_flecha=c.coords('flecha')
        #--------

        cord_av2=c.coords(avatar33)
        cords_espada=c.coords('espada')
        #--------
        cord_av3=c.coords(avatar44)
        cords_garrote=c.coords('garrote')

        cord_av4=c.coords(avatar55)
        
        bala4=c.create_image(cords_alien[0],cords_alien[1]+15,image=bala3,tags='B',state=NORMAL)
        #1  
        flecha1=c.create_image(cord_av[0],cord_av[1]+15,image=flecha,tags='flecha',state=NORMAL)
        #2
        flecha2=c.create_image(cord_av4[0],cord_av4[1]+15,image=flecha,tags='flecha2',state=NORMAL)
        
        espada1=c.create_image(cord_av2[0],cord_av2[1]+15,image=espada,tags='espada',state=NORMAL)
        
        garrote1=c.create_image(cord_av3[0],cord_av3[1]+15,image=garrote,tags='garrote',state=NORMAL)    
        bala_enemigo()

    def bala_enemigo():#Se mueven los proyectiles comparando las coordenadas de estas 
        global bala4
        global flecha1
        global espada1
        global garrote1
        global flecha2
        cords_alien=c.coords(avatar1)
        cords_bala=c.coords(bala4)
        #-------
        cord_av=c.coords(avatar22)
        cords_flecha=c.coords(flecha1)
        #----
        cord_av2=c.coords(avatar33)
        cords_espada=c.coords(espada1)
        #----
        cord_av3=c.coords(avatar44)
        cords_garrote=c.coords(garrote1)
        #----
        cord_av4=c.coords(avatar55)
        cords_flecha2=c.coords(flecha2)
        
        if cords_bala[0]>-50:
            c.coords(bala4,cords_bala[0]-2,cords_bala[1])
            c.coords(flecha1,cords_flecha[0]-2,cords_flecha[1])
            c.coords(espada1,cords_espada[0]-2,cords_espada[1])
            c.coords(garrote1,cords_garrote[0]-2,cords_garrote[1])
            c.coords(flecha2,cords_flecha2[0]-2,cords_flecha2[1])
            
        if cords_bala[0]<=100: 
            c.coords(espada1,cord_av2[0],cord_av2[1]+15)
            
            c.coords(bala4,cords_alien[0],cords_alien[1]+15)
            
            c.coords(flecha1,cord_av[0],cord_av[1]+15)
            
            c.coords(garrote1,cord_av3[0],cord_av3[1]+15)

            c.coords(flecha2,cord_av4[0],cord_av4[1]+15)        
            
        if OPEN==TRUE:#Iniciamos el thread 
            top3.after(10,lambda:bala_enemigo())
    def crear_varias(): #Esta funcion crear varias pero queda absoleta por el after      
        crear()
        
        top3.after(70000000,lambda:crear_varias())
    crear_varias()
    #----------------------------------------------------------------------------Proyectiles--------------------------------------------------------------
    #-------------------------------------------------Clases---------------------------------------------------------------------------------------------
    #Función de cronómetro  
    def cronometro():
        global TIME
        c2.delete(ALL)
        TIME=TIME+1
        time=c2.create_text(50,10, text=TIME,fill="Purple")
        if TIME==0:
            game_over()
        else:
            c2.after(1000,cronometro)
    c2=Canvas(top3,width=75,height=20,bg="white")
    c2.place(x=920,y=0)
    cronometro()

    
    #c.focus_set()
    ventana.withdraw()
    top3.mainloop()
def close_juegos():
    ventana.deiconify()
    top3.destroy()


#############################################################################################################################
##############################################################################################################################
#############################################################################################################################
#Ventanan de juego 2 
def ventana_de_juego_2():#Esta funcion presenta la misma funciones que el nivel 1 de juego, pero se crean nuevos enemigos y poseen mas vida 
    global top3
    global a1
    global c
    top3=Toplevel()
    top3.title('Ventana de Juego 2')
    top3.minsize(1000,700)
    top3.resizable(width=NO, height=NO)
    c=Canvas(top3,width=1000,height=700,bg='white')
    c.place(x=0,y=0)
    b=Button(top3,text='volver a menu',command=close_juegos)
    b.place(x=500,y=650)
    Label23=Label(top3,text="User name:"+username1,bg='red',font=('Calibri',10),fg='white')
    Label23.place(x=875,y=65)
    #Variables 
    OPEN=True
    #Posiciones inciales tablero 
    y=135
    y2=232
    y3=315
    y4=410
    y5=486
    y6=565
    #Lista de posiciones en el tablero 
    list_posiciones=[y,y2,y3,y4,y5,y6]
    random.shuffle(list_posiciones)
    pos1=list_posiciones[0]
    pos2=list_posiciones[1]
    pos3=list_posiciones[2]
    pos4=list_posiciones[3]
    pos5=list_posiciones[4]
    pos6=list_posiciones[5] 
    ##lISTA DE IMAGENES RANDOM
    lis_avatars=["avatar escudero.png","avatar caníbal.png","avatar leñador.png","avatar flechero.png"]
    random.shuffle(lis_avatars)
    ava=lis_avatars[0]
    ava2=lis_avatars[1]
    ava3=lis_avatars[2]
    ava4=lis_avatars[3]
    ###########################
    global img
    global water1
    global my_img1
    #Imagen del tablero
    Tablero=cImagen("t.png")
    Tablerol=c.create_image(0,0,anchor=NW,image=Tablero)
    #Imagen de torres
    img=PhotoImage(file="Imgs\\sand1.png")
    my_img1=c.create_image(100,5,anchor=NW,image=img)
    #------
    rock=cImagen("rock.png")
    rock1=c.create_image(300,5,anchor=NW,image=rock)
    #---
    global fire 
    fire=cImagen("fire.png")
    fire1=c.create_image(500,5,anchor=NW,image=fire)
    #-----
    water=cImagen("water.png")
    water1=c.create_image(700,5,anchor=NW,image=water,tags='rook1')
    global avatar55
    #Imagenes de avatars
    avatar=cImagen('avatar leñador.png')
    avatar1=c.create_image(900,pos1,anchor=CENTER,image=avatar,tags='f1')
    #--------
    avatar2=cImagen('avatar flechero.png')
    avatar22=c.create_image(900,pos2,anchor=CENTER,image=avatar2,tags='f2')
    #--------
    avatar3=cImagen('avatar escudero.png')
    avatar33=c.create_image(900,pos3,anchor=CENTER,image=avatar3,tags='f3')
    #----
    avatar4=cImagen('avatar caníbal.png')
    avatar44=c.create_image(900,pos4,anchor=CENTER,image=avatar4,tags='f4')
    #----
    avatar5=cImagen('avatar flechero.png')
    avatar55=c.create_image(900,pos6,anchor=CENTER,image=avatar5,tags='f5')

    avatar6=cImagen('avatar escudero.png')
    avatar66=c.create_image(900,pos5,anchor=CENTER,image=avatar6,tags='avatar_escudero2')
    
    #Cagar imagenes de monedas
    global coin50
    global coin25
    global coin100
    global monedas
    coin50=cImagen('50 coin.png')
    coin25=cImagen('25 coin.png')
    coin100=cImagen('100 coin.png')
    
    monedas=[coin50,coin25,coin100]
    def crearcoin():
        global coin50
        global coin25
        global coin100
        global monedas
        global imaggg
        random.shuffle(monedas)
        imaggg=c.create_image(random.randint(100,600),random.randint(300,600),anchor=CENTER,image=monedas[0],tags=str(monedas[0]))
        top3.after(10000,lambda:crearcoin())
    Thread(target=crearcoin).start()

    ####################################################################################
    global imaggg
    #Creear imagenes de proyectiles
    ########################################Puedo usar la misma variable###################################################################
    bala3=cImagen("axe.png")
    bala4=c.create_image(0,0,image=bala3,tags='B',state=HIDDEN)
    
    flecha=cImagen("arrow.png")
    flecha1=c.create_image(0,0,image=flecha,tags='flecha',state=HIDDEN)

    espada=cImagen("sword.png")
    espada1=c.create_image(0,0,image=espada,tags='espada',state=HIDDEN)
    
    garrote=cImagen("garrote.png")
    garrote1=c.create_image(0,0,image=garrote,tags='garrote',state=HIDDEN)
    
    ###############################################################################################
    bullet=cImagen("fire ball.png")
    #bullet1=c.create_image(0,0,image=bullet,tags='bullet',state=HIDDEN)

    proyectil=cImagen("spikeball.png")

    proyectil2=cImagen("Water ball.png")

    def printt(event):
        print(event.x,event.y)

    c.bind("<ButtonPress-2>",printt)
    #########################################################################################################################################
    #----------------------------------------------------------------IMGS------------------------------------------------------------------------
    global var
    #global coin
    global laelcoi
    #coin=1000
    var=0
    labelcoi=Label(top3,text="Coins" +str(coin))
    labelcoi.place(x=920,y=30)
    def mouse_acc(event):
        global var
        global coin
        global imaggg
        rango=c.bbox(my_img1)#Sand rook
        rang=c.bbox(rock1)
        rang1=c.bbox(fire1)
        rang2=c.bbox(water1)
        rang3=c.bbox(imaggg)
        if event.x >=rango[0] and event.x < (rango[2]):
            if event.y >= rango[1] and event.y <(rango[3]):#Hago lo mismo nada mas que con otra imagen y con las variables 
                var=1
                coin=coin-50
                labelcoi.config(text="Coins"+str(coin))
        if event.x >=rang[0] and event.x < (rang[2]):#2
            if event.y >= rang[1] and event.y <(rang[3]):
                var=2
                coin=coin-100
                labelcoi.config(text="Coins"+str(coin))
        if event.x >=rang1[0] and event.x < (rang1[2]):#3
            if event.y >= rang1[1] and event.y <(rang1[3]):
                var=3
                coin=coin-150
                labelcoi.config(text="Coins"+str(coin))
        if event.x >=rang2[0] and event.x < (rang2[2]):#4
            if event.y >= rang2[1] and event.y <(rang2[3]):
                var=4
                coin=coin-200
                labelcoi.config(text="Coins"+str(coin))
        if event.x >=rang3[0] and event.x < (rang3[2]):#4
            if event.y >= rang3[1] and event.y <(rang3[3]):
                if str(monedas[0])==str(coin50):
                    coin=coin+50
                    labelcoi.config(text="Coins"+str(coin))
                    var=5
                if str(monedas[0])==str(coin25):
                    coin=coin+25
                    labelcoi.config(text="Coins"+str(coin))
                    var=5
                if str(monedas[0])==str(coin100):
                    coin=coin+100
                    labelcoi.config(text="Coins"+str(coin))
                    var=5
    
    global listadetorres
    global listadetorres1
    global listadetorres2
    listadetorres=[]
    listadetorres1=[]
    listadetorres2=[]
    def colocar_torre(event):#Para hacer otras imagenes cambio la variables 
        global var
        global coin
        global imgz
        if var==1:
            c.create_image(event.x,event.y,anchor=CENTER,image=img,state=NORMAL,tags='aaa'+str(len(listadetorres)))
            listadetorres.append(c.create_image(event.x,event.y,anchor=CENTER,image=img,state=NORMAL,tags='aaa'+str(len(listadetorres))))
            proyectiles()
            c.update()
            var=0
        if var==2:
            c.create_image(event.x,event.y,anchor=CENTER,image=rock,state=NORMAL,tags='aaa'+str(len(listadetorres)))
            listadetorres.append(c.create_image(event.x,event.y,anchor=CENTER,image=rock,state=NORMAL,tags='aaa'+str(len(listadetorres))))
            proyectiles()
            c.update()
            var=0
        if var==3:
            c.create_image(event.x,event.y,image=fire,state=NORMAL,tags='ccc'+str(len(listadetorres1)))
            listadetorres1.append(c.create_image(event.x,event.y,image=fire,state=NORMAL,tags='ccc'+str(len(listadetorres1))))
            #print(c.bbox(listadetorres1[0]))
            proyectiles2()
            c.update()
            var=0
        if var==4:
            c.create_image(event.x,event.y,anchor=CENTER,image=water,tags='torre'+str(len(listadetorres2)))
            listadetorres2.append(c.create_image(event.x,event.y,anchor=CENTER,image=water,tags='torre'+str(len(listadetorres2))))
            proyectiles3()
            c.update()
            var=0
        if var==5:
            c.delete(imaggg)
            c.update()
            var=0    
    c.bind("<ButtonPress-1>",mouse_acc)
    c.bind("<ButtonRelease-1>",colocar_torre)

    #Colisiones entre las torres
    global vida_torre
    global vida_torre2
    global vida_torres3
    vida_torre=20
    vida_torre2=16
    vida_torres3=25    
    def eliminar():
        global vida_torre
        if len(listadetorres1)>=1:
            for b in range(0,len(listadetorres1)):
                bx=c.bbox("espada")
                bx1=c.bbox("garrote")
                bx2=c.bbox("B")
                bx3=c.bbox("flecha")
                bx4=c.bbox("flecha2")
                bx5=c.bbox("espada2")
                sbx=c.bbox(listadetorres1[b])
                if (bx1[2]in range ((sbx[0]),(sbx[2]-99))) and  ((bx1[1] in range(sbx[1],sbx[3]))):
                    vida_torre-=4
                    vidas_torres()
                if (bx[2]in range ((sbx[0]),(sbx[2]-99))) and ((bx[1] in range(sbx[1],sbx[3]))):
                    vida_torre-=2
                    vidas_torres()
                if (bx2[2]in range ((sbx[0]),(sbx[2]-99))) and ((bx2[1] in range(c.bbox(listadetorres1[b])[1],c.bbox(listadetorres1[b])[3]))):
                    vida_torre-=3
                    vidas_torres()
                if (bx3[2]in range ((sbx[0]),(sbx[2]-98))) and ((bx3[1] in range(c.bbox(listadetorres1[b])[1],c.bbox(listadetorres1[b])[3]))):
                    vida_torre-=1
                    vidas_torres()
                if (bx4[2]in range ((sbx[0]),(sbx[2]-98))) and ((bx4[1] in range(c.bbox(listadetorres1[b])[1],c.bbox(listadetorres1[b])[3]))):
                    vida_torre-=1
                    vidas_torres()

                if (bx5[2]in range ((sbx[0]),(sbx[2]-98))) and ((bx5[1] in range(c.bbox(listadetorres1[b])[1],c.bbox(listadetorres1[b])[3]))):
                    vida_torre-=4
                    vidas_torres()
                            
        if OPEN==TRUE:
            top3.after(1,lambda:eliminar())
    t1=Thread(target=eliminar)
    t1.start()
    def eliminar_torres():
        global vida_torre2
        if len(listadetorres)>=1:
            for b in range(0,len(listadetorres)):
                bx=c.bbox("espada")
                bx1=c.bbox("garrote")
                bx2=c.bbox("B")
                bx3=c.bbox("flecha")
                bx4=c.bbox("flecha2")
                bx5=c.bbox("espada2")
                sbx=c.bbox(listadetorres[b])
                if (bx1[2]in range ((sbx[0]),(sbx[2]-99))) and  ((bx1[1] in range(sbx[1],sbx[3]))):
                    vida_torre2-=4
                    vidas_torres()
                if (bx[2]in range ((sbx[0]),(sbx[2]-99))) and ((bx[1] in range(sbx[1],sbx[3]))):
                    vida_torre2-=2
                    vidas_torres()
                if (bx2[2]in range ((sbx[0]),(sbx[2]-99))) and ((bx2[1] in range(c.bbox(listadetorres[b])[1],c.bbox(listadetorres[b])[3]))):
                    vida_torre2-=3
                    vidas_torres()
                if (bx3[2]in range ((sbx[0]),(sbx[2]-98))) and ((bx3[1] in range(c.bbox(listadetorres[b])[1],c.bbox(listadetorres[b])[3]))):
                    vida_torre2-=1
                    vidas_torres()
                if (bx4[2]in range ((sbx[0]),(sbx[2]-98))) and ((bx4[1] in range(c.bbox(listadetorres[b])[1],c.bbox(listadetorres[b])[3]))):
                    vida_torre2-=1
                    vidas_torres()
                if (bx5[2]in range ((sbx[0]),(sbx[2]-98))) and ((bx5[1] in range(c.bbox(listadetorres[b])[1],c.bbox(listadetorres[b])[3]))):
                    vida_torre2-=4
                    vidas_torres()

                    
        if OPEN==TRUE:
            top3.after(1,lambda:eliminar_torres())
        
    t2=Thread(target=eliminar_torres)
    t2.start()    
    def eliminar_torres2():
        global vida_torres3
        if len(listadetorres2)>=1:
            for b in range(0,len(listadetorres2)):
                bx=c.bbox("espada")
                bx1=c.bbox("garrote")
                bx2=c.bbox("B")
                bx3=c.bbox("flecha")
                bx4=c.bbox("flecha2")
                bx5=c.bbox("espada2")
                sbx=c.bbox(listadetorres2[b])
                if (bx1[2]in range ((sbx[0]),(sbx[2]-99))) and  ((bx1[1] in range(sbx[1],sbx[3]))):
                    vida_torres3-=4
                    vidas_torres()
                if (bx[2]in range ((sbx[0]),(sbx[2]-99))) and ((bx[1] in range(sbx[1],sbx[3]))):
                    vida_torres3-=2
                    vidas_torres()
                if (bx2[2]in range ((sbx[0]),(sbx[2]-99))) and ((bx2[1] in range(c.bbox(listadetorres2[b])[1],c.bbox(listadetorres2[b])[3]))):
                    vida_torres3-=3
                    vidas_torres()
                if (bx3[2]in range ((sbx[0]),(sbx[2]-98))) and ((bx3[1] in range(c.bbox(listadetorres2[b])[1],c.bbox(listadetorres2[b])[3]))):
                    vida_torres3-=1
                    vidas_torres()
                if (bx4[2]in range ((sbx[0]),(sbx[2]-98))) and ((bx4[1] in range(c.bbox(listadetorres2[b])[1],c.bbox(listadetorres2[b])[3]))):
                    vida_torres3-=1
                    vidas_torres()
                if (bx5[2]in range ((sbx[0]),(sbx[2]-98))) and ((bx5[1] in range(c.bbox(listadetorres2[b])[1],c.bbox(listadetorres2[b])[3]))):
                    vida_torres3-=4
                    vidas_torres()
        if OPEN==TRUE:
            top3.after(1,lambda:eliminar_torres2())
    t3=Thread(target=eliminar_torres2)
    t3.start()
    def vidas_torres():
        global vida_torre
        global vida_torre2
        global vida_torres3
        if vida_torre<=0:
            c.move(c.gettags(listadetorres1[len(listadetorres1)-1]),40000,40000)
            vida_torre=10
            c.update()
        if vida_torre2<=0:
            c.move(c.gettags(listadetorres[len(listadetorres)-1]),20000,20000)
            vida_torre2=7
            c.update()
        if vida_torres3<=0:
            c.move(c.gettags(listadetorres2[len(listadetorres2)-1]),20000,20000)
            vida_torres3=12
            c.update()
    #Seccion de proyectiles 
    global listadeproyec
    global listadeproyec1
    global listadeproyec2
    listadeproyec=[]
    listadeproyec1=[]
    listadeproyec2=[]
    def proyectiles():
     
        if len(listadetorres)>=1:
            c.coords(listadetorres[len(listadetorres)-1])
            listadeproyec.append(c.create_image(c.coords(listadetorres[len(listadetorres)-1])[0],c.coords(listadetorres[len(listadetorres)-1])[1],
                                                image=bullet,state=NORMAL,tags='ff'+str(len(listadeproyec))))    
    def proyectiles2():
        if len(listadetorres1)>=1:
            c.coords(listadetorres1[len(listadetorres1)-1])
            listadeproyec1.append(c.create_image(c.coords(listadetorres1[len(listadetorres1)-1])[0],c.coords(listadetorres1[len(listadetorres1)-1])[1],
                                                 image=proyectil,state=NORMAL,tags='aa'+str(len(listadeproyec1))))
    def proyectiles3():
        if len(listadetorres2)>=1:
            c.coords(listadetorres2[len(listadetorres2)-1])
            listadeproyec2.append(c.create_image(c.coords(listadetorres2[len(listadetorres2)-1])[0],c.coords(listadetorres2[len(listadetorres2)-1])[1],
                                                 image=proyectil2,state=NORMAL,tags='Img'+str(len(listadeproyec2))))
    #Vidas de los avatars
    global vida_avatar_lenandor
    global vida_avatar_escudero
    global vida_avatar_canibal
    global vida_avatar_flechero1
    global vida_avatar_flechero2
    global vida_avatar_escudero2
    
    vida_avatar_lenandor=10
    vida_avatar_escudero=8
    vida_avatar_canibal=12
    vida_avatar_flechero1=4
    vida_avatar_flechero2=4
    vida_avatar_escudero2=8
    ########################################################
    mixer.init()
    impact_sound_effect=mixer.Sound("Impacto.wav")
    #########################################################
    def moverlistadeproyectiles():
        global vida_avatar_lenandor
        global vida_avatar_escudero
        global vida_avatar_canibal
        global vida_avatar_flechero1
        global vida_avatar_flechero2
        global vida_avatar_escudero2
        if len(listadeproyec)>=1:
            for j in range(0,len(listadeproyec)):
                c.coords((c.gettags(listadeproyec[j])),c.coords((listadeproyec[j]))[0]+1,c.coords((listadeproyec[j]))[1])
                if c.bbox('avatar_escudero2')[0]<c.bbox(listadeproyec[j])[2]<c.bbox('avatar_escudero2')[2]-97 and c.bbox('avatar_escudero2')[1]<c.bbox(listadeproyec[j])[1]<c.bbox('avatar_escudero2')[3]:
                    vida_avatar_escudero2-=2
                    
                    avatar_dead()
                    impact_sound_effect.play()
                if c.bbox('f1')[0]<c.bbox(listadeproyec[j])[2]<c.bbox('f1')[2]-97 and c.bbox('f1')[1]<c.bbox(listadeproyec[j])[1]<c.bbox('f1')[3]:
                    vida_avatar_lenandor-=2
                    avatar_dead()
                    impact_sound_effect.play()
                if c.bbox('f3')[0]<c.bbox(listadeproyec[j])[2]<c.bbox('f3')[2]-97 and c.bbox('f3')[1]<c.bbox(listadeproyec[j])[1]<c.bbox('f3')[3]:
                    vida_avatar_escudero-=2
                    avatar_dead()
                    impact_sound_effect.play()
                if c.bbox('f4')[0]<c.bbox(listadeproyec[j])[2]<c.bbox('f4')[2]-97 and c.bbox('f4')[1]<c.bbox(listadeproyec[j])[1]<c.bbox('f4')[3]:
                    vida_avatar_canibal-=2
                    avatar_dead()
                    impact_sound_effect.play()
                if c.bbox('f2')[0]<c.bbox(listadeproyec[j])[2]<c.bbox('f2')[2]-97 and c.bbox('f2')[1]<c.bbox(listadeproyec[j])[1]<c.bbox('f2')[3]:
                    vida_avatar_flechero1-=2
                    avatar_dead()
                    impact_sound_effect.play()
                    
                if c.bbox('f5')[0]<c.bbox(listadeproyec[j])[2]<c.bbox('f5')[2]-97 and c.bbox('f5')[1]<c.bbox(listadeproyec[j])[1]<c.bbox('f5')[3]:
                    vida_avatar_flechero2-=2
                    avatar_dead()
                    impact_sound_effect.play()                    
                if c.coords((listadeproyec[j]))[0]>1000:
                    c.coords((c.gettags(listadeproyec[j])),c.coords((listadetorres[j]))[0],c.coords((listadetorres[j]))[1])
       
        if OPEN==TRUE:
            top3.after(10,lambda:moverlistadeproyectiles())
       
    a=Thread(target=moverlistadeproyectiles)
    a.start()
    
    #Esta funcion mueve la lista de los proyectiles del  ROCK ROOK 
    def moverlistadeproyectiles2():
        global vida_avatar_lenandor
        global vida_avatar_escudero
        global vida_avatar_canibal
        global vida_avatar_flechero1
        global vida_avatar_flechero2
        global vida_avatar_escudero2
        if len(listadeproyec1)>=1:
            for k in range(0,len(listadeproyec1)):
                           c.coords((c.gettags(listadeproyec1[k])),c.coords((listadeproyec1[k]))[0]+1,c.coords((listadeproyec1[k]))[1])
                           if c.bbox('avatar_escudero2')[0]<c.bbox(listadeproyec1[k])[2]<c.bbox('avatar_escudero2')[2]-97 and c.bbox('avatar_escudero2')[1]<c.bbox(listadeproyec1[k])[1]<c.bbox('avatar_escudero2')[3]:
                               vida_avatar_escudero2-=3
                               avatar_dead()
                               impact_sound_effect.play()
                           if c.bbox('f5')[0]<c.bbox(listadeproyec1[k])[2]<c.bbox('f5')[2]-97 and c.bbox('f5')[1]<c.bbox(listadeproyec1[k])[1]<c.bbox('f5')[3]:
                               vida_avatar_flechero2-=3
                               avatar_dead()
                               impact_sound_effect.play()             

                           if c.bbox('f2')[0]<c.bbox(listadeproyec1[k])[2]<c.bbox('f2')[2]-97 and c.bbox('f2')[1]<c.bbox(listadeproyec1[k])[1]<c.bbox('f2')[3]:
                                vida_avatar_flechero1-=3
                                avatar_dead()
                                impact_sound_effect.play()

                           if c.bbox('f4')[0]<c.bbox(listadeproyec1[k])[2]<c.bbox('f4')[2]-97 and c.bbox('f4')[1]<c.bbox(listadeproyec1[k])[1]<c.bbox('f4')[3]:
                               vida_avatar_canibal-=3
                               avatar_dead()
                               impact_sound_effect.play()
                           
                           if c.bbox('f1')[0]<c.bbox(listadeproyec1[k])[2]<c.bbox('f1')[2]-97 and c.bbox('f1')[1]<c.bbox(listadeproyec1[k])[1]<c.bbox('f1')[3]:
                               vida_avatar_lenandor-=3
                               avatar_dead()
                               impact_sound_effect.play()
                        
                           if c.bbox('f3')[0]<c.bbox(listadeproyec1[k])[2]<c.bbox('f3')[2]-97 and c.bbox('f3')[1]<c.bbox(listadeproyec1[k])[1]<c.bbox('f3')[3]:
                               vida_avatar_escudero-=3
                               avatar_dead()
                               impact_sound_effect.play()
                           elif c.coords((listadeproyec1[k]))[0]>1000:
                               c.coords((c.gettags(listadeproyec1[k])),c.coords((listadetorres1[k]))[0],c.coords((listadetorres1[k]))[1])
                        
        if OPEN==TRUE:
            top3.after(10,lambda:moverlistadeproyectiles2())                           
    a1=Thread(target=moverlistadeproyectiles2)
    a1.start()
    def avatar_dead():
        global coin 
        if vida_avatar_lenandor<=0:
            coin=coin+75
            labelcoi.config(text="Coins"+str(coin))
            c.move('f1',8000,8000)
        if vida_avatar_escudero<=0:
            coin=coin+75
            labelcoi.config(text="Coins"+str(coin))
            c.move('f3',8000,8000)
        if vida_avatar_canibal<=0:
            coin=coin+75
            labelcoi.config(text="Coins"+str(coin))
            c.move('f4',8000,8000)
        if vida_avatar_flechero1<=0:
            coin=coin+75
            labelcoi.config(text="Coins"+str(coin))
            c.move('f2',8000,8000)
        if vida_avatar_flechero2<=0:
            coin=coin+75
            labelcoi.config(text="Coins"+str(coin))
            c.move('f5',8000,8000)
        if vida_avatar_escudero2<=0:
            coin=coin+75
            labelcoi.config(text="Coins"+str(coin))
            c.move('avatar_escudero2',8000,8000)
        if vida_avatar_lenandor<=0 and vida_avatar_escudero<=0 and vida_avatar_canibal<=0 and vida_avatar_flechero1<=0 and vida_avatar_flechero2<=0 and vida_avatar_escudero2<=0:
            win_game()
    def moverlistadeproyectiles3():
        global vida_avatar_lenandor
        global vida_avatar_escudero
        global vida_avatar_canibal
        global vida_avatar_flechero1
        global vida_avatar_flechero2
        global vida_avatar_escudero2
        if len(listadeproyec2)>=1:
            for i in range(0,len(listadeproyec2)):
                           c.coords((c.gettags(listadeproyec2[i])),c.coords((listadeproyec2[i]))[0]+1,c.coords((listadeproyec2[i]))[1])
                           if c.bbox('avatar_escudero2')[0]<c.bbox(listadeproyec2[i])[2]<c.bbox('avatar_escudero2')[2]-97 and c.bbox('avatar_escudero2')[1]<c.bbox(listadeproyec2[i])[1]<c.bbox('avatar_escudero2')[3]:
                               vida_avatar_escudero2-=3
                               avatar_dead()
                               impact_sound_effect.play()
                           
                           if c.bbox('f5')[0]<c.bbox(listadeproyec2[i])[2]<c.bbox('f5')[2]-97 and c.bbox('f5')[1]<c.bbox(listadeproyec2[i])[1]<c.bbox('f5')[3]:
                               vida_avatar_flechero2-=4
                               avatar_dead()
                               impact_sound_effect.play()
                           if c.bbox('f2')[0]<c.bbox(listadeproyec2[i])[2]<c.bbox('f2')[2]-97 and c.bbox('f2')[1]<c.bbox(listadeproyec2[i])[1]<c.bbox('f2')[3]:
                               vida_avatar_flechero1-=4
                               avatar_dead()
                               impact_sound_effect.play()
                           if c.bbox('f4')[0]<c.bbox(listadeproyec2[i])[2]<c.bbox('f4')[2]-97 and c.bbox('f4')[1]<c.bbox(listadeproyec2[i])[1]<c.bbox('f4')[3]:
                               vida_avatar_canibal-=4
                               avatar_dead()
                               impact_sound_effect.play()
                           if c.bbox('f1')[0]<c.bbox(listadeproyec2[i])[2]<c.bbox('f1')[2]-97 and c.bbox('f1')[1]<c.bbox(listadeproyec2[i])[1]<c.bbox('f1')[3]:
                               vida_avatar_lenandor-=4
                               avatar_dead()
                               impact_sound_effect.play()
                            
                           if c.bbox('f3')[0]<c.bbox(listadeproyec2[i])[2]<c.bbox('f3')[2]-97 and c.bbox('f3')[1]<c.bbox(listadeproyec2[i])[1]<c.bbox('f3')[3]:
                               vida_avatar_escudero-=4
                               avatar_dead()
                               impact_sound_effect.play()
                              
                           if c.coords((listadeproyec2[i]))[0]>1000:
                               c.coords((c.gettags(listadeproyec2[i])),c.coords((listadetorres2[i]))[0],c.coords((listadetorres2[i]))[1])
        if OPEN==TRUE:
            top3.after(9,lambda:moverlistadeproyectiles3())

    a2=Thread(target=moverlistadeproyectiles3)
    a2.start()
############################################################################################################################################           
    def play_music():
        mixer.init()
        mixer.music.load("musica.wav")
        mixer.music.play(-1)
    def stop_music():
        mixer.music.stop()
    playBtn=Button(top3,text="Play Music",command=play_music)
    playBtn.place(x=100,y=655)
    stopBtn=Button(top3,text="Stop Music",command=stop_music)
    stopBtn.place(x=300,y=655)
    ####################################################################
    #MOVIMIENTO BÁSICO DE LOS ENEMIGOS     
    def mov():
        cord=c.coords('f1')
        cord1=c.coords('f2')
        cord2=c.coords('f3')
        cord3=c.coords('f4')
        cord4=c.coords('f5')
        cord5=c.coords('avatar_escudero2')
        if cord[0]!=150:
            c.coords('f1',cord[0]-1.5,cord[1])
        if cord1[0]!=150:
            c.coords('f2',cord1[0]-1.5,cord1[1])
        if cord2[0]!=150:
            c.coords('f3',cord2[0]-1.5,cord2[1])
        if cord3[0]!=150:
            c.coords('f4',cord3[0]-1.5,cord3[1])
        if cord4[0]!=150:
            c.coords('f5',cord4[0]-1.5,cord4[1])
        if cord5[0]!=150:
            c.coords('avatar_escudero2',cord5[0]-1.5,cord5[1])
        else:
            game_over()
        if OPEN==True:
            top3.after(100,lambda:mov())
    Thread(target=mov).start()
    def game_over():
        top3.destroy()
        game_over=Toplevel()
        game_over.title("game_over")
        game_over.minsize(1000,700)
        game_over.resizable(width=NO,height=NO)
        game_over_canvas=Canvas(game_over,width=1000,height=700,bg='white')
        game_over_canvas.place(x=0,y=0)
        game_over_canvas.image2=cImagen("Wallpaper.png")
        imgcanvas2=game_over_canvas.create_image(0,0,anchor=NW,image=game_over_canvas.image2)
        Labe=Label(game_over,text="GAME OVer",bg="red",font=("Arial bold",10),fg='white')
        Labe.place(x=300,y=300)
        

    def win_game():
        top3.destroy()
        win_game1=Toplevel()
        win_game1.title("WIN LEVEL 2")
        win_game1.minsize(1000,700)
        win_game1.resizable(width=NO,height=NO)
        win_gamecanvas=Canvas(win_game1,width=1000,height=700,bg='white')
        win_gamecanvas.place(x=0,y=0)
        win_gamecanvas.image2=cImagen("Wallpaper.png")
        imgcanvas2=win_gamecanvas.create_image(0,0,anchor=NW,image=win_gamecanvas.image2)
        Labe=Label(win_game1,text="Nivel 2 completado",bg="red",font=("Arial bold",10),fg='white')
        Labe.place(x=300,y=300)
        boton_next_level=Button(win_gamecanvas,text='LEVEL 3',bg='red',fg='white',height=2,width=15,command=ventana_de_juego3)
        boton_next_level.place(x=500,y=600)
        
        
    #---------------------------------------------------------------------------------------------------------------------------------
    #Crear balas de enemigos tengo que cambiar cosas animacion
    #-----------------------------------------------------------------Proyectiles-----------------------------------------------------    
    def crear():
        global bala4
        global flecha1
        global espada1
        global garrote1
        global flecha2
        global espada2
        cords_alien=c.coords(avatar1)
        cords_bala=c.coords('B')
        #-------
        cord_av=c.coords(avatar22)
        cords_flecha=c.coords('flecha')
        #--------

        cord_av2=c.coords(avatar33)
        cords_espada=c.coords('espada')
        #--------
        cord_av3=c.coords(avatar44)
        cords_garrote=c.coords('garrote')

        cord_av4=c.coords(avatar55)


        cord_av5=c.coords(avatar66)
        
        bala4=c.create_image(cords_alien[0],cords_alien[1]+15,image=bala3,tags='B',state=NORMAL)
        #1  
        flecha1=c.create_image(cord_av[0],cord_av[1]+15,image=flecha,tags='flecha',state=NORMAL)
        #2
        flecha2=c.create_image(cord_av4[0],cord_av4[1]+15,image=flecha,tags='flecha2',state=NORMAL)
        
        #1
        espada1=c.create_image(cord_av2[0],cord_av2[1]+15,image=espada,tags='espada',state=NORMAL)

        #2
        espada2=c.create_image(cord_av5[0],cord_av5[1]+15,image=espada,tags='espada2',state=NORMAL)
        
        garrote1=c.create_image(cord_av3[0],cord_av3[1]+15,image=garrote,tags='garrote',state=NORMAL)    

        
        bala_enemigo()

    def bala_enemigo():
        global bala4
        global flecha1
        global espada1
        global garrote1
        global flecha2
        global espada2
        cords_alien=c.coords(avatar1)
        cords_bala=c.coords(bala4)
        #-------
        cord_av=c.coords(avatar22)
        cords_flecha=c.coords(flecha1)
        #----
        cord_av2=c.coords(avatar33)
        cords_espada=c.coords(espada1)
        #----
        cord_av3=c.coords(avatar44)
        cords_garrote=c.coords(garrote1)
        #----
        cord_av4=c.coords(avatar55)
        cords_flecha2=c.coords(flecha2)

        cord_av5=c.coords(avatar66)
        cords_espada2=c.coords(espada2)
        
        if cords_bala[0]>-50:
            c.coords(bala4,cords_bala[0]-2,cords_bala[1])
            c.coords(flecha1,cords_flecha[0]-2,cords_flecha[1])
            c.coords(espada1,cords_espada[0]-2,cords_espada[1])
            c.coords(garrote1,cords_garrote[0]-2,cords_garrote[1])
            c.coords(flecha2,cords_flecha2[0]-2,cords_flecha2[1])
            c.coords(espada2,cords_espada2[0]-2,cords_espada2[1])
        if cords_bala[0]<=100: 
            c.coords(espada1,cord_av2[0],cord_av2[1]+15)
            
            c.coords(bala4,cords_alien[0],cords_alien[1]+15)
            
            c.coords(flecha1,cord_av[0],cord_av[1]+15)
            
            c.coords(garrote1,cord_av3[0],cord_av3[1]+15)

            c.coords(flecha2,cord_av4[0],cord_av4[1]+15)

            c.coords(espada2,cord_av5[0],cord_av5[1]+15)                        
        if OPEN==TRUE:
            top3.after(10,lambda:bala_enemigo())
    def crear_varias():
        
        crear()
        
        top3.after(70000000,lambda:crear_varias())
    crear_varias()
#----------------------------------------------------------------------------Proyectiles--------------------------------------------------------------
    #-------------------------------------------------Clases----------------------------------------------------------------------------------------------
    #Función de cronómetro  
    def cronometro():
        global TIME
        c2.delete(ALL)
        TIME=TIME+1
        time=c2.create_text(50,10, text=TIME,fill="Purple")
        if TIME==0:
            game_over()
        else:
            c2.after(1000,cronometro)
    c2=Canvas(top3,width=75,height=20,bg="white")
    c2.place(x=920,y=0)
    cronometro()
    #c.focus_set()
    #ventana.withdraw()
    top3.mainloop()
    
####################################################################################################################################################################  
####################################################################################################################################################################
def ventana_de_juego3():
    global top3
    global a1
    global c
    top3=Toplevel()
    top3.title('ventana de juego3')
    top3.minsize(1000,700)
    top3.resizable(width=NO, height=NO)
    c=Canvas(top3,width=1000,height=700,bg='white')
    c.place(x=0,y=0)
    b=Button(top3,text='volver a menu',command=close_juegos)
    b.place(x=500,y=650)
    Label23=Label(top3,text="User name:"+username1,bg='red',font=('Calibri',10),fg='white')
    Label23.place(x=875,y=65)
    #Variables 
    OPEN=True
    #Posiciones inciales tablero 
    y=135
    y2=232
    y3=315
    y4=410
    y5=486
    y6=565
    #Lista de posiciones en el tablero 
    list_posiciones=[y,y2,y3,y4,y5,y6]
    random.shuffle(list_posiciones)
    pos1=list_posiciones[0]
    pos2=list_posiciones[1]
    pos3=list_posiciones[2]
    pos4=list_posiciones[3]
    pos5=list_posiciones[4]
    pos6=list_posiciones[5] 
    ##lISTA DE IMAGENES RANDOM
    lis_avatars=["avatar escudero.png","avatar caníbal.png","avatar leñador.png","avatar flechero.png"]
    random.shuffle(lis_avatars)
    ava=lis_avatars[0]
    ava2=lis_avatars[1]
    ava3=lis_avatars[2]
    ava4=lis_avatars[3]
    ###########################
    global img
    global water1
    global my_img1
    #Imagen del tablero
    Tablero=cImagen("t.png")
    Tablerol=c.create_image(0,0,anchor=NW,image=Tablero)
    #Imagen de torres
    img=PhotoImage(file="Imgs\\sand1.png")
    my_img1=c.create_image(100,5,anchor=NW,image=img)
    #------
    rock=cImagen("rock.png")
    rock1=c.create_image(300,5,anchor=NW,image=rock)
    #---
    global fire 
    fire=cImagen("fire.png")
    fire1=c.create_image(500,5,anchor=NW,image=fire)
    #-----
    water=cImagen("water.png")
    water1=c.create_image(700,5,anchor=NW,image=water,tags='rook1')
    global avatar55
    #Imagenes de avatars
    avatar=cImagen('avatar leñador.png')
    avatar1=c.create_image(900,pos1,anchor=CENTER,image=avatar,tags='f1')
    #--------
    avatar2=cImagen('avatar flechero.png')
    avatar22=c.create_image(900,pos2,anchor=CENTER,image=avatar2,tags='f2')
    #--------
    avatar3=cImagen('avatar escudero.png')
    avatar33=c.create_image(900,pos3,anchor=CENTER,image=avatar3,tags='f3')
    #----
    avatar4=cImagen('avatar caníbal.png')
    avatar44=c.create_image(900,pos4,anchor=CENTER,image=avatar4,tags='f4')
    #----
    avatar5=cImagen('avatar flechero.png')
    avatar55=c.create_image(900,pos6,anchor=CENTER,image=avatar5,tags='f5')

    avatar6=cImagen('avatar escudero.png')
    avatar66=c.create_image(900,pos5,anchor=CENTER,image=avatar6,tags='avatar_escudero2')
    
    #Cagar imagenes de monedas
    global coin50
    global coin25
    global coin100
    global monedas
    coin50=cImagen('50 coin.png')
    coin25=cImagen('25 coin.png')
    coin100=cImagen('100 coin.png')
    
    monedas=[coin50,coin25,coin100]
    def crearcoin():
        global coin50
        global coin25
        global coin100
        global monedas
        global imaggg
        random.shuffle(monedas)
        imaggg=c.create_image(random.randint(100,600),random.randint(300,600),anchor=CENTER,image=monedas[0],tags=str(monedas[0]))
        top3.after(10000,lambda:crearcoin())
    Thread(target=crearcoin).start()

    ####################################################################################
    global imaggg
    #Creear imagenes de proyectiles
    ########################################Puedo usar la misma variable###################################################################
    bala3=cImagen("axe.png")
    bala4=c.create_image(0,0,image=bala3,tags='B',state=HIDDEN)
    
    flecha=cImagen("arrow.png")
    flecha1=c.create_image(0,0,image=flecha,tags='flecha',state=HIDDEN)

    espada=cImagen("sword.png")
    espada1=c.create_image(0,0,image=espada,tags='espada',state=HIDDEN)
    
    garrote=cImagen("garrote.png")
    garrote1=c.create_image(0,0,image=garrote,tags='garrote',state=HIDDEN)
    
    ###############################################################################################
    bullet=cImagen("fire ball.png")
    #bullet1=c.create_image(0,0,image=bullet,tags='bullet',state=HIDDEN)

    proyectil=cImagen("spikeball.png")

    proyectil2=cImagen("Water ball.png")

    def printt(event):
        print(event.x,event.y)

    c.bind("<ButtonPress-2>",printt)
    #########################################################################################################################################
    #----------------------------------------------------------------IMGS------------------------------------------------------------------------
    global var
    #global coin
    global laelcoi
    #coin=1000
    var=0
    labelcoi=Label(top3,text="Coins" +str(coin))
    labelcoi.place(x=920,y=30)
    def mouse_acc(event):
        global var
        global coin
        global imaggg
        rango=c.bbox(my_img1)#Sand rook
        rang=c.bbox(rock1)
        rang1=c.bbox(fire1)
        rang2=c.bbox(water1)
        rang3=c.bbox(imaggg)
        if event.x >=rango[0] and event.x < (rango[2]):
            if event.y >= rango[1] and event.y <(rango[3]):#Hago lo mismo nada mas que con otra imagen y con las variables 
                var=1
                coin=coin-50
                labelcoi.config(text="Coins"+str(coin))
        if event.x >=rang[0] and event.x < (rang[2]):#2
            if event.y >= rang[1] and event.y <(rang[3]):
                var=2
                coin=coin-100
                labelcoi.config(text="Coins"+str(coin))
        if event.x >=rang1[0] and event.x < (rang1[2]):#3
            if event.y >= rang1[1] and event.y <(rang1[3]):
                var=3
                coin=coin-150
                labelcoi.config(text="Coins"+str(coin))
        if event.x >=rang2[0] and event.x < (rang2[2]):#4
            if event.y >= rang2[1] and event.y <(rang2[3]):
                var=4
                coin=coin-200
                labelcoi.config(text="Coins"+str(coin))
        if event.x >=rang3[0] and event.x < (rang3[2]):#4
            if event.y >= rang3[1] and event.y <(rang3[3]):
                if str(monedas[0])==str(coin50):
                    coin=coin+50
                    labelcoi.config(text="Coins"+str(coin))
                    var=5
                if str(monedas[0])==str(coin25):
                    coin=coin+25
                    labelcoi.config(text="Coins"+str(coin))
                    var=5
                if str(monedas[0])==str(coin100):
                    coin=coin+100
                    labelcoi.config(text="Coins"+str(coin))
                    var=5
    
    global listadetorres
    global listadetorres1
    global listadetorres2
    listadetorres=[]
    listadetorres1=[]
    listadetorres2=[]
    def colocar_torre(event):#Para hacer otras imagenes cambio la variables 
        global var
        global coin
        global imgz
        if var==1:
            c.create_image(event.x,event.y,anchor=CENTER,image=img,state=NORMAL,tags='aaa'+str(len(listadetorres)))
            listadetorres.append(c.create_image(event.x,event.y,anchor=CENTER,image=img,state=NORMAL,tags='aaa'+str(len(listadetorres))))
            proyectiles()
            c.update()
            var=0
        if var==2:
            c.create_image(event.x,event.y,anchor=CENTER,image=rock,state=NORMAL,tags='aaa'+str(len(listadetorres)))
            listadetorres.append(c.create_image(event.x,event.y,anchor=CENTER,image=rock,state=NORMAL,tags='aaa'+str(len(listadetorres))))
            proyectiles()
            c.update()
            var=0
        if var==3:
            c.create_image(event.x,event.y,image=fire,state=NORMAL,tags='ccc'+str(len(listadetorres1)))
            listadetorres1.append(c.create_image(event.x,event.y,image=fire,state=NORMAL,tags='ccc'+str(len(listadetorres1))))
            proyectiles2()
            c.update()
            var=0
        if var==4:
            c.create_image(event.x,event.y,anchor=CENTER,image=water,tags='torre'+str(len(listadetorres2)))
            listadetorres2.append(c.create_image(event.x,event.y,anchor=CENTER,image=water,tags='torre'+str(len(listadetorres2))))
            proyectiles3()
            c.update()
            var=0
        if var==5:
            c.delete(imaggg)
            c.update()
            var=0    
    c.bind("<ButtonPress-1>",mouse_acc)
    c.bind("<ButtonRelease-1>",colocar_torre)

    #Colisiones entre las torres
    global vida_torre
    global vida_torre2
    global vida_torres3
    vida_torre=20
    vida_torre2=16
    vida_torres3=25    
    def eliminar():
        global vida_torre
        if len(listadetorres1)>=1:
            for b in range(0,len(listadetorres1)):
                bx=c.bbox("espada")
                bx1=c.bbox("garrote")
                bx2=c.bbox("B")
                bx3=c.bbox("flecha")
                bx4=c.bbox("flecha2")
                bx5=c.bbox("espada2")
                sbx=c.bbox(listadetorres1[b])
                if (bx1[2]in range ((sbx[0]),(sbx[2]-99))) and  ((bx1[1] in range(sbx[1],sbx[3]))):
                    vida_torre-=4
                    vidas_torres()
                if (bx[2]in range ((sbx[0]),(sbx[2]-99))) and ((bx[1] in range(sbx[1],sbx[3]))):
                    vida_torre-=2
                    vidas_torres()
                if (bx2[2]in range ((sbx[0]),(sbx[2]-99))) and ((bx2[1] in range(c.bbox(listadetorres1[b])[1],c.bbox(listadetorres1[b])[3]))):
                    vida_torre-=3
                    vidas_torres()
                if (bx3[2]in range ((sbx[0]),(sbx[2]-98))) and ((bx3[1] in range(c.bbox(listadetorres1[b])[1],c.bbox(listadetorres1[b])[3]))):
                    vida_torre-=1
                    vidas_torres()
                if (bx4[2]in range ((sbx[0]),(sbx[2]-98))) and ((bx4[1] in range(c.bbox(listadetorres1[b])[1],c.bbox(listadetorres1[b])[3]))):
                    vida_torre-=1
                    vidas_torres()

                if (bx5[2]in range ((sbx[0]),(sbx[2]-98))) and ((bx5[1] in range(c.bbox(listadetorres1[b])[1],c.bbox(listadetorres1[b])[3]))):
                    vida_torre-=4
                    vidas_torres()
                            
        if OPEN==TRUE:
            top3.after(1,lambda:eliminar())
    t1=Thread(target=eliminar)
    t1.start()
    def eliminar_torres():
        global vida_torre2
        if len(listadetorres)>=1:
            for b in range(0,len(listadetorres)):
                bx=c.bbox("espada")
                bx1=c.bbox("garrote")
                bx2=c.bbox("B")
                bx3=c.bbox("flecha")
                bx4=c.bbox("flecha2")
                bx5=c.bbox("espada2")
                sbx=c.bbox(listadetorres[b])
                if (bx1[2]in range ((sbx[0]),(sbx[2]-99))) and  ((bx1[1] in range(sbx[1],sbx[3]))):
                    vida_torre2-=4
                    vidas_torres()
                if (bx[2]in range ((sbx[0]),(sbx[2]-99))) and ((bx[1] in range(sbx[1],sbx[3]))):
                    vida_torre2-=2
                    vidas_torres()
                if (bx2[2]in range ((sbx[0]),(sbx[2]-99))) and ((bx2[1] in range(c.bbox(listadetorres[b])[1],c.bbox(listadetorres[b])[3]))):
                    vida_torre2-=3
                    vidas_torres()
                if (bx3[2]in range ((sbx[0]),(sbx[2]-98))) and ((bx3[1] in range(c.bbox(listadetorres[b])[1],c.bbox(listadetorres[b])[3]))):
                    vida_torre2-=1
                    vidas_torres()
                if (bx4[2]in range ((sbx[0]),(sbx[2]-98))) and ((bx4[1] in range(c.bbox(listadetorres[b])[1],c.bbox(listadetorres[b])[3]))):
                    vida_torre2-=1
                    vidas_torres()
                if (bx5[2]in range ((sbx[0]),(sbx[2]-98))) and ((bx5[1] in range(c.bbox(listadetorres[b])[1],c.bbox(listadetorres[b])[3]))):
                    vida_torre2-=4
                    vidas_torres()

                    
        if OPEN==TRUE:
            top3.after(1,lambda:eliminar_torres())
        
    t2=Thread(target=eliminar_torres)
    t2.start()    
    def eliminar_torres2():
        global vida_torres3
        if len(listadetorres2)>=1:
            for b in range(0,len(listadetorres2)):
                bx=c.bbox("espada")
                bx1=c.bbox("garrote")
                bx2=c.bbox("B")
                bx3=c.bbox("flecha")
                bx4=c.bbox("flecha2")
                bx5=c.bbox("espada2")
                sbx=c.bbox(listadetorres2[b])
                if (bx1[2]in range ((sbx[0]),(sbx[2]-99))) and  ((bx1[1] in range(sbx[1],sbx[3]))):
                    vida_torres3-=4
                    vidas_torres()
                if (bx[2]in range ((sbx[0]),(sbx[2]-99))) and ((bx[1] in range(sbx[1],sbx[3]))):
                    vida_torres3-=2
                    vidas_torres()
                if (bx2[2]in range ((sbx[0]),(sbx[2]-99))) and ((bx2[1] in range(c.bbox(listadetorres2[b])[1],c.bbox(listadetorres2[b])[3]))):
                    vida_torres3-=3
                    vidas_torres()
                if (bx3[2]in range ((sbx[0]),(sbx[2]-98))) and ((bx3[1] in range(c.bbox(listadetorres2[b])[1],c.bbox(listadetorres2[b])[3]))):
                    vida_torres3-=1
                    vidas_torres()
                if (bx4[2]in range ((sbx[0]),(sbx[2]-98))) and ((bx4[1] in range(c.bbox(listadetorres2[b])[1],c.bbox(listadetorres2[b])[3]))):
                    vida_torres3-=1
                    vidas_torres()
                if (bx5[2]in range ((sbx[0]),(sbx[2]-98))) and ((bx5[1] in range(c.bbox(listadetorres2[b])[1],c.bbox(listadetorres2[b])[3]))):
                    vida_torres3-=4
                    vidas_torres()
        if OPEN==TRUE:
            top3.after(1,lambda:eliminar_torres2())
    t3=Thread(target=eliminar_torres2)
    t3.start()
    def vidas_torres():
        global vida_torre
        global vida_torre2
        global vida_torres3
        if vida_torre<=0:
            c.move(c.gettags(listadetorres1[len(listadetorres1)-1]),40000,40000)
            vida_torre=10
            c.update()
        if vida_torre2<=0:
            c.move(c.gettags(listadetorres[len(listadetorres)-1]),20000,20000)
            vida_torre2=7
            c.update()
        if vida_torres3<=0:
            c.move(c.gettags(listadetorres2[len(listadetorres2)-1]),20000,20000)
            vida_torres3=12
            c.update()
    #Seccion de proyectiles 
    global listadeproyec
    global listadeproyec1
    global listadeproyec2
    listadeproyec=[]
    listadeproyec1=[]
    listadeproyec2=[]
    def proyectiles():
     
        if len(listadetorres)>=1:
            c.coords(listadetorres[len(listadetorres)-1])
            listadeproyec.append(c.create_image(c.coords(listadetorres[len(listadetorres)-1])[0],c.coords(listadetorres[len(listadetorres)-1])[1],
                                                image=bullet,state=NORMAL,tags='ff'+str(len(listadeproyec))))    
    def proyectiles2():
        if len(listadetorres1)>=1:
            c.coords(listadetorres1[len(listadetorres1)-1])
            listadeproyec1.append(c.create_image(c.coords(listadetorres1[len(listadetorres1)-1])[0],c.coords(listadetorres1[len(listadetorres1)-1])[1],
                                                 image=proyectil,state=NORMAL,tags='aa'+str(len(listadeproyec1))))
    def proyectiles3():
        if len(listadetorres2)>=1:
            c.coords(listadetorres2[len(listadetorres2)-1])
            listadeproyec2.append(c.create_image(c.coords(listadetorres2[len(listadetorres2)-1])[0],c.coords(listadetorres2[len(listadetorres2)-1])[1],
                                                 image=proyectil2,state=NORMAL,tags='Img'+str(len(listadeproyec2))))
    #Vidas de los avatars
    global vida_avatar_lenandor
    global vida_avatar_escudero
    global vida_avatar_canibal
    global vida_avatar_flechero1
    global vida_avatar_flechero2
    global vida_avatar_escudero2
    
    vida_avatar_lenandor=10
    vida_avatar_escudero=8
    vida_avatar_canibal=12
    vida_avatar_flechero1=4
    vida_avatar_flechero2=4
    vida_avatar_escudero2=8
    ########################################################
    mixer.init()
    impact_sound_effect=mixer.Sound("Impacto.wav")
    #########################################################
    def moverlistadeproyectiles():
        global vida_avatar_lenandor
        global vida_avatar_escudero
        global vida_avatar_canibal
        global vida_avatar_flechero1
        global vida_avatar_flechero2
        global vida_avatar_escudero2
        if len(listadeproyec)>=1:
            for j in range(0,len(listadeproyec)):
                c.coords((c.gettags(listadeproyec[j])),c.coords((listadeproyec[j]))[0]+1,c.coords((listadeproyec[j]))[1])
                if c.bbox('avatar_escudero2')[0]<c.bbox(listadeproyec[j])[2]<c.bbox('avatar_escudero2')[2]-97 and c.bbox('avatar_escudero2')[1]<c.bbox(listadeproyec[j])[1]<c.bbox('avatar_escudero2')[3]:
                    vida_avatar_escudero2-=2
                    avatar_dead()
                    impact_sound_effect.play()
                if c.bbox('f1')[0]<c.bbox(listadeproyec[j])[2]<c.bbox('f1')[2]-97 and c.bbox('f1')[1]<c.bbox(listadeproyec[j])[1]<c.bbox('f1')[3]:
                    vida_avatar_lenandor-=2
                    avatar_dead()
                    impact_sound_effect.play()
                if c.bbox('f3')[0]<c.bbox(listadeproyec[j])[2]<c.bbox('f3')[2]-97 and c.bbox('f3')[1]<c.bbox(listadeproyec[j])[1]<c.bbox('f3')[3]:
                    vida_avatar_escudero-=2
                    avatar_dead()
                    impact_sound_effect.play()
                if c.bbox('f4')[0]<c.bbox(listadeproyec[j])[2]<c.bbox('f4')[2]-97 and c.bbox('f4')[1]<c.bbox(listadeproyec[j])[1]<c.bbox('f4')[3]:
                    vida_avatar_canibal-=2
                    avatar_dead()
                    impact_sound_effect.play()
                if c.bbox('f2')[0]<c.bbox(listadeproyec[j])[2]<c.bbox('f2')[2]-97 and c.bbox('f2')[1]<c.bbox(listadeproyec[j])[1]<c.bbox('f2')[3]:
                    vida_avatar_flechero1-=2
                    avatar_dead()
                    impact_sound_effect.play()
                    
                if c.bbox('f5')[0]<c.bbox(listadeproyec[j])[2]<c.bbox('f5')[2]-97 and c.bbox('f5')[1]<c.bbox(listadeproyec[j])[1]<c.bbox('f5')[3]:
                    vida_avatar_flechero2-=1.5
                    avatar_dead()
                    impact_sound_effect.play()                    
                if c.coords((listadeproyec[j]))[0]>1000:
                    c.coords((c.gettags(listadeproyec[j])),c.coords((listadetorres[j]))[0],c.coords((listadetorres[j]))[1])
       
        if OPEN==TRUE:
            top3.after(10,lambda:moverlistadeproyectiles())
       
    a=Thread(target=moverlistadeproyectiles)
    a.start()
    
    #Esta funcion mueve la lista de los proyectiles del  ROCK ROOK 
    def moverlistadeproyectiles2():
        global vida_avatar_lenandor
        global vida_avatar_escudero
        global vida_avatar_canibal
        global vida_avatar_flechero1
        global vida_avatar_flechero2
        global vida_avatar_escudero2
        if len(listadeproyec1)>=1:
            for k in range(0,len(listadeproyec1)):
                           c.coords((c.gettags(listadeproyec1[k])),c.coords((listadeproyec1[k]))[0]+1,c.coords((listadeproyec1[k]))[1])
                           if c.bbox('avatar_escudero2')[0]<c.bbox(listadeproyec1[k])[2]<c.bbox('avatar_escudero2')[2]-97 and c.bbox('avatar_escudero2')[1]<c.bbox(listadeproyec1[k])[1]<c.bbox('avatar_escudero2')[3]:
                               vida_avatar_escudero2-=3
                               avatar_dead()
                               impact_sound_effect.play()
                           if c.bbox('f5')[0]<c.bbox(listadeproyec1[k])[2]<c.bbox('f5')[2]-97 and c.bbox('f5')[1]<c.bbox(listadeproyec1[k])[1]<c.bbox('f5')[3]:
                               vida_avatar_flechero2-=3
                               avatar_dead()
                               impact_sound_effect.play()             

                           if c.bbox('f2')[0]<c.bbox(listadeproyec1[k])[2]<c.bbox('f2')[2]-97 and c.bbox('f2')[1]<c.bbox(listadeproyec1[k])[1]<c.bbox('f2')[3]:
                                vida_avatar_flechero1-=3
                                avatar_dead()
                                impact_sound_effect.play()

                           if c.bbox('f4')[0]<c.bbox(listadeproyec1[k])[2]<c.bbox('f4')[2]-97 and c.bbox('f4')[1]<c.bbox(listadeproyec1[k])[1]<c.bbox('f4')[3]:
                               vida_avatar_canibal-=3
                               avatar_dead()
                               impact_sound_effect.play()
                           
                           if c.bbox('f1')[0]<c.bbox(listadeproyec1[k])[2]<c.bbox('f1')[2]-97 and c.bbox('f1')[1]<c.bbox(listadeproyec1[k])[1]<c.bbox('f1')[3]:
                               vida_avatar_lenandor-=3
                               avatar_dead()
                               impact_sound_effect.play()
                        
                           if c.bbox('f3')[0]<c.bbox(listadeproyec1[k])[2]<c.bbox('f3')[2]-97 and c.bbox('f3')[1]<c.bbox(listadeproyec1[k])[1]<c.bbox('f3')[3]:
                               vida_avatar_escudero-=3
                               avatar_dead()
                               impact_sound_effect.play()
                           elif c.coords((listadeproyec1[k]))[0]>1000:
                               c.coords((c.gettags(listadeproyec1[k])),c.coords((listadetorres1[k]))[0],c.coords((listadetorres1[k]))[1])
                        
        if OPEN==TRUE:
            top3.after(10,lambda:moverlistadeproyectiles2())                           
    a1=Thread(target=moverlistadeproyectiles2)
    a1.start()
    def avatar_dead():
        global coin
        if vida_avatar_lenandor<=0:
            coin=coin+75
            labelcoi.config(text="Coins"+str(coin))
            c.move('f1',8000,8000)
        if vida_avatar_escudero<=0:
            coin=coin+75
            labelcoi.config(text="Coins"+str(coin))
            c.move('f3',8000,8000)
        if vida_avatar_canibal<=0:
            coin=coin+75
            labelcoi.config(text="Coins"+str(coin))
            c.move('f4',8000,8000)
        if vida_avatar_flechero1<=0:
            coin=coin+75
            labelcoi.config(text="Coins"+str(coin))
            c.move('f2',8000,8000)
        if vida_avatar_flechero2<=0:
            coin=coin+75
            labelcoi.config(text="Coins"+str(coin))
            c.move('f5',8000,8000)
        if vida_avatar_escudero2<=0:
            coin=coin+75
            labelcoi.config(text="Coins"+str(coin))
            c.move('avatar_escudero2',8000,8000)
        if vida_avatar_lenandor<=0 and vida_avatar_escudero<=0 and vida_avatar_canibal<=0 and vida_avatar_flechero1<=0 and vida_avatar_flechero2<=0 and vida_avatar_escudero2<=0:
            win_game()
    def moverlistadeproyectiles3():
        global vida_avatar_lenandor
        global vida_avatar_escudero
        global vida_avatar_canibal
        global vida_avatar_flechero1
        global vida_avatar_flechero2
        global vida_avatar_escudero2
        if len(listadeproyec2)>=1:
            for i in range(0,len(listadeproyec2)):
                           c.coords((c.gettags(listadeproyec2[i])),c.coords((listadeproyec2[i]))[0]+1,c.coords((listadeproyec2[i]))[1])
                           if c.bbox('avatar_escudero2')[0]<c.bbox(listadeproyec2[i])[2]<c.bbox('avatar_escudero2')[2]-97 and c.bbox('avatar_escudero2')[1]<c.bbox(listadeproyec2[i])[1]<c.bbox('avatar_escudero2')[3]:
                               vida_avatar_escudero2-=3
                               avatar_dead()
                               impact_sound_effect.play()
                           
                           if c.bbox('f5')[0]<c.bbox(listadeproyec2[i])[2]<c.bbox('f5')[2]-97 and c.bbox('f5')[1]<c.bbox(listadeproyec2[i])[1]<c.bbox('f5')[3]:
                               vida_avatar_flechero2-=3
                               avatar_dead()
                               impact_sound_effect.play()
                           if c.bbox('f2')[0]<c.bbox(listadeproyec2[i])[2]<c.bbox('f2')[2]-97 and c.bbox('f2')[1]<c.bbox(listadeproyec2[i])[1]<c.bbox('f2')[3]:
                               vida_avatar_flechero1-=3
                               avatar_dead()
                               impact_sound_effect.play()
                           if c.bbox('f4')[0]<c.bbox(listadeproyec2[i])[2]<c.bbox('f4')[2]-97 and c.bbox('f4')[1]<c.bbox(listadeproyec2[i])[1]<c.bbox('f4')[3]:
                               vida_avatar_canibal-=3
                               avatar_dead()
                               impact_sound_effect.play()
                           if c.bbox('f1')[0]<c.bbox(listadeproyec2[i])[2]<c.bbox('f1')[2]-97 and c.bbox('f1')[1]<c.bbox(listadeproyec2[i])[1]<c.bbox('f1')[3]:
                               vida_avatar_lenandor-=3
                               avatar_dead()
                               impact_sound_effect.play()
                            
                           if c.bbox('f3')[0]<c.bbox(listadeproyec2[i])[2]<c.bbox('f3')[2]-97 and c.bbox('f3')[1]<c.bbox(listadeproyec2[i])[1]<c.bbox('f3')[3]:
                               vida_avatar_escudero-=3
                               avatar_dead()
                               impact_sound_effect.play()
                              
                           if c.coords((listadeproyec2[i]))[0]>1000:
                               c.coords((c.gettags(listadeproyec2[i])),c.coords((listadetorres2[i]))[0],c.coords((listadetorres2[i]))[1])
        if OPEN==TRUE:
            top3.after(9,lambda:moverlistadeproyectiles3())

    a2=Thread(target=moverlistadeproyectiles3)
    a2.start()
############################################################################################################################################           
    def play_music():
        mixer.init()
        mixer.music.load("musica.wav")
        mixer.music.play(-1)
    def stop_music():
        mixer.music.stop()
    playBtn=Button(top3,text="Play Music",command=play_music)
    playBtn.place(x=100,y=655)
    stopBtn=Button(top3,text="Stop Music",command=stop_music)
    stopBtn.place(x=300,y=655)
    ####################################################################
    #MOVIMIENTO BÁSICO DE LOS ENEMIGOS     
    def mov():
        cord=c.coords('f1')
        cord1=c.coords('f2')
        cord2=c.coords('f3')
        cord3=c.coords('f4')
        cord4=c.coords('f5')
        cord5=c.coords('avatar_escudero2')
        if cord[0]!=150:
            c.coords('f1',cord[0]-1.5,cord[1])
        if cord1[0]!=150:
            c.coords('f2',cord1[0]-1.5,cord1[1])
        if cord2[0]!=150:
            c.coords('f3',cord2[0]-1.5,cord2[1])
        if cord3[0]!=150:
            c.coords('f4',cord3[0]-1.5,cord3[1])
        if cord4[0]!=150:
            c.coords('f5',cord4[0]-1.5,cord4[1])
        if cord5[0]!=150:
            c.coords('avatar_escudero2',cord5[0]-1.5,cord5[1])
        else:
            game_over()
        if OPEN==True:
            top3.after(100,lambda:mov())
    Thread(target=mov).start()
    def game_over():
        top3.destroy()
        game_over=Toplevel()
        game_over.title("game_over")
        game_over.minsize(1000,700)
        game_over.resizable(width=NO,height=NO)
        game_over_canvas=Canvas(game_over,width=1000,height=700,bg='white')
        game_over_canvas.place(x=0,y=0)
        game_over_canvas.image2=cImagen("Wallpaper.png")
        imgcanvas2=game_over_canvas.create_image(0,0,anchor=NW,image=game_over_canvas.image2)
        Labe=Label(game_over,text="GAME OVer",bg="red",font=("Arial bold",10),fg='white')
        Labe.place(x=300,y=300)

    def win_game():
        top3.destroy()
        win_game1=Toplevel()
        win_game1.title("WIN")
        win_game1.minsize(1000,700)
        win_game1.resizable(width=NO,height=NO)
        win_gamecanvas=Canvas(win_game1,width=1000,height=700,bg='white')
        win_gamecanvas.place(x=0,y=0)
        win_gamecanvas.image2=cImagen("Wallpaper.png")
        imgcanvas2=win_gamecanvas.create_image(0,0,anchor=NW,image=win_gamecanvas.image2)
        Labe=Label(win_game1,text="YOU WIN",bg="red",font=("Arial bold",10),fg='white',width=15,height=5)
        Labe.place(x=300,y=300)
        def updatefile():
            global TIME
            f=open('scores.txt','r')
            file=f.readlines()
            last=int(file[0])
            x=str(TIME)
            a=len(x)+1
            b=x.ljust(a)
            f.close()
            file=open('scores.txt','a')
            file.write('\n'+b)
        updatefile()
        def updatefile2():
            f1=open('scores.txt','r')
            file2=f1.readlines()
            last2=str(file2[4])
            x=sorted(file2,reverse=True)
            a=prod_escalar(x)
            a.sort(reverse=False)
            higscore=Label(win_game1,text="High score1 :"+str(a[0]),bg="red",font=("Arial bold",15),fg='white')
            higscore.place(x=500,y=0)
            higscore1=Label(win_game1,text="High score2:"+str(a[1]),bg="red",font=("Arial bold",15),fg='white')
            higscore1.place(x=500,y=100)
            higscore2=Label(win_game1,text="High score3:"+str(a[2]),bg="red",font=("Arial bold",15),fg='white')
            higscore2.place(x=500,y=200)
            higscore3=Label(win_game1,text="High score4:"+str(a[3]),bg="red",font=("Arial bold",15),fg='white')
            higscore3.place(x=500,y=300)
            higscore4=Label(win_game1,text="High score5:"+str(a[4]),bg="red",font=("Arial bold",15),fg='white')
            higscore4.place(x=500,y=400)
        def prod_escalar(vec1):
            return prod_escalar_aux(vec1,0,len(vec1),[])

        def prod_escalar_aux(vec1,i,n,vecr):
            if i==n:
                return vecr
            else:
                vecr.append(int(vec1[i]))
                return prod_escalar_aux(vec1,i+1,n,vecr)
        updatefile2()
    #---------------------------------------------------------------------------------------------------------------------------------
    #Crear balas de enemigos tengo que cambiar cosas animacion
    #-----------------------------------------------------------------Proyectiles-----------------------------------------------------    
    def crear():
        global bala4
        global flecha1
        global espada1
        global garrote1
        global flecha2
        global espada2
        cords_alien=c.coords(avatar1)
        cords_bala=c.coords('B')
        #-------
        cord_av=c.coords(avatar22)
        cords_flecha=c.coords('flecha')
        #--------

        cord_av2=c.coords(avatar33)
        cords_espada=c.coords('espada')
        #--------
        cord_av3=c.coords(avatar44)
        cords_garrote=c.coords('garrote')

        cord_av4=c.coords(avatar55)


        cord_av5=c.coords(avatar66)
        
        bala4=c.create_image(cords_alien[0],cords_alien[1]+15,image=bala3,tags='B',state=NORMAL)
        #1  
        flecha1=c.create_image(cord_av[0],cord_av[1]+15,image=flecha,tags='flecha',state=NORMAL)
        #2
        flecha2=c.create_image(cord_av4[0],cord_av4[1]+15,image=flecha,tags='flecha2',state=NORMAL)
        
        #1
        espada1=c.create_image(cord_av2[0],cord_av2[1]+15,image=espada,tags='espada',state=NORMAL)

        #2
        espada2=c.create_image(cord_av5[0],cord_av5[1]+15,image=espada,tags='espada2',state=NORMAL)
        
        garrote1=c.create_image(cord_av3[0],cord_av3[1]+15,image=garrote,tags='garrote',state=NORMAL)    

        
        bala_enemigo()

    def bala_enemigo():
        global bala4
        global flecha1
        global espada1
        global garrote1
        global flecha2
        global espada2
        cords_alien=c.coords(avatar1)
        cords_bala=c.coords(bala4)
        #-------
        cord_av=c.coords(avatar22)
        cords_flecha=c.coords(flecha1)
        #----
        cord_av2=c.coords(avatar33)
        cords_espada=c.coords(espada1)
        #----
        cord_av3=c.coords(avatar44)
        cords_garrote=c.coords(garrote1)
        #----
        cord_av4=c.coords(avatar55)
        cords_flecha2=c.coords(flecha2)

        cord_av5=c.coords(avatar66)
        cords_espada2=c.coords(espada2)
        
        if cords_bala[0]>-50:
            c.coords(bala4,cords_bala[0]-2,cords_bala[1])
            c.coords(flecha1,cords_flecha[0]-2,cords_flecha[1])
            c.coords(espada1,cords_espada[0]-2,cords_espada[1])
            c.coords(garrote1,cords_garrote[0]-2,cords_garrote[1])
            c.coords(flecha2,cords_flecha2[0]-2,cords_flecha2[1])
            c.coords(espada2,cords_espada2[0]-2,cords_espada2[1])
        if cords_bala[0]<=100: 
            c.coords(espada1,cord_av2[0],cord_av2[1]+15)
            
            c.coords(bala4,cords_alien[0],cords_alien[1]+15)
            
            c.coords(flecha1,cord_av[0],cord_av[1]+15)
            
            c.coords(garrote1,cord_av3[0],cord_av3[1]+15)

            c.coords(flecha2,cord_av4[0],cord_av4[1]+15)

            c.coords(espada2,cord_av5[0],cord_av5[1]+15)                        
        if OPEN==TRUE:
            top3.after(10,lambda:bala_enemigo())
    def crear_varias():
        
        crear()
        
        top3.after(70000000,lambda:crear_varias())
    crear_varias()
#----------------------------------------------------------------------------Proyectiles--------------------------------------------------------------
    #-------------------------------------------------Clases----------------------------------------------------------------------------------------------
    #Función de cronómetro  
    def cronometro():
        global TIME
        c2.delete(ALL)
        TIME=TIME+1
        time=c2.create_text(50,10, text=TIME,fill="Purple")
        if TIME==0:
            game_over()
        else:
            c2.after(1000,cronometro)
    c2=Canvas(top3,width=75,height=20,bg="white")
    c2.place(x=920,y=0)
    cronometro()

    
    #c.focus_set()
    #ventana.withdraw()
    top3.mainloop()
























































btn_entry=Button(C_principal,text='Ayuda',bg='red',fg='white',height=2,width=15,command=abrirayuda)
btn_entry.place(x=550,y=150)

btn_entry2=Button(C_principal,text='Créditos',bg='red',fg='white',height=2,width=15,command=abrircreditos)
btn_entry2.place(x=550,y=250)

btn_entry3=Button(C_principal,text='Register',bg='red',fg='white',height=2,width=15,command=register)
btn_entry3.place(x=550,y=450)

btn_entry5=Button(C_principal,text='Login',bg='red',fg='white',height=2,width=15,command=login)
btn_entry5.place(x=550,y=550)



btn_entry4=Button(C_principal,text='Game',bg='red',fg='white',height=2,width=15,command=juego)
btn_entry4.place(x=550,y=350)

btn_entry7=Button(C_principal,text='Higscore',bg='red',fg='white',height=2,width=15,command=abrirventaA)
btn_entry7.place(x=200,y=200)

C_principal.fondo=cImagen("Wallpaper.png")
imgcanvas=C_principal.create_image(0,0,anchor=NW,image=C_principal.fondo)
ventana.mainloop()
