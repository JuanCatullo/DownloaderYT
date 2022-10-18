import pytube

print ("BIENVENIDO AL SISTEMA DE DESCARGA")
print("----------------------------------")

input ("Inserte la URL completa de YT: ")
yt = pytube.Youtube(url)

def descarga():
    print("Elija la opcion deseada:")
    print ("1 - Video alta definicion")
    print("2 - Video baja definicion")
    print("3 - Solo audio MP3")
    opt = input ("Opcion: ")

    if (opt=="1"):
        print("DESCARGANDO... Aguarde un momento")
        videoHD = yt.streams.get_highest_resolution()
        videoHD.Download(filename="VideoAltaDefinicion.mp4")
    elif (opt=="2"):
        print("DESCARGANDO... Aguarde un momento")
        videoLOW = yt.streams.get_lowest_resolution()
        videoLOW.Download(filename="VideoBajaDefinicion.mp4")
    elif (opt=="3"):
         print("DESCARGANDO... Aguarde un momento")
         audio = yt.streams.get_audio_only()
         audio.Download(filename="audio.mp3")
    else:
        print("Opcion no valida")
        print("----------------")

        descarga()
        print("descarga finalizada")