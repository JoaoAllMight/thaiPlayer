import tkinter as tk
from tkinter import PhotoImage
from pygame import mixer
from PIL import Image, ImageTk

mixer.init()

#Função para tocar música 
def tocar_musica(caminho):
    mixer.music.load(caminho)
    mixer.music.play()

janela = tk.Tk()
janela.title("Meus Discos Favoritos")
janela.geometry("900x400")
janela.configure(bg="#202020")

discos = [
    {
        "banda": "Home Made Kazoku",
        "album": "Shounen Heart",
        "imagem": "shounen_heart.jpg",
        "musica": "shounen_heart.mp3"
    },
    {
        "banda": "Asian Kung-Fu Generation",
        "album": "Sol-fa",
        "imagem": "solfa.jpg",
        "musica": "rewrite.mp3"
    },
    {
        "banda": "Nico Touches the Walls",
        "album": "Who Are You?",
        "imagem": "who_are_you.jpg",
        "musica": "broken_youth.mp3"
    }
]

# --- Criação dos cards ---
for i, disco in enumerate(discos):
    frame = tk.Frame(janela, bg="#2c2c2c", bd=2, relief="ridge")
    frame.place(x=50 + i*280, y=40, width=250, height=320)

    # Capas dos discos
    img = Image.open(disco["imagem"])
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    lbl_img = tk.Label(frame, image=img_tk, bg="#2c2c2c")
    lbl_img.image = img_tk
    lbl_img.pack(pady=10)

    # Nome da banda e do álbum
    lbl_banda = tk.Label(frame, text=disco["banda"], fg="white", bg="#2c2c2c", font=("Arial", 11, "bold"))
    lbl_banda.pack()
    lbl_album = tk.Label(frame, text=disco["album"], fg="gray", bg="#2c2c2c", font=("Arial", 10))
    lbl_album.pack(pady=5)

    # Botão tocar
    btn = tk.Button(frame, text="▶ Tocar música", command=lambda m=disco["musica"]: tocar_musica(m))
    btn.pack(pady=10)

janela.mainloop()

