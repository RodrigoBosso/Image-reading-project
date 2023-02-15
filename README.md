# Image-reading-project
Projeto de leitura de imagens Esse projeto desenvolvido em python usa a biblioteca Open CV e a biblioteca Py teceract para construir um arquivo em texto que será convertido em áudio com ajuda do programa balabolka

Cuidados de uso:
•	O programa Tem 2 versões, a em Português e a em Inglês
•	Inicialmente o Usuário deve passar para as pastas "Imageseng" e "Imagenspor"
•	Removendo as imagens que não gostaria de fazer a conversão e colocando apenas as que ele deseja fazer (como por exemplo um livro)
•	O Usuário não pode ter arquivos de imagens que estejam escritos com caracteres especiais, ç ã ô ... no nomes das imagens, pois isso retornará erro no projeto, o erro também ocorre se o caminho que o projeto estiver armazenado tem esses caracteres especiais.
•	Tendo seguido as regras de Nomes e de caminhos, basta verificar se nas pastas de Áudio e de result. estão vazias, se não estiverem delete os arquivos anteriores, ou os mova se assim for de sua vontade.
•	Ambos as 2 versões dos arquivos dependem das pastas adjacentes. As pastas não devem ser apagadas ou renomeadas pois esse procedimento quebrará os códigos. Já se mover o projeto todo , deverá se atentar aos nomes dos caminhos apenas.
Após esses cuidados O programa pode ser rodado normalmente e já não deverá apresentar erros.
O programa faz uso de um outro programa conhecido como balabolka que será controlado através de uma biblioteca conhecida como PyAutoGui. 
