import requests
import base64
import json
import os
import cv2
import numpy as np

# Configuration
API_URL = "https://inf3995.share.zrok.io/api"
API_KEY = "dev_key_123"
HEADERS = {
    "x-api-key": API_KEY,
    "Content-Type": "application/json"
}

# Image paths (Update these to your local paths)
IMAGE_PATH = "images/test_image.png"
CROP_PATH = "images/crop.png"


def encode_image(path):
    """Helper to encode image to base64 string."""
    try:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode('utf-8')
    except FileNotFoundError:
        print(f"Error: File {path} not found.")
        return None

def draw_boxes(image_path, objects, output_path):
    """Draw bounding boxes and labels on the image and save it."""
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not load image {image_path} for drawing.")
        return

    for obj in objects:
        label = obj.get('label', 'unknown')
        conf = obj.get('confidence', 0.0)
        bbox = obj.get('bbox', [])

        if len(bbox) == 4:
            x1, y1, x2, y2 = [int(foo) for foo in bbox]
            
            # Draw rectangle
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # Draw label
            text = f"{label} {conf:.2f}"
            y = y1 - 10 if y1 - 10 > 10 else y1 + 10
            cv2.putText(img, text, (x1, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imwrite(output_path, img)
    print(f"Saved visualization to {output_path}")

def main():
    # ---------------------------------------------------------
    # 1. Object Detection (Simple)
    # ---------------------------------------------------------
    print("\n--- 1. Object Detection (Default conf=0.25) ---")
    img_b64 = encode_image(IMAGE_PATH)
    if img_b64:
        payload = {
            "image": img_b64
        }
        response = requests.post(f"{API_URL}/detect", headers=HEADERS, json=payload)
        data = response.json()
        print(f"Response: {data}")
        
        if 'objects' in data:
            draw_boxes(IMAGE_PATH, data['objects'], "detection_result_1.jpg")

        print("\n--- 1b. Object Detection (High Confidence conf=0.8) ---")
        payload_high_conf = {
            "image": img_b64,
            "conf": 0.7
        }
        response = requests.post(f"{API_URL}/detect", headers=HEADERS, json=payload_high_conf)
        data = response.json()
        print(f"Response: {data}")
        
        if 'objects' in data:
           draw_boxes(IMAGE_PATH, data['objects'], "detection_result_1b.jpg")

    # ---------------------------------------------------------
    # 2. Object Detection with Visual Prompt
    # ---------------------------------------------------------
    print("\n--- 2. Object Detection with Visual Prompt ---")
    crop_b64 = encode_image(CROP_PATH)
    if img_b64 and crop_b64:
        payload = {
            "image": img_b64,
            "visual_prompts": crop_b64,
            "conf": 0.02
        }
        response = requests.post(f"{API_URL}/detect", headers=HEADERS, json=payload)
        data = response.json()
        print(f"Response: {data}")

        if 'objects' in data:
           draw_boxes(IMAGE_PATH, data['objects'], "detection_result_2.jpg")

    # ---------------------------------------------------------
    # 3. Object Detection with Text Prompt
    # ---------------------------------------------------------
    print("\n--- 3. Object Detection with Text Prompt ---")
    if img_b64:
        payload = {
            "image": img_b64,
            # "text_prompts": ["goal", "shoes"], # These were for soccer image?
            "text_prompts": ["chair", "lamp"],
            "conf": 0.05
        }
        response = requests.post(f"{API_URL}/detect", headers=HEADERS, json=payload)
        data = response.json()
        print(f"Response: {data}")

        if 'objects' in data:
           draw_boxes(IMAGE_PATH, data['objects'], "detection_result_3.jpg")

    # ---------------------------------------------------------
    # 4. Chat with LLM
    # ---------------------------------------------------------
    print("\n--- 4. Chat with LLM ---")
    payload = {
        "prompt": "Hello world"
    }
    response = requests.post(f"{API_URL}/chat", headers=HEADERS, json=payload)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.json()}")

    # ---------------------------------------------------------
    # 5. Chat with LLM + Image (VLM)
    # ---------------------------------------------------------
    print("\n--- 5. Chat with LLM + Image (VLM) ---")
    if img_b64:
        payload = {
            "prompt": "Describe this image",
            "image": img_b64
        }
        response = requests.post(f"{API_URL}/chat", headers=HEADERS, json=payload)
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")

if __name__ == "__main__":
    # Ensure images directory exists or comment out if using own paths
    if not os.path.exists(IMAGE_PATH):
        print("Note: Images not found. Please verify file paths.")
    
    main()
