
name_list = [

"Tom Araya",
"Jeff Hanneman",
"Kerry King",
"James Hetfield"

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
