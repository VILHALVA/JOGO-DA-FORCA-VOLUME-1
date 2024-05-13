# JOGO DA FORCA - VOLUME 1
👨‍💻ESSE É PEQUENO JOGO QUE RODA NO CONSOLE DA IDE.

<img src="FOTO.png" align="center" width="400"> <br>

## DESCRIÇÃO:
Este programa implementa um jogo simples de forca em Python. Ele seleciona aleatoriamente uma palavra de um arquivo chamado "WORD.txt" localizado no mesmo diretório do script, oculta a palavra, e permite que o usuário adivinhe as letras. O jogo fornece feedback sobre as letras corretas e incorretas, exibe o progresso da palavra oculta e termina quando o jogador adivinha corretamente a palavra ou excede o número máximo de tentativas (6 chances). O programa inclui também uma opção de "hack" que revela a palavra secreta, útil para depuração.

## EXECUTANDO O JOGO:
1. Certifique-se de ter um arquivo chamado `WORD.txt` no mesmo diretório que este arquivo Python.
2. No arquivo `WORD.txt`, insira uma palavra em cada linha. Essas palavras serão escolhidas aleatoriamente para o jogo.
3. Execute o arquivo Python.
4. O jogo começará, exibindo uma série de traços representando as letras da palavra secreta.
5. Você tem 6 chances para adivinhar a palavra secreta, digitando uma letra de cada vez.
6. Se você adivinhar corretamente todas as letras da palavra, você vence. Se não, o jogo termina e revela a palavra secreta.

## SOBRE O EXECUTAVEL:
### 1. EXECUTANDO:
    - Este arquivo executável está disponível apenas para `Windows X64`. Para executá-lo, basta dar dois cliques. O executável é bastante útil caso o Python não esteja instalado. Trata-se da mesma aplicação do arquivo `CODIGO.py`. Se desejar, você pode recompilá-lo novamente; é para isso que forneci o arquivo `imagem.ico`.

### 2. GERANDO:
   **1. Instalação do [PyInstaller:](https://pyinstaller.org/en/stable/)**
   - Certifique-se de ter o PyInstaller instalado. Se não tiver, instale usando o comando abaixo:
   ```bash
   pip install pyinstaller
   ```

   **2. Gerando o Executável:**
   - Para gerar o executável, utilize o comando `pyinstaller` seguido de opções:
      - `--icon="imagem.ico"`: Especifica o ícone do executável.
      - `-F`: Gera um único arquivo executável em vez de vários.
      - `CODIGO.py`: Substitua "CODIGO.py" pelo nome do seu arquivo Python principal.
   ```bash
   pyinstaller --icon="imagem.ico" -F CODIGO.py
   ```

## NÃO SABE?
- Entendemos que para manipular arquivos em muitas linguagens e tecnologias, é necessário possuir conhecimento nessas áreas. Para auxiliar nesse aprendizado, oferecemos cursos gratuitos disponíveis:
* [CURSO DE PYTHON](https://github.com/VILHALVA/CURSO-DE-PYTHON)
* [CONFIRA MAIS CURSOS](https://github.com/VILHALVA?tab=repositories&q=+topic:CURSO)

## CREDITOS:
- [PROJETO CRIADO PELO VILHALVA](https://github.com/VILHALVA)
