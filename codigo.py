import qrcode
import os

# Dados para os QR Codes
abelhas = {
    "Melipona-quadrifasciata": "https://drive.google.com/file/d/1aa5IHKGt1PEg4YVH_7yW4n9aDaniZ9LG/view?usp=sharing",
    "Plebeia-droryana": "https://drive.google.com/file/d/1tTNZnOPQoJZl9IzNUBcQTd_XjI5yBlxp/view?usp=sharing",
    "Tetragonisca-angustula": "https://drive.google.com/file/d/1QnqNtoUUI_HZJzw_cVFQKByvQVe8-ihH/view?usp=sharing"
}

# Pasta de saída
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Geração dos QR Codes
for nome, link in abelhas.items():
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    # Salvar a imagem
    caminho_arquivo = os.path.join(output_dir, f"qrcode_{nome}.png")
    img.save(caminho_arquivo)
    print(f"QR Code para {nome} gerado com sucesso em: {caminho_arquivo}")

print("Todos os QR Codes foram gerados!")
##