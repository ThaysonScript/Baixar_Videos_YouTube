# Importando o pacote Pytube
from pytube import YouTube
# Importando o pacote Time para esperar tarefas
from time import sleep

# Boas vindas!
print('Bem vindo ao YouTube Downloader!\n')
sleep(1)
yt = str(input('Digite o Link do video que deseja baixar: '))

# Lista acumulador esta desativada!
acumulador = []
acumulador.append(yt)

# Guarda a url propria do youtube a fim de ser verificada algum erro depois.
lista = []
lista.append(yt[:17])
validar = ['https://youtu.be/']

sleep(1)
print('Obtendo informacoes sobre o link!')
sleep(1)

while True:
    # Se a lista estiver com a url correta do youtube.
    if lista in validar:
        # Nao faca nada.
        pass
        # Se a url estiver errada faca o usuario digitar a url correta.
        if lista not in validar:
            print(f'Por favor! Digite o link correto (comece com "https://youtu.be/")')
            yt = str(input('Digite novamente o Link do video que deseja baixar: '))
    
    sleep(1)
    print('Preparando para baixar os seus videos...')

    # Criando variavel e atribuindo um objeto a uma variavel a qual e o link do video do youtube.
    youtube = YouTube(yt)
                                                        # Obtendo o texto do video.
    print(f'Obetendo informacoes dos titulos do video: {youtube.title}')

    sleep(1.5)

    print('Baixando...')
    # Variavel = variavel.configuracoesVideo(TipoExtensaoVideo).PegueTipoResolucao(18 para 360p e 22 para 720p)
    baixe_video = youtube.streams.filter(file_extension='mp4').get_by_itag(18)
    # Variavel.BaixeVideo
    baixe_video.download()
    print('Video baixado com sucesso!')

    # Querer baixar outro video novamente
    saida = str(input('Deseja continuar a baixar videos? [S/N] '))
    if saida in 'Ss':
        continue
    elif saida in 'Nn':
        break
    else:
        print('Erro! Digite somente [S/N]')
sleep(1)
print('Finalizando Programa...')

# O Download sera arquivado na pasta onde esta o codigo!
