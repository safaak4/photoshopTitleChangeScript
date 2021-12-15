
name_list = [

"Abdulkadir Taşkın",
"Abdullah Varıcı",
"Ferhat Korul",
"Lütfü Evren",
"Mehmet Akif Akkaya",
"Oğuzhan Yılmaz",
"Metehan Kılıç",
"Muhammed Çelik",
"Suphi Boyacı",
"Ubeydullah Yaşar",
"Furkan Özbek",
"Mehmet Fatih Dener",
"Şehmus Saygın",
"Ahmed Eymen Çimen",
"Ahmet Kerem Hızlı",
"Cemal Çetin",
"İbrahim Ersin",
"İlyas Koçyiğit",
"Muhammed Ali Köse",
"Muhammed Mustafa Karlı",
"Yakup Bozkurt",
"Abdullah Sağlam",
"Emin Yiğit Sezer",
"Emir Taha Altaş",
"Enes Beyler",
"Enes Karabulut",
"Furkan Çoban",
"İbrahim Olgun",
"İsmail Aktaş",
"Muhammed Berk Erman",
"Ömer Faruk İşcan",
"Yusuf Ahmet Kahraman",
"Ahmet Kaan Aydoğan",
"Ahmet Taha Elmas",
"Ahmet Yasin Kaymaz",
"Cemil Sefa Kaplan",
"Furkan Küçükarslan",
"Melih Taha Demiryürek",
"Muhammet Ali Gümüşoğlu",
"Enes Bushi",
"Yusuf Mert",
"Enes Erol",
"Ahmet Selim Özsoy",
"Halil Kerem Çorak",
"Muhammed Emin Soy",
"Mehmet Akif Mısırlı",
"M.Mansur Kurt",
"M.Eymen Yaman",
"Muhammed Eren Pola",
"Ömer Burak Tekin",
"Muhammed Emin Özkahraman",
"Furkan İmret",
"Ahmet Efe Gündoğdu",
"Ubeydullah Bilal Tuğtekin",
"Osman Efe Kaleli",
"Affan Duran",
"Muhammet Emin Yolcu",
"Muhammed Ali Öztürk",
"Ammar Emin Topal",
"Tarık Avcılar",
"Muhammed Ali hançer",
"Mustafa Berk Canbaz"

]


import win32com.client
import os

psApp = win32com.client.Dispatch("Photoshop.Application")
psApp.Open(r"C:\Users\cumas\Desktop\beyaz25.psd")

doc = psApp.Application.ActiveDocument

layer_name = doc.ArtLayers["namelayer"]

i = 0

#while i < len(name_list):
while i < 4:

    text_of_layer = layer_name.TextItem
    text_of_layer.contents = name_list[i]

    options = win32com.client.Dispatch('Photoshop.ExportOptionsSaveForWeb')
    options.Format = 6  # JPEG
    options.Quality = 100  # Value from 0-100

    jpgFile = r"C:\Users\cumas\Desktop\davetiye\%s"%(str(name_list[i]) + ".jpeg")

    doc.Export(ExportIn=jpgFile, ExportAs=2, Options=options)

    i = i + 1