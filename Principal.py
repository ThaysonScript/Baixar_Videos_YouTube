from pytube import YouTube
from time import sleep

print('Bem vindo ao YouTube Downloader!\n')
sleep(1)
yt = str(input('Digite o Link do video que deseja baixar: '))
acumulador = []
acumulador.append(yt)
lista = []
lista.append(yt[:17])
validar = ['https://youtu.be/']

sleep(1)
print('Obtendo informacoes sobre o link!')
sleep(1)

while True:
    if lista in validar:
        pass
        if lista not in validar:
            print(f'Por favor! Digite o link correto (comece com "https://youtu.be/")')
            yt = str(input('Digite novamente o Link do video que deseja baixar: '))
    
    sleep(1)
    print('Preparando para baixar os seus videos...')

    youtube = YouTube(yt)

    print(f'Obetendo informacoes dos titulos do video: {youtube.title}')

    sleep(1.5)

    print('Baixando...')
    baixe_video = youtube.streams.filter(file_extension='mp4').get_by_itag(18)
    baixe_video.download()
    print('Video baixado com sucesso!')

    saida = str(input('Deseja continuar a baixar videos? [S/N] '))
    if saida in 'Ss':
        yt = str(input('Digite outro Link de video que deseja baixar: '))
        sleep(2)
        acumulador.append(yt)
    elif saida in 'Nn':
        break
    else:
        print('Erro! Digite somente [S/N]')
sleep(1)
print('Finalizando Programa...')
