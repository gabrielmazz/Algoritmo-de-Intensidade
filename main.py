import argparse
from rich.console import Console
from rich.progress import Progress
import Intensidade.Intensidade as intens
import Utils.utils_imagem as ut_img
import Utils.utils_code as ut_code
import time
import Utils.library_checker as lib_checker

# Variáveis para passagem de argumentos via terminal
parser = argparse.ArgumentParser()

# Argumento para salvar a imagem na pasta de resultados
SAVE = parser.add_argument('--save', action='store_true', help='Salvar a imagem na pasta de resultados')
INFO = parser.add_argument('--info', action='store_true', help='Exibir o tempo de execução')
URL_IMAGE = parser.add_argument('--url', type=str, help='URL da imagem para usar no algoritmo')

def intensidade(imagem_escolhida, tipo):
    
    # Inicializa o tempo de execução
    start_time = time.time()
    
    with Progress() as progress:
        
        # Atualiza o progresso
        task = progress.add_task("[cyan]Processando...", total=3)
        
        time.sleep(1)
        
        # Leitura da imagem
        progress.update(task, advance=1, description='[cyan]Lendo a imagem...')
        Imagem_Original = ut_img.leitura_Imagem('./imagens/{}'.format(imagem_escolhida))    

        time.sleep(1)

        # Segmentação da imagem
        progress.update(task, advance=1, description='[cyan]Segmentando a imagem...')
        imagem_intensidade = intens.segment_image(Imagem_Original)
       
        time.sleep(1)
       
        # Realiza a plotagem das imagens
        progress.update(task, advance=1, description='[cyan]Plotando as imagens...')
        ut_img.plotagem_imagem(Imagem_Original, imagem_intensidade)
       
    end_time = time.time() - start_time - 3
    
    # Salva a imagem na pasta de resultados
    if args.save:
        ut_img.salvar_imagem(imagem_intensidade, './Resultados/Imagem_Intensidade_{}'.format(imagem_escolhida))
        
    if args.info:
        ut_code.print_infos(end_time, tipo, imagem_escolhida)
        
    if args.url:
        ut_img.deletar_imagem(imagem_escolhida)
     
if __name__ == '__main__':
    
    # Verifica se os argumentos foram passados corretamente
    args = parser.parse_args()
    
    # Verifica se as bibliotecas necessárias estão instaladas
    lib_checker.check_library()
    
    ut_code.clear_terminal()
    ut_code.print_title()
    
    if args.url:
        ut_img.download_imagem(args)
    
    # Inicializa a console
    console = Console()
    
    # Lista as imagens disponíveis na pasta
    imagens_disponiveis = ut_img.lista_imagens_pasta('./imagens', console)
    
    # Escolhe uma imagem para aplicar o método de Otsu
    imagem_escolhida = ut_img.escolher_imagens(imagens_disponiveis, console)
        
    intensidade(imagem_escolhida, 'Intensidade')