import tkinter
from tkinter import *
from tkinter import ttk 

import random 

############# cores #############
co0 = "#444466" # Preta
co1 = "#feffff" # branca
co2 = "#6f9fbd" # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"    # letra 
co5 = "#e06636"    # - profit 
co6 = "#6dd695"    # + profit
co7 = "#ef5350"    # vermelha
co8 = "#00bfa5"    # + verde
fundo = "#3b3b3b"
co10 ="#fcfbf7"

cor1 = '#f58b5d'
cor2 = '#ff333a'
cor3 = '#6bd66f'
cor4 = "#ab8918"

janela = Tk()
janela.title('')
janela.geometry('350x280')
janela.configure(bg=fundo)

#################### Frames #################

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=2, ipadx=280)

frame_top = Frame(janela, width=350, height=30,bg=co1, pady=0,padx=0, relief="flat",)
frame_top.grid(row=1, column=0, sticky=NW)
frame_corpo = Frame(janela, width=350, height=280,bg=fundo, pady=0,padx=0, relief="flat",)
frame_corpo.grid(row=2, column=0,  sticky=NW)

style = ttk.Style(janela)
style.theme_use("clam")

# configurando frame top (topo do quadro)
app_nome = Label(frame_top, text = "ADIVINHA O NUMERO", anchor='center', font=('verdana 14 bold'), bg=co1, fg=co3)
app_nome.place(x=55, y=0)

# funcao iniciar o jogo

tentativas = 5
pontuacao = 0

def iniciar_jogo():
    l_regra_1['text'] = ''
    l_regra_2['text'] = ''
    l_regra_3['text'] = ''
    
    numeros = random.sample(range(1,10),8)
    resposta = random.choice(numeros)
    
    def estado_do_valor(v):
        
        numeros = random.sample(range(1,10),8)
        resposta = [random.choice(numeros)]
        
        global tentativas
        global pontuacao
        
        for i in resposta:
            print(i)
            if v == i:
                tentativas += 2
                pontuacao += 10
                l_tentativas['text'] = str(tentativas) + 'Tentativas'
                l_pontos['text'] = 'Pontuacao : ' + str(pontuacao)
                             
            else:
                tentativas -= 1
                l_tentativas['text'] = str(tentativas) + 'Tentativas'
                
                #desabilitando os botões apos tentativas ser igual a 0                
                if tentativas <=0:
                     b_1['state'] = 'disable'   
                     b_2['state'] = 'disable'   
                     b_3['state'] = 'disable'   
                     b_4['state'] = 'disable'   
                     b_5['state'] = 'disable'   
                     b_6['state'] = 'disable'   
                     b_7['state'] = 'disable'   
                     b_8['state'] = 'disable'  
                                          
                     b_1['text'] = ''   
                     b_1['text'] = ''   
                     b_1['text'] = ''   
                     b_2['text'] = ''   
                     b_3['text'] = ''   
                     b_4['text'] = ''   
                     b_5['text'] = ''   
                     b_6['text'] = ''   
                     b_7['text'] = ''   
                     b_8['text'] = ''    

                       
                    # chamar a funcao game over
                     game_over()
                
                else:
                     pass
                    

    b_1 = Button(frame_corpo, command=lambda: estado_do_valor(numeros[0]) ,text = numeros[0], width=5, height=2,  font=('Ivy 15 bold'), bg=co10, fg=co0,relief=RAISED, overrelief=RIDGE)
    b_1.place(x=40, y=70)
    
    b_2 = Button(frame_corpo, command=lambda: estado_do_valor(numeros[1]) ,text = numeros[1], width=5, height=2,  font=('Ivy 15 bold'), bg=co10, fg=co0,relief=RAISED, overrelief=RIDGE)
    b_2.place(x=108, y=70)
    
    b_3 = Button(frame_corpo, command=lambda: estado_do_valor(numeros[2]) ,text = numeros[2], width=5, height=2,  font=('Ivy 15 bold'), bg=co10, fg=co0,relief=RAISED, overrelief=RIDGE)
    b_3.place(x=176, y=70)
    
    b_4 = Button(frame_corpo, command=lambda: estado_do_valor(numeros[3]) ,text = numeros[3], width=5, height=2,  font=('Ivy 15 bold'), bg=co10, fg=co0,relief=RAISED, overrelief=RIDGE)
    b_4.place(x=244, y=70)
   
    b_5 = Button(frame_corpo, command=lambda: estado_do_valor(numeros[4]) ,text = numeros[4], width=5, height=2,  font=('Ivy 15 bold'), bg=co10, fg=co0,relief=RAISED, overrelief=RIDGE)
    b_5.place(x=40, y=133)
    
    b_6 = Button(frame_corpo, command=lambda: estado_do_valor(numeros[5]) ,text = numeros[5], width=5, height=2,  font=('Ivy 15 bold'), bg=co10, fg=co0,relief=RAISED, overrelief=RIDGE)
    b_6.place(x=108, y=133)
    
    b_7 = Button(frame_corpo, command=lambda: estado_do_valor(numeros[6]) ,text = numeros[6], width=5, height=2,  font=('Ivy 15 bold'), bg=co10, fg=co0,relief=RAISED, overrelief=RIDGE)
    b_7.place(x=176, y=133)
    
    b_8 = Button(frame_corpo, command=lambda: estado_do_valor(numeros[7]) ,text = numeros[7], width=5, height=2,  font=('Ivy 15 bold'), bg=co10, fg=co0,relief=RAISED, overrelief=RIDGE)
    b_8.place(x=244, y=133)
    
    
