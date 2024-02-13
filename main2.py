# Librarias ------------------------------------------------------------------------------------------------------
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import cv2
from PIL import Image, ImageTk
import os
# ---------------------------------------------------------------------------------------------------------------
# Variaveis de controlo -----------------------------------------------------------------------------------------
cap = None  # Variável global para a captura de vídeo
webcam_selected = None  # Variável global para a webcam selecionada
#----------------------------------------------------------------------------------------------------------------
# função Para iniciar a webcam ----------------------------------------------------------------------------------
def iniciar_webcam():
    global cap
    global webcam_selected
    if cap is None or not cap.isOpened():
        try:
            webcam_selected = Cmbweb.get()
            cap = cv2.VideoCapture(int(webcam_selected[-1]) - 1)
            if not cap.isOpened():
                messagebox.showerror("Erro", "Webcam não encontrada. Por favor, selecione outra.")
            else:
                messagebox.showinfo("Webcam", f"{webcam_selected} Iniciada com sucesso.")
                exibir_frame()
        except Exception as e:
            messagebox.showerror("Erro", "Ocorreu um erro ao acessar a webcam. Por favor, selecione outra.")
    else:
        messagebox.showinfo("Webcam", "A webcam já está em execução.")
#----------------------------------------------------------------------------------------------------------------
# criar a Função Sair -------------------------------------------------------------------------------------------
def sair():
    resposta = messagebox.askyesno("Sair", "Tem certeza que deseja sair? sim/nao")
    if resposta:
        parar_webcam()  # Parar a webcam antes de fechar
        Janela.destroy()   # Encerrar a aplicação
#---------------------------------------------------------------------------------------------------------------
# Adicione esta função para capturar o frame --------------------------------------------------------------------
def capturar_frame():
    global cap
    if cap is not None:
        ret, frame = cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frame = Image.fromarray(frame)
            # Diretório onde a imagem capturada será salva
            diretorio = os.path.join(os.path.expanduser("~"), "Pictures", "Minhas Imagens")
            # Certifique-se de que o diretório exista, caso contrário, crie-o
            if not os.path.exists(diretorio):
                os.makedirs(diretorio)
            # Caminho completo para salvar a imagem
            caminho_imagem = os.path.join(diretorio, "frame_capturado.png")
            frame.save(caminho_imagem)
            messagebox.showinfo("Captura de Frame", f"Frame capturado com sucesso.\nSalvo em: {caminho_imagem}")
#---------------------------------------------------------------------------------------------------------------
# função Para Selecionar a Webcam ------------------------------------------------------------------------------
def selecionar_webcam(event):
    global cap
    global webcam_selected
    try:
        webcam_selected = Cmbweb.get()
        cap = cv2.VideoCapture(int(webcam_selected[-1]) - 1)
        if not cap.isOpened():
            messagebox.showerror("Erro", "Webcam não encontrada. Por favor, selecione outra.")
        else:
            messagebox.showinfo("Webcam :", f"{webcam_selected} Selecionada Com Sucesso")
            exibir_frame()
    except Exception as e:
        messagebox.showerror("Erro", "Ocorreu um erro ao acessar a webcam. Por favor, selecione outra.")
#--------------------------------------------------------------------------------------------------------------
# funçao Para Exbir Frame -------------------------------------------------------------------------------------        
def exibir_frame():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = Image.fromarray(frame)
        frame.thumbnail((860, 310))  # Redimensiona para 600 pixels de largura e 400 de altura
        frame = ImageTk.PhotoImage(frame)
        Limagem.config(image=frame)
        Limagem.image = frame
        Limagem.after(10, exibir_frame)  # Atualiza o frame a cada 10 milissegundos
#--------------------------------------------------------------------------------------------
# função para parar webcam ------------------------------------------------------------------        
def parar_webcam():
    global cap
    if cap is not None:
        cap.release()
        Limagem.config(image=None)  # Limpa a exibição
        messagebox.showinfo("Webcam", "Captura de vídeo interrompida com sucesso.")
#--------------------------------------------------------------------------------------------
# selecionar as Cores a Usar ----------------------------------------------------------------
Co1='#ffffff' # cor Branco para a Janela 
co2='#e7e9e9' # cor Amarelo claro para os Botões
#--------------------------------------------------------------------------------------------
# configurar a Janela -----------------------------------------------------------------------
Janela = Tk()
Janela.geometry('600x430+100+100')
Janela.resizable(0,0)
Janela.title('Menu Webcam DevJoel2024 ©')
Janela.config(bg=Co1)
Janela.iconbitmap('C:\\Users\\HP\\Desktop\\Projectos\\webcam\\icon.ico')
#---------------------------------------------------------------------------------------------
# criar combobox para selecionar Camras ------------------------------------------------------
Cmbweb = Combobox (Janela, font=('arial 14'), width=50)
Cmbweb.place(x=10, y=10)
Cmbweb.set('Selecione a Webcam')
Cmbweb.bind("<<ComboboxSelected>>", selecionar_webcam)  
Cmbweb['values'] = ['Webcam 1', 'Webcam 2', 'Webcam 3']  
#----------------------------------------------------------------------------------------------
# cria o label onde ira ser apresentada a Imagem ----------------------------------------------
Limagem = Label(Janela, text='', bg='white')
Limagem.place(x=10, y=55)
#---------------------------------------------------------------------------------------------
# criar Os Botões ----------------------------------------------------------------------------
Bcapturar = Button(Janela, text='Capturar', font=('arial 18'), relief=RAISED, overrelief=RIDGE, command=capturar_frame, bg=co2)
Bcapturar.place(x=10, y=370)
Bparar = Button(Janela, text='Parar Webcam', font=('arial 18'), relief=RAISED, overrelief=RIDGE, command=parar_webcam, bg=co2)
Bparar.place(x=140, y=370)
BSair = Button(Janela, text='Fechar', font=('arial 18'), relief=RAISED, overrelief=RIDGE, bg=co2, command=sair)
BSair.place(x=450, y=370)
Biniciar = Button(Janela, text='iniciar', font=('arial 18'), relief=RAISED, overrelief=RIDGE, bg=co2, command=iniciar_webcam)
Biniciar.place(x=335, y=370)
#---------------------------------------------------------------------------------------------
# Aqui Vamos iniciar a Nossa janela ---------------------------------------------------------- 
Janela.mainloop()
#---------------------------------------------------------------------------------------------
