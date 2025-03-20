from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def segment_image(image):
    
    # Converter para grayscale se necessário
    img = image.convert("L")
    img_array = np.array(img)

    # Aplicar segmentação de intensidade
    segmented_array = np.select(
        [
            (img_array >= 0) & (img_array <= 50),
            (img_array >= 51) & (img_array <= 100),
            (img_array >= 101) & (img_array <= 150),
            (img_array >= 151) & (img_array <= 200),
            (img_array >= 201) & (img_array <= 255),
        ],
        [25, 75, 125, 175, 255]
    )

    # Converter o array segmentado de volta para PIL Image
    segmented_img = Image.fromarray(segmented_array.astype(np.uint8))

    return segmented_img