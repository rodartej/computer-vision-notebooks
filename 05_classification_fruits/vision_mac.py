import torch
from torchvision import models, transforms
from PIL import Image

# 1. Cargar el modelo (ResNet18)
model = models.resnet18(weights='DEFAULT')
model.eval()

# 2. Configurar el preprocesamiento
preprocess = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# 3. Diccionario manual de frutas (IDs estándar de ImageNet)
# Esto evita el error de JSON y funciona offline
frutas_dict = {
    948: "Manzana (Apple)",
    949: "Fresa (Strawberry)",
    950: "Naranja (Orange)",
    951: "Limón (Lemon)",
    952: "Higo (Fig)",
    953: "Piña (Pineapple)",
    954: "Plátano (Banana)",
    955: "Jackfruit",
    956: "Natilla (Custard Apple)",
    957: "Granada (Pomegranate)"
}

def identificar(ruta):
    try:
        img = Image.open(ruta).convert('RGB')
        batch = preprocess(img).unsqueeze(0)

        with torch.no_grad():
            output = model(batch)
        
        # Obtener el ID con mayor probabilidad
        probabilidades = torch.nn.functional.softmax(output[0], dim=0)
        idx = torch.argmax(probabilidades).item()
        
        # Buscar en nuestro diccionario o dar el ID general
        nombre = frutas_dict.get(idx, f"Objeto ID: {idx} (No es una fruta común)")
        confianza = probabilidades[idx].item() * 100

        print("-" * 30)
        print(f"RESULTADO: {nombre}")
        print(f"CONFIANZA: {confianza:.2f}%")
        print("-" * 30)
        
    except Exception as e:
        print(f"Error al procesar: {e}")

# Cambia esto por la ruta de tu foto
identificar("/Users/jesusrodarte/Documents/Escuela/CdD/CdD 6/Finanzas/Visión Computacional/naranja.jpg")
identificar("/Users/jesusrodarte/Documents/Escuela/CdD/CdD 6/Finanzas/Visión Computacional/manzana.jpg")
identificar("/Users/jesusrodarte/Documents/Escuela/CdD/CdD 6/Finanzas/Visión Computacional/fresa.jpg")