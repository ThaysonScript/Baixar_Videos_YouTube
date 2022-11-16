from pytube import YouTube
import Mp3
from time import sleep

print('Bem vindo ao YouTube Downloader!\n')
sleep(1)
yt = str(input('Digite o Link do video que deseja baixar: '))

escolha = str(input('Digite se quer "Video" ou "Musica": '))

while True:
    if escolha == 'Musica':
        escolha = Mp3.Musica(yt)
        break
    elif escolha == 'Video':
        escolha = Mp3.Video(yt)
        break
    else:
        print('Erro! Digite somente "Video" ou "Musica"')

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

    print(f'Obetendo informacoes dos titulos do video: {escolha.title}')

    sleep(1.5)

    print('Baixando...')
    escolha.download()
    print('Video baixado com sucesso!')

    break

sleep(1)
print('Finalizando Programa...')
