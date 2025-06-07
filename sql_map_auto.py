import subprocess
import os
from datetime import datetime

def run_sqlmap_with_burp_request(request_file_path):
    output_dir = f"results_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
    os.makedirs(output_dir, exist_ok=True)
    screenshot_path = os.path.join(output_dir, "screenshot.png")

    command = [
        "sqlmap",
        "-r", request_file_path,
        "--batch",
        "--output-dir", output_dir
    ]

    print(f"[+] Running: {' '.join(command)}\n")
    subprocess.run(command)

    try:
        import pyautogui
        screenshot = pyautogui.screenshot()
        screenshot.save(screenshot_path)
        print(f"[+] Screenshot saved to {screenshot_path}")
    except Exception as e:
        print(f"[-] Screenshot failed: {e}")

if __name__ == "__main__":
    request_file = input("📂 Enter path to BurpSuite request file (e.g. request.txt): ").strip()
    if os.path.exists(request_file):
        run_sqlmap_with_burp_request(request_file)
    else:
        print("[-] File not found.")
