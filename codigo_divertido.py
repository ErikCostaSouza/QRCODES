import qrcode
import os
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import CircleModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask

# Dados para os QR Codes
abelhas = {
    "Melipona-quadrifasciata": "https://drive.google.com/file/d/1aa5IHKGt1PEg4YVH_7yW4n9aDaniZ9LG/view?usp=sharing",
    "Plebeia-droryana": "https://drive.google.com/file/d/1tTNZnOPQoJZl9IzNUBcQTd_XjI5yBlxp/view?usp=sharing",
    "Tetragonisca-angustula": "https://drive.google.com/file/d/1QnqNtoUUI_HZJzw_cVFQKByvQVe8-ihH/view?usp=sharing"
}

# Pasta de saída
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

for nome, link in abelhas.items():
    # Cria a instância do QRCode com mais redundância para suportar estilização pesada
    qr = qrcode.QRCode(
        version=3,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=15,
        border=3,
    )
    qr.add_data(link)
    qr.make(fit=True)

    # Gerando um QR Code Diferentão (Bolinhas com Gradiente Laranja/Marrom que lembra mel)
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=CircleModuleDrawer(),
        color_mask=RadialGradiantColorMask(
            back_color=(255, 255, 255), # Fundo Branco
            center_color=(255, 170, 0), # Laranja Mel no centro
            edge_color=(100, 50, 0)     # Marrom nas bordas
        )
    )
    
    # Salvar a imagem com prefixo divertido
    caminho_arquivo = os.path.join(output_dir, f"qrcode_divertido_{nome}.png")
    img.save(caminho_arquivo)
    print(f"QR Code divertido para {nome} gerado com sucesso em: {caminho_arquivo}")

print("\nTodos os QR Codes diferentões foram criados na pasta output!")
