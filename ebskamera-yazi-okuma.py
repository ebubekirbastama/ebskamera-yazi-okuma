import cv2
import pytesseract

# Tesseract'ın kurulu olduğu yolu ayarlayın
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Tesseract yolu

# Kamerayı başlat
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Görüntüyü gri tonlamaya çevir
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Görüntüyü bulanıklaştır (gürültüyü azaltmak için)
    blur_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

    # Görüntüyü ikili (binary) hale getir
    _, binary_frame = cv2.threshold(blur_frame, 150, 255, cv2.THRESH_BINARY)

    # Yazıyı tespit et (Türkçe dilini belirtiyoruz)
    custom_config = r'--oem 3 --psm 6 -l tur'  # OEM: OCR Engine Mode, PSM: Page Segmentation Mode
    text = pytesseract.image_to_string(binary_frame, config=custom_config)

    # Tespit edilen yazıyı konsola yazdır
    print("Tespit Edilen Yazı:", text)

    # Sonucu ekranda göster
    cv2.imshow('Yazı Algılama', binary_frame)

    # 'q' tuşuna basarak çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakları serbest bırak
cap.release()
cv2.destroyAllWindows()
