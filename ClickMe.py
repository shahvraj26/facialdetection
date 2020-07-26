# Imports from the Beginning
import os
import time

# Some Prints Used Before Code Starts so User knows what to do
print("PLEASE READ THE README.docx BEFORE BEGINNING OR THIS CODE WILL NOT WORK")
print("--------------------------------------------------------")
time.sleep(3)
print("After reading README.docx THOROUGHLY just come back to this code.")
print("--------------------------------------------------------")
time.sleep(2)
print("Opening README.docx...")
# Opens README
os.system("start README.docx")
print("--------------------------------------------------------")
time.sleep(5)
print("Don't worry about clicking the ClickMe.py code again, it will automatically start again for you after 60 seconds, YOU JUST HAVE TO CLICK THIS ONCE.")
print("--------------------------------------------------------")
time.sleep(5)
print("WELCOME TO IMAGE FACIAL RECONITION WITH PYTHON OPENCV, THANK YOU FOR CHECKING IT OUT")
print("--------------------------------------------------------")
time.sleep(5)
print("MAKE SURE PYTHON AND PIP ARE INSTALLED ON YOUR COMPUTER")
print("--------------------------------------------------------")
time.sleep(5)

# Asking User to Install specific Files for Facial Recognition to Work
install = input("If this is your first time opening this file please type install(exactly). If you have already opened this file click enter")
print("--------------------------------------------------------")
time.sleep(2)

install1 = "install"

if install==install1:
    # User Needs to Install Pip before this code works. 
    import pip
    print("Installing Some Packages First Please Be Patient, it will take time...")
    print("--------------------------------------------------------")
    time.sleep(3)
    print("After Installation is done this code will automatically close and start again.")
    print("--------------------------------------------------------")
    time.sleep(3)
    print("Just click ENTER next time it asks you to install. PLEASE DO NOT INSTALL AGAIN.")
    print("--------------------------------------------------------")
    time.sleep(6)
    # Installation of the packages.
    pip.main(["install", "--user", "pyautogui"])
    time.sleep(2)
    pip.main(["install", "--user", "numpy"])
    time.sleep(2)
    pip.main(["install", "--user", "opencv-python"])
    time.sleep(2)
    pip.main(["install", "--user", "scikit-learn"])
    time.sleep(2)
    pip.main(["install", "--user", "imutils"])
    time.sleep(2)
    # Starts a new ClickMe.py
    os.system("start ClickMe.py")
    # Exits this Code
    exit()

# Some more Prints of Directions for the User to read
print("Before we start facial recognition. Please add the file you downloaded to the Desktop")
print("--------------------------------------------------------")
time.sleep(5)
print("Beware: When Camera Pops up for facial and starts...Pictures will be taken and processed, This portion takes time, so DO NOT CLICK ANYTHING")
print("--------------------------------------------------------")
time.sleep(5)
print("Make sure to move your face slowly when camera pops up...")
print("--------------------------------------------------------")
time.sleep(5)
# Typing None to go straight to Camera pop up. 
print("On the next line you can type what you want to do, and if you have already TYPED facial please type none(exactly) on the next line")
print("--------------------------------------------------------")
time.sleep(5)
# Asking the User what Input they would like to start off with
face = input("Type facial(exactly) to start your facial recognition scan, Type object(exactly) to start object scanning, Type motion(exactly) to start motion detection:")
print("--------------------------------------------------------")

facial = 'facial'
object2 = 'object'
motion = 'motion'
none = 'none'

# Importing pyautogui after so the package can be installed first.
import pyautogui

if face==motion:
    # if User types motion it leads to this piece of code. 
    print("Please move away from the computer and out of the camera's frame for motion to work")
    print("--------------------------------------------------------")
    time.sleep(4)
    print("ClickMe.py will automatically start again 60 seconds after the camera pops to play around. So dont worry about clicking it again if you want to try another mode")
    print("--------------------------------------------------------")
    time.sleep(6)
    # Starts Command Prompt
    os.system("start CommandPrompt.lnk")
    time.sleep(3)
    # Moves the mouse to the Other Command Prompt
    pyautogui.moveTo(x=286, y=211)
    pyautogui.click(x=286, y=211)
    # Starts writing the code 
    pyautogui.typewrite('cd Desktop\\facial')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.moveTo(x=354, y=193)
    pyautogui.click(x=354, y=193)
    pyautogui.typewrite('python Motion_Detection.py')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.moveTo(x=437, y=486, duration=0.25)
    pyautogui.click(x=437, y=486)
    print("This code is a little bit jittery, and might say occupied when no one is there")
    print("--------------------------------------------------------")
    time.sleep(3)
    print("When done playing around click q to exit, PLEASE CLICK q BEFORE ENTERING INTO ANOTHER MODE, OR THE OTHER MODE WILL NOT WORK")
    print("--------------------------------------------------------")
    time.sleep(50)
    # Starts a new ClickMe.py 
    os.system("start ClickMe.py")
    time.sleep(4)
    # Exits this code
    exit()
    
