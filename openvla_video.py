from transformers import AutoModelForVision2Seq, AutoProcessor
from PIL import Image
import torch
import cv2
import numpy as np

print("Loading model and processor...")
processor = AutoProcessor.from_pretrained("openvla/openvla-7b", trust_remote_code=True)
vla = AutoModelForVision2Seq.from_pretrained(
    "openvla/openvla-7b",
    torch_dtype=torch.bfloat16,
    low_cpu_mem_usage=True,
    trust_remote_code=True
).to("cuda:0")
print("Model loaded successfully!")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("Cannot open webcam")

print("\nWebcam started. Press ENTER in the webcam window to process a frame.")
print("Press ESC in the webcam window to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Display the webcam feed. Press ENTER in this window to process, ESC to quit.
    # 웹캠 화면을 보여줍니다. 이 창에서 ENTER 키를 눌러 프레임을 처리하고, ESC 키를 눌러 종료하세요.
    cv2.imshow('Webcam - Press ENTER to process, ESC to quit', frame)

    key = cv2.waitKey(1) & 0xFF

    # If ESC is pressed, exit the loop.
    # ESC 키를 누르면 루프를 종료합니다.
    if key == 27:
        break

    # If ENTER is pressed, capture the frame and ask for user instruction.
    # ENTER 키를 누르면 현재 프레임을 캡처하고 사용자 명령을 요청합니다.
    if key == 13:
        print("\n----------------------------------------")
        print("Frame captured! Enter your instruction:")
        
        # Get user instruction from the terminal.
        # 터미널에서 사용자 명령을 입력받습니다.
        instruction = input("> ")

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(rgb_frame)

        prompt = f"In: What action should the robot take to {instruction}?\nOut:"

        inputs = processor(prompt, image).to("cuda:0", dtype=torch.bfloat16)

        print("Predicting action...")
        action = vla.predict_action(**inputs, unnorm_key="bridge_orig", do_sample=False)

        print(f"\nPredicted Action: {action}")
        print("----------------------------------------")
        print("\nWebcam is running. Press ENTER to process a new frame or ESC to quit.")

cap.release()
cv2.destroyAllWindows()
print("Program finished.")