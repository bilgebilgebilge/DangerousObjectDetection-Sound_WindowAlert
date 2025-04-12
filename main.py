"""
Dangerous Object Detection
This application uses YOLOv8 to detect defined objects such as scissors, knives in real-time camera image,
plays alert sound and displays window alert.
"""


import cv2
from ultralytics import YOLO
from gtts import gTTS
import os
import pygame
import tkinter as tk
from tkinter import messagebox

# Pygame'i başlat
pygame.mixer.init()

# YOLO modelini yükle
model = YOLO("yolov8m.pt")

# Türkçe nesne isimleri
coco_labels_tr = {
    "person": "insan", "backpack": "Sırt Çantası", "handbag": "El Çantası", 
    "tie": "Kravat", "suitcase": "Valiz", "bottle": "Şişe", "cell phone": "Cep Telefonu",
    "laptop": "Dizüstü Bilgisayar", "clock": "Saat", "book": "Kitap", "scissors": "Makas",
    "knife": "Bıçak", "gun": "Silah", "pen": "Kalem", "eraser": "Silgi", "sharpener": "Kalemtıraş",
    "watch": "Kol Saati", "glasses": "Gözlük", "umbrella": "Şemsiye", "mouse": "Bilgisayar Faresi",
    "keyboard": "Klavye", "headphones": "Kulaklık", "wallet": "Cüzdan", "ring": "Yüzük",
    "bracelet": "Bileklik", "necklace": "Kolye", "earrings": "Küpe", "belt": "Kemer",
    "marker": "İşaretleyici", "pencil": "Kurşun Kalem", "pen": "Tükenmez Kalem", 
    "highlighter": "Sarı Kalem", "paper": "Kağıt", "notebook": "Defter", "stapler": "Zımba",
    "tape": "Bant", "folder": "Dosya", "ruler": "Cetvel", "calculator": "Hesap Makinesi",
    "glue": "Yapıştırıcı", "chalk": "Tebeşir"
}

# Tehlikeli nesneler
dangerous_objects = ["Bıçak", "Makas", "Çakı", "Silah", "Biber Gazı"] 

# Uyarı penceresini oluştur
def show_alert(message):
    root = tk.Tk()
    root.withdraw()
    messagebox.showwarning("Dikkat!", message)
    root.quit()

# Sesli uyarıyı çal ve dosya silme hatasını önle
def play_warning_sound():
    warning_file = "warning.mp3"
    if not os.path.exists(warning_file):
        tts = gTTS("Dikkat! Tehlikeli bir nesne tespit edildi.", lang='tr')
        tts.save(warning_file)
    pygame.mixer.music.load(warning_file)
    pygame.mixer.music.play()

# Ses durdurma
def stop_warning_sound():
    pygame.mixer.music.stop()

# Kamerayı aç ve tehlikeli nesneleri tespit et
def detect_dangerous_objects():
    cap = cv2.VideoCapture(0)
    object_detected = False

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # YOLO modelini çalıştır
        results = model(frame)

        current_danger_detected = False

        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = box.conf[0].item()
                cls = int(box.cls[0].item())

                # Güven skoru eşik değerini düşürdük (%40)
                if conf < 0.4:
                    continue

                class_names = model.names
                label = class_names.get(cls, "Bilinmeyen")
                label_tr = coco_labels_tr.get(label, label)

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, f'{label_tr} ({conf:.2f})', (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

                # Tehlikeli nesne kontrolü
                if label_tr in dangerous_objects:
                    current_danger_detected = True
                    if not object_detected:
                        play_warning_sound()
                        show_alert(f"Dikkat! {label_tr} tespit edildi.")
                        object_detected = True

        if not current_danger_detected and object_detected:
            stop_warning_sound()
            object_detected = False

        cv2.imshow("Nesne Tespiti", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Programın ana işleyişi
if __name__ == "__main__":
    detect_dangerous_objects()
