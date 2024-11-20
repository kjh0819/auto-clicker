import os
os.system("pip install pyautogui")
os.system("pip install opencv-python")
os.system("pip install pillow")
import pyautogui
import time

print(os.getcwd())

# Image file paths
launcher_download_path = "LauncherDownload1.png"
LDP2= "LauncherDownload2.png"
website_download_path = "download_website1.PNG"
WDP2="download_website2.png"
threshold = 0.9

while True:
    try:
        print("Checking for Launcher Download Button")
        launcher_location = pyautogui.locateOnScreen(launcher_download_path, confidence=threshold)

        if launcher_location is not None:
            # Click on the launcher download button if found
            pyautogui.click(launcher_location.left + 5, launcher_location.top + 5)

        time.sleep(3)  # Introduce a delay before taking the screenshot

    except pyautogui.ImageNotFoundException:
        try:
            print("Checking for Secondary Launcher Download Button")
            launcher_location = pyautogui.locateOnScreen(LDP2, confidence=threshold)

            if launcher_location is not None:
                # Click on the secondary launcher download button if found
                pyautogui.click(launcher_location.left + 10, launcher_location.top + 10)

            time.sleep(3)  # Introduce a delay before taking the screenshot

        except pyautogui.ImageNotFoundException::
            print("Secondary image not found. Waiting for the element to appear.")
            

    try:
        print("Checking for Website Download Button")
        website_location = pyautogui.locateOnScreen(website_download_path, confidence=threshold)

        if website_location is not None:
            # Click on the website download button if found
            pyautogui.click(website_location.left + 5, website_location.top + 5)

        time.sleep(3)
        print("Waiting for 5 seconds...")

    except pyautogui.ImageNotFoundException:
        try:
            print("Checking for Secondary Launcher Download Button")
            launcher_location = pyautogui.locateOnScreen(WDP2, confidence=threshold)

            if launcher_location is not None:
                # Click on the secondary launcher download button if found
                pyautogui.click(launcher_location.left + 5, launcher_location.top + 5)

            time.sleep(3)  # Introduce a delay before taking the screenshot

        except pyautogui.ImageNotFoundException:
            print("Secondary image not found. Waiting for the element to appear.")
