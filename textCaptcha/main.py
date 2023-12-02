try:
    from PIL import Image
except ImportError:
    import Image

import cv2
import pytesseract


def apply_blur(image_path, blur_strength=5):
    # Load the image
    image = cv2.imread(image_path)

    # Apply Gaussian blur to the image
    blurred_image = cv2.GaussianBlur(image, (blur_strength, blur_strength), 0)

    # Save the blurred image (optional)
    cv2.imwrite('blurred_image.png', blurred_image)

    return blurred_image


def solve_captcha(image_path):
    # Preprocess the image
    blurred_image = apply_blur(image_path, 3)

    # Use pytesseract to perform OCR on the preprocessed image
    captcha_text = pytesseract.image_to_string(Image.fromarray(blurred_image))

    print(captcha_text)
    return captcha_text


if __name__ == "__main__":
    # Specify the path to your captcha image
    captcha_image_path = '/home/codertjay/PycharmProjects/Bot/textCaptcha/img_5.png'

    # Solve the captcha
    solve_captcha(captcha_image_path)

# Grayscale, Gaussian blur, Otsu's threshold
image = cv2.imread('img_5.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (3, 3), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Morph open to remove noise and invert image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
invert = 255 - opening

# Perform text extraction
invert_data = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')
print("Invert ", invert_data)
thresh_data = pytesseract.image_to_string(thresh, lang='eng', config='--psm 6')
print("thresh_data ", thresh_data)
opening_data = pytesseract.image_to_string(opening, lang='eng', config='--psm 6')
print("opening_data ", opening_data)

cv2.imwrite('thresh.png', thresh)
cv2.imwrite('opening.png', opening)
cv2.imwrite('invert.png', invert)

import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

im = Image.open("img_5.png")  # the second one
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('temp.jpg')
text = pytesseract.image_to_string(Image.open('temp.jpg'))
print("enchancer ", text)

"""
pip install opencv-python
sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
"""
