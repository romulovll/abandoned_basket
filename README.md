# abandoned_basket

Desafio proposto para vaga de engenheiro de dados.


## Ambiente

Para a execução do teste pode-se utilizar dessas configurações ou executar no google colab (https://colab.research.google.com/),
no qual tem todo ambiente configurado para executar o teste, ou pode executar localmente. 

Para testar em uma máquina local, é necessário utilizar as seguintes configurações:
*	Versão do Python 2.7.15
*	apache-beam 2.13.0
## Arquivos
* **abandoned-basket-only-python.py** (Apresenta do desafio sem implementar utilizar o apache beam)
* **abandoned-basket-trying-use-pipeline.py** (Neste arquivo é apresentado como seria a estrutura se 
conseguisse implementar utilizando o apache beam )
* **input** (Nesse diretório está o arquivo no qual contém uma arquivo com a extensão (.json))
* **output** (Nesse diretório está o arquivo de saída, conforme o teste solicita.)
## Abordagem do desafio

Dado que foi meu primeiro contato com a tecnologia apache beam, foi necessário realizar 
um estudo exploratório, com intuito de conhecer o processo de criação e execução de um pipeline. 

1. O arquivo será executado localmente, por esse motivo é utilizado o DirectRunner

2. Criar as configurações do pipeline, como os parâmetros de entrada e de saída.

3. Execução dos dados armazenados nas Colections e tratado nos PCtransform.
