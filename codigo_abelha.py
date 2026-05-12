import qrcode
import os
from PIL import Image, ImageDraw
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import CircleModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask

def criar_logo_abelha(caminho="bee_logo.png"):
    # Cria uma imagem com fundo transparente (100x100)
    img = Image.new("RGBA", (150, 150), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # Fundo branco em formato circular para destacar a abelha no QR Code
    draw.ellipse((5, 5, 145, 145), fill="white")

    # Corpo da abelha (amarelo)
    draw.ellipse((30, 50, 120, 100), fill="gold", outline="black", width=3)
    
    # Listras da abelha
    draw.line((60, 52, 60, 98), fill="black", width=8)
    draw.line((90, 52, 90, 98), fill="black", width=8)
    
    # Olho da abelha
    draw.ellipse((105, 65, 112, 75), fill="black")
    
    # Asas da abelha
    draw.ellipse((45, 20, 75, 60), fill="lightblue", outline="black", width=2)
    draw.ellipse((65, 20, 95, 60), fill="lightblue", outline="black", width=2)
    
    # Ferrão da abelha
    draw.polygon([(32, 70), (32, 80), (10, 75)], fill="black")
    
    img.save(caminho)
    return caminho

# Dados para os QR Codes
abelhas = {
    "Melipona-quadrifasciata": "https://drive.google.com/file/d/1aa5IHKGt1PEg4YVH_7yW4n9aDaniZ9LG/view?usp=sharing",
    "Plebeia-droryana": "https://drive.google.com/file/d/1tTNZnOPQoJZl9IzNUBcQTd_XjI5yBlxp/view?usp=sharing",
    "Tetragonisca-angustula": "https://drive.google.com/file/d/1QnqNtoUUI_HZJzw_cVFQKByvQVe8-ihH/view?usp=sharing"
}

# Pasta de saída
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Gera o logo da abelha
logo_path = criar_logo_abelha()

for nome, link in abelhas.items():
    qr = qrcode.QRCode(
        version=5, # Aumentei a versão para o QR Code ter mais espaço para a imagem central
        error_correction=qrcode.constants.ERROR_CORRECT_H, # Nível alto de correção de erro é essencial aqui
        box_size=15,
        border=3,
    )
    qr.add_data(link)
    qr.make(fit=True)

    # Gerando o QR Code com a abelhinha no centro
    img = qr.make_image(
        image_factory=StyledPilImage,
        module_drawer=CircleModuleDrawer(),
        color_mask=SolidFillColorMask(
            back_color=(255, 255, 255), 
            front_color=(200, 120, 0), # Laranja/Marrom (cor de mel) sólido
        ),
        embeded_image_path=logo_path # Inserindo a imagem no centro!
    )
    
    caminho_arquivo = os.path.join(output_dir, f"qrcode_abelha_{nome}.png")
    img.save(caminho_arquivo)
    print(f"QR Code com logo gerado para {nome}: {caminho_arquivo}")

print("\nTodos os QR Codes com a abelhinha no centro foram criados!")