def game_over():
    global tentativas
    global pontuacao
     
    l_pontuacao = Label(frame_corpo, text = 'Voce pontuou : ' + str(pontuacao) + ' pontos', relief='raised', anchor='center', font=('ivy 15 bold'), bg=co1, fg=co2)
    l_pontuacao.place(x=52, y=90)
    
    l_jogo = Label(frame_corpo, text = 'GAME OVER', relief='raised', anchor='center', font=('ivy 15 bold'), bg=co1, fg=co2)
    l_jogo.place(x=130, y=120)
    
    tentativas = 5
    pontuacao = 0
    
    l_tentativas['text'] = str(tentativas) + 'Tentativas'
    l_pontos['text'] = 'Pontuacao : ' + str(pontuacao)
    
    b_jogar = Button (frame_corpo,command=iniciar_jogo, text = 'Jogar', width=17, font=('Ivy 12 bold'), bg=co10, fg=co0,relief=RAISED, overrelief=RIDGE)
    b_jogar.place(x=100, y=150)
    
         
# configurando frame baixo (parte de baixo do quadro)
l_pontos = Label(frame_corpo, text = 'Pontuação: 0', anchor='center', font=('Ivy 12 bold'), bg=fundo, fg=co1)
l_pontos.place(x=40, y=30)

l_tentativas = Label(frame_corpo, text = 'Tentativas: 5', anchor='center', font=('Ivy 12 bold'), bg=fundo, fg=co1)
l_tentativas.place(x=205, y=30)

l_linha = Label(frame_corpo, text = '', width=90, anchor='center', font=('Ivy 4'), bg=cor3, fg=co1)
l_linha.place(x=39, y=59)

l_regra_1 = Label(frame_corpo, text = 'Tenta adivinhar o numero para pontuar', anchor='center', font=('Ivy 8 bold'), bg=fundo, fg=co1)
l_regra_1.place(x=40, y=80)

l_regra_2 = Label(frame_corpo, text = 'Se voce acertar, voce ganhara + 2 chances', anchor='center', font=('Ivy 8 bold'), bg=fundo, fg=co1)
l_regra_2.place(x=40, y=110)

l_regra_3 = Label(frame_corpo, text = 'Se voce errar, as suas chances ira reduzir', anchor='center', font=('Ivy 8 bold'), bg=fundo, fg=co1)
l_regra_3.place(x=40, y=140)

b_jogar = Button (frame_corpo,command=iniciar_jogo, text = 'Jogar', width=17, font=('Ivy 10 bold'), bg=co10, fg=co0,relief=RAISED, overrelief=RIDGE)
b_jogar.place(x=40, y=170)


janela.mainloop()
