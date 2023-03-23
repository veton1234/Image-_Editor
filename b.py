from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QListWidget, QFileDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image
from PIL import ImageFilter
from PIL.ImageQt import ImageQt
from PIL import ImageFilter
from PIL.ImageFilter import (BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, SMOOTH, SMOOTH_MORE, SHARPEN, GaussianBlur, UnsharpMask) 

import os

app = QApplication([]) #krijojme aplikacionin
main = QWidget()
main.resize(700,500) #permasat e dritares
main.setWindowTitle('Veton')
im = QLabel('abc')
butoni = QPushButton('Folder') #butoni folder ku aksesohen folderat te MyPc
lista = QListWidget()

left = QPushButton('Left') #butonat left,right,bardh e zi,flip,sharp
right = QPushButton('Right')
bz = QPushButton('BZ')
mirror = QPushButton('Mirror')
sharp = QPushButton('Sharpness')

r1 = QHBoxLayout() #vendosja e butonave ne nje rresht
k1 = QVBoxLayout()
k2 = QVBoxLayout()
k1.addWidget(butoni)
k1.addWidget(lista)
k2.addWidget(im,95)

but = QHBoxLayout()
but.addWidget(left)
but.addWidget(right)
but.addWidget(mirror)
but.addWidget(sharp)
but.addWidget(bz)
k2.addLayout(but)
r1.addLayout(k1,20)
r1.addLayout(k2,80)
main.setLayout(r1)


direkt = '' #direktoria
def filter(doc, prp): 
    res = []
    for emri in doc:
        for ext in prp:
            if emri.endswith(ext):
                res.append(emri)
    return res

def zgjidh():
    global direkt
    direkt = QFileDialog.getExistingDirectory()

def listen():
    prp = ['.jpg','.png','.bmp','.gif','.jpeg'] #prapashtesat e emrave file-ve
    zgjidh()
    emrat = filter(os.listdir(direkt),prp)
    lista.clear()

    for emri in emrat:
        lista.addItem(emri)
butoni.clicked.connect(listen)  

class imazhi(): #klasa
    def __init__(self):
        self.image = None
        self.dir = None
        self.emri = None
        self.ruaj = "djaadj"

    def ngarko(self,dir,emri):   #funksioni qe ngarkon imazhin
        self.dir = dir
        self.emri = emri
        i_path = os.path.join(dir, emri)
        self.image = Image.open(i_path)    

    

    def b_z(self):   #funksini bardh e zi
        self.image = self.image.convert('L')
        self.ruaj_im()
        i_path = os.path.join(self.dir, self.ruaj,self.emri)
        self.shfaq(i_path)

    def left(self): #funksioni majtas
        self.image = self.image.transpose(Image.ROTATE_90)
        self.ruaj_im()
        i_path =  os.path.join(self.dir, self.ruaj,self.emri)
        self.shfaq(i_path)

    def right(self): #funksioni djathtas
        self.image = self.image.transpose(Image.ROTATE_270)
        self.ruaj_im()
        i_path =  os.path.join(self.dir, self.ruaj,self.emri)
        self.shfaq(i_path) 

    def flip(self): #funksioni flip
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.ruaj_im()
        i_path =  os.path.join(self.dir, self.ruaj,self.emri)
        self.shfaq(i_path)

    def sharp(self): #funksioni sharp
        self.image = self.image.filter(SHARPEN)
        self.ruaj_im()
        i_path =  os.path.join(self.dir, self.ruaj,self.emri)
        self.shfaq(i_path)


    def ruaj_im(self): #funksioni qe ruan imazhin
        path = os.path.join(self.dir, self.ruaj)
        if not(os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)
        i_path = os.path.join(path, self.emri)
        self.image.save(i_path)   

    def shfaq(self,path): #funskioni qe shfaq imazhin
        im.hide()
        pix = QPixmap(path) 
        w,h = im.width(),im.height()   
        pix = pix.scaled(w,h,Qt.KeepAspectRatio)
        im.setPixmap(pix)
        im.show()     

i_zgjedhur = imazhi()

def shfaq1():   #funksioni qe hap imazhin
    if lista.currentRow() >= 0:
        emri = lista.currentItem().text()
        i_zgjedhur.ngarko(direkt, emri)
        i_path = os.path.join(i_zgjedhur.dir, i_zgjedhur.emri)
        i_zgjedhur.shfaq(i_path)
lista.currentRowChanged.connect(shfaq1) #lidhja e butonave
bz.clicked.connect(i_zgjedhur.b_z)
left.clicked.connect(i_zgjedhur.left)
right.clicked.connect(i_zgjedhur.right)
mirror.clicked.connect(i_zgjedhur.flip)
sharp.clicked.connect(i_zgjedhur.sharp)











main.show()
app.exec()