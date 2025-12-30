Here is a **simple README.md** written in plain text without technical overload.

# Real-Time Person Identification System

This project detects a person using a webcam.
If the person is trained and recognized, their name is shown.
If not recognized, it displays "Unauthorized Person".

The system uses YOLO for detecting people and Face Recognition for identifying who the person is.

## How it Works

1. The camera opens and captures video.
2. YOLO detects a person in the frame.
3. The face is taken and compared with stored face images.
4. If the face matches stored images, it displays the person's name.
5. If no match is found, it shows "Unauthorized Person".

---

## Folder Setup

```
project/
 ├── main.py
 └── known_faces/
      └── Hariharan/
          ├── Hariharan_1.jpg
          ├── Hariharan_2.jpg
          ├── ...
```

Place multiple images of the person inside:

```
known_faces/Hariharan/
```

More images = better accuracy.

---

## Install Requirements

```
pip install ultralytics opencv-python face_recognition numpy
```

---

## Run the Program

```
python main.py
```

Press `Q` to close the window.

---

## Output

- If the person is recognized → shows name in **green**
- If not recognized → shows **Unauthorized Person** in red

---

That's it.
This is a simple real-time person recognition project using Python.

---

If you want, I can also give:

- A short explanation version
- One-line summary
- Short project report format

Tell me what you want.
