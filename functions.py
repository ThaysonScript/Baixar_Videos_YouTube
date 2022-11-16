from pytube import YouTube

def Musica(opt):
    resultado = YouTube(opt)
    return resultado.streams.filter(only_audio=True).get_by_itag(140)


def Video(opt):
    resultado = YouTube(opt)
    return resultado.streams.filter(file_extension='mp4').get_by_itag(18)