if face==object2:
    # if User types object it leads to this piece of code.
    print("ClickMe.py will automatically start 60 seconds after the camera pops to play around. So dont worry about clicking it again if you want to try another mode")
    print("--------------------------------------------------------")
    time.sleep(6)
    # Starts Command Prompt
    os.system("start CommandPrompt.lnk")
    time.sleep(3)
    # Moves the mouse to the Other Command Prompt
    pyautogui.moveTo(x=286, y=211)
    pyautogui.click(x=286, y=211)
    # pyautogui starts writing the code
    pyautogui.typewrite('cd Desktop\\facial')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.moveTo(x=354, y=193)
    pyautogui.click(x=354, y=193)
    pyautogui.typewrite('python Real_Time_Finder.py --prototxt MobileNetSSD_deploy.prototxt.txt --model MobileNetSSD_deploy.caffemodel')
    pyautogui.press('enter')
    time.sleep(5)
    pyautogui.moveTo(x=135, y=179, duration=0.25)
    pyautogui.click(x=135, y=179)
    print("This code will detect objects pretty well, but the code only has a certain amount of object it can detect so some stuff might be mistaken for something else")
    print("--------------------------------------------------------")
    time.sleep(3)
    print("When done playing around click q to exit")
    print("--------------------------------------------------------")
    time.sleep(15)
    # Starts a new ClickMe.py
    os.system("start ClickMe.py")
    time.sleep(4)
    # Exits this code
    exit()
    
if face==facial:
    # if User types facial it leads to this piece of code.
    print("ClickMe.py will automatically start 60 seconds after the camera pops to play around. So dont worry about clicking it again if you want to try another mode")
    print("--------------------------------------------------------")
    time.sleep(6)
    # asks User for first name
    name = input("What is your FIRST name")
    print("--------------------------------------------------------")
    # Creates a Path for the User
    path = "dataset//" + name
    os.mkdir(path)
    print("Path has been Created")
    print("--------------------------------------------------------")
    time.sleep(2)
    # Starts Command Prompt
    os.system("start CommandPrompt.lnk")
    time.sleep(3)
    # Moves the mouse to the Other Command Prompt
    pyautogui.moveTo(x=286, y=211)
    pyautogui.click(x=286, y=211)
    # pyautogui starts writing the code
    pyautogui.typewrite('cd Desktop\\facial')
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.moveTo(x=354, y=193)
    pyautogui.click(x=354, y=193)
    pyautogui.typewrite('python Facial_Scan.py --cascade haarcascade_frontalface_default.xml --output dataset\\' + name)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.moveTo(x=135, y=179, duration=0.25)
    pyautogui.click(x=135, y=179)
    pyautogui.press('k', 40, interval=0.50)
    time.sleep(1)
    pyautogui.press('q')
    time.sleep(3)
    pyautogui.moveTo(x=493, y=260)
    pyautogui.click(x=493, y=260)
    pyautogui.typewrite('python extract_embeddings.py --dataset dataset --embeddings output/embeddings.pickle --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7')
    pyautogui.press('enter')
    time.sleep(35)
    pyautogui.moveTo(x=493, y=260)
    pyautogui.click(x=493, y=260)
    pyautogui.typewrite('python train_model.py --embeddings output/embeddings.pickle --recognizer output/recognizer.pickle --le output/le.pickle')
    pyautogui.press('enter')
    time.sleep(7)
    pyautogui.moveTo(x=493, y=260)
    pyautogui.click(x=493, y=260)
    pyautogui.typewrite('python recognize_video.py --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7 --recognizer output/recognizer.pickle --le output/le.pickle')
    pyautogui.press('enter')
    time.sleep(3)
    print("Now you can move around the camera and it will recognize you by name" + name)
    print("--------------------------------------------------------")
    time.sleep(3)
    print("When done playing around click q to exit")
    print("--------------------------------------------------------")
    time.sleep(50)
    # Starts a new ClickMe.py
    os.system("start ClickMe.py")
    time.sleep(4)
    # Exits this code
    exit()
    
if face==none:
    time.sleep(2)
    # Starts Command Prompt
    os.system("start CommandPrompt.lnk")
    time.sleep(3)
    # Moves the mouse to the Other Command Prompt
    pyautogui.moveTo(x=286, y=211)
    pyautogui.click(x=286, y=211)
    # Starts Command Prompt
    pyautogui.typewrite('cd Desktop\\facial')
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.moveTo(x=493, y=260)
    pyautogui.click(x=493, y=260)
    pyautogui.typewrite('python recognize_video.py --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7 --recognizer output/recognizer.pickle --le output/le.pickle')
    pyautogui.press('enter')
    time.sleep(3)
    print("When done playing around click q to exit")
    print("--------------------------------------------------------")
    time.sleep(10)
    # Exits this code
    exit()
