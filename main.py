from ultralytics import YOLO
import cv2
import face_recognition
import os
import numpy as np

model = YOLO("yolov8n.pt") 
known_face_encodings = []
known_face_names = []

known_folder = "known_faces/Hariharan"
for file in os.listdir(known_folder):
    path = f"{known_folder}/{file}"
    
    img = face_recognition.load_image_file(path)
    enc = face_recognition.face_encodings(img)
    
    if len(enc) > 0:  
        known_face_encodings.append(enc[0])
        known_face_names.append("Hariharan")   

print("Loaded Images:", len(known_face_encodings))


cap = cv2.VideoCapture(0)
cv2.namedWindow("Real-Time Face Authorization", cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty("Real-Time Face Authorization", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)




while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(frame, conf=0.3)[0]

    for box in results.boxes:
        cls = int(box.cls[0])
        label = model.names[cls]

        if label == "person":  
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            face = frame[y1:y2, x1:x2]
            rgb = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
            encodings = face_recognition.face_encodings(rgb)

            name = "Unauthorized Person"

            if len(encodings) > 0:
                face_enc = encodings[0]

                matches = face_recognition.compare_faces(known_face_encodings, face_enc)
                dist = face_recognition.face_distance(known_face_encodings, face_enc)

                if True in matches:
                    best_match = np.argmin(dist)
                    name = known_face_names[best_match]

            color = (0,255,0) if name != "Unauthorized Person" else (0,0,255)

            cv2.rectangle(frame, (x1,y1), (x2,y2), color, 2)
            cv2.putText(frame, name, (x1, y1-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

    cv2.imshow("Real-Time Face Authorization", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
