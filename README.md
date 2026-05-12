# QR Codes para Abelhas 🐝

Este projeto foi criado para gerar QR Codes personalizados que apontam para arquivos em PDF contendo informações sobre diferentes espécies de abelhas nativas do pai do usuário.

## O Pedido Inicial

O objetivo inicial era criar um script em Python que gerasse três QR Codes simples, cada um apontando para um link do Google Drive correspondente a uma espécie de abelha específica:

1. **Melipona quadrifasciata** (Mandaçaia)
2. **Plebeia droryana** (Mirim Droryana)
3. **Tetragonisca angustula** (Jataí)

## O que Fizemos (Evolução do Projeto)

Ao longo do desenvolvimento, exploramos diferentes formas de estilizar os QR Codes para deixá-los mais temáticos e atrativos. O projeto foi dividido em três scripts principais, mostrando a evolução da ideia:

### 1. Script Básico (`codigo.py`)
Criamos o script inicial utilizando a biblioteca `qrcode`. Ele recebe os links e gera QR Codes tradicionais (quadrados em preto e branco). Esse código já estabeleceu a base de ler os dados e salvar as imagens na pasta `output/`.

### 2. Script Divertido com Gradiente (`codigo_divertido.py`)
Para sair "da caixa", criamos uma segunda versão. Utilizamos os módulos de estilização da biblioteca:
- Trocamos os quadrados por **círculos** (estilo "bolinhas").
- Aplicamos uma máscara de cor em **gradiente radial**, que começava com um laranja vivo no centro e escurecia para marrom nas bordas, lembrando a cor de mel.

### 3. Script Final Temático (`codigo_abelha.py`)
A versão definitiva! Fomos além e adicionamos um logo diretamente no centro do QR Code. 
- Utilizamos a biblioteca `Pillow` (PIL) para **desenhar programaticamente um ícone de abelhinha** do zero (com asas, listras e ferrão), salvo temporariamente como `bee_logo.png`.
- Inserimos essa abelhinha no centro de cada QR Code.
- A pedido do usuário, ajustamos as cores: mantivemos o formato de bolinhas, mas removemos o gradiente em favor de uma **cor sólida amarelo-alaranjada** (cor de mel), deixando o visual mais limpo, mas mantendo a temática perfeitamente.

## Estrutura do Repositório

- `codigo.py`: Script gerador de QR Codes padrão.
- `codigo_divertido.py`: Script gerador de QR Codes em bolinhas com gradiente.
- `codigo_abelha.py`: Script gerador de QR Codes em bolinhas, cor de mel sólida e com logo de abelha no centro.
- `output/`: Pasta onde todas as imagens PNG dos QR Codes gerados são salvas.
- `input/`: Arquivos PDF originais sobre as abelhas.

## Como Executar

Certifique-se de ter as bibliotecas instaladas:
```bash
pip install "qrcode[pil]" pillow
```

Para gerar os QR Codes finais (com a abelha no centro), rode:
```bash
python codigo_abelha.py
```
As imagens serão geradas na pasta `output/`.
