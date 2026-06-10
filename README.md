# Computer Vision Notebooks

> Notebooks de visión computacional clásica: procesamiento, detección de bordes (Canny), detección y conteo de objetos, intro a clasificación con redes.

[![Python](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.9-5C3EE8?logo=opencv&logoColor=white)](https://opencv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Índice

| # | Carpeta | Tema | Notebooks |
|---|---------|------|-----------|
| 01 | [`01_image_processing/`](01_image_processing/) | Carga, filtros, operaciones morfológicas | 3 |
| 02 | [`02_edge_detection/`](02_edge_detection/) | Canny implementado paso a paso + comparativa OpenCV | 2 |
| 03 | [`03_object_detection/`](03_object_detection/) | Conteo de objetos: piezas LEGO, triángulos, multi-objeto | 3 |
| 04 | [`04_classification_intro/`](04_classification_intro/) | Red neuronal + convolución desde cero | 3 |
| 05 | [`05_classification_fruits/`](05_classification_fruits/) | Clasificador fruta (manzana/naranja/fresa) por features visuales | 1 (Python) |

## Stack

- **Python 3.10+**
- **CV**: OpenCV, scikit-image, Pillow
- **ML**: scikit-learn
- **Análisis**: NumPy, SciPy
- **Visualización**: Matplotlib

## Setup

```bash
git clone https://github.com/rodartej/computer-vision-notebooks.git
cd computer-vision-notebooks

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

jupyter lab
```

## Estructura

```
computer-vision-notebooks/
├── README.md
├── requirements.txt
├── LICENSE
├── .gitignore
├── 01_image_processing/
├── 02_edge_detection/
├── 03_object_detection/
├── 04_classification_intro/
├── 05_classification_fruits/
│   └── vision_mac.py
└── assets/
    └── sample_images/        # imágenes de prueba versionadas
        ├── fresa.jpg
        ├── manzana.jpg
        └── naranja.jpg
```

## Highlights

**Canny desde cero** ([`02_edge_detection/algoritmo_canny.ipynb`](02_edge_detection/algoritmo_canny.ipynb))
Implementación paso a paso del algoritmo de Canny (gradiente Sobel → no-max suppression → doble umbral → histeresis) sin usar `cv2.Canny`, contrastado contra la implementación de OpenCV.

**Conteo de piezas LEGO** ([`03_object_detection/piezas_lego.ipynb`](03_object_detection/piezas_lego.ipynb))
Segmentación + conteo automático de piezas de LEGO usando umbrales adaptativos, contornos y filtros morfológicos.

**Clasificador de frutas** ([`05_classification_fruits/vision_mac.py`](05_classification_fruits/vision_mac.py))
Clasificación naive de manzana/naranja/fresa a partir de features de color HSV + textura. Imágenes de demo en `assets/sample_images/`.

## Contexto académico

Reorganizado de cursos **Reconocimiento de Patrones** y **Visión Computacional aplicada a Finanzas** — CdD 6 (2026).

## Licencia

MIT — ver [LICENSE](LICENSE).

## Autor

**Jesús Eduardo Rodarte Rosales**
[GitHub](https://github.com/rodartej) · [LinkedIn](https://www.linkedin.com/in/jesusrodarte/) · jesusrod254@gmail.com
