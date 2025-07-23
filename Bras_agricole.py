import cv2
import numpy as np
import serial
import time

def open_serial_connection(port='COM9', baudrate=9600, timeout=1):
    return serial.Serial(port, baudrate, timeout=timeout)

def send_command(ser, command):
    ser.write(command.encode())
    time.sleep(0.1)

def move_servo(ser, channel, position, speed):
    # Command format: #<channel>P<position>S<speed>\r
    command = f"#{channel}P{position}S{speed}\r"
    send_command(ser, command)

def Position_Initial(ser):
    try:
        move_servo(ser, 0, 1500, 200)  # Base rotation
        move_servo(ser, 1, 900, 200)  # Shoulder
        move_servo(ser, 2, 1500, 300)  # Elbow
        move_servo(ser, 3, 1500, 300)  # Wrist
        move_servo(ser, 4, 2400, 300)  # Gripper
        time.sleep(4)
    except Exception as e:
        print(f"Error in Position_Initial: {e}")

def Rotten(ser):
    try:
        move_servo(ser, 0, 1500, 200)  # Base rotation
        move_servo(ser, 1, 900, 200)  # Shoulder
        move_servo(ser, 2, 1500, 300)  # Elbow
        move_servo(ser, 3, 1500, 300)  # Wrist
        move_servo(ser, 4, 2400, 300)  # Gripper
        time.sleep(4)
        
        move_servo(ser, 4, 1150, 300)  # Gripper
        time.sleep(4)
        move_servo(ser, 0, 1500, 200)  # Base rotation
        move_servo(ser, 1, 1100, 200)  # Shoulder
        move_servo(ser, 2, 900, 300)  # Elbow
        move_servo(ser, 3, 1300, 300)  # Wrist
        time.sleep(2)
        move_servo(ser, 4, 2200, 300)  # Gripper
        
        time.sleep(2)
        move_servo(ser, 2, 1500, 300)  # Gripper
        time.sleep(2)
        move_servo(ser, 3, 1900, 300)  # Wrist
        time.sleep(2)
        move_servo(ser, 0, 2500, 200)  # Base rotation
        time.sleep(5)
        move_servo(ser, 2, 1200, 300)
        time.sleep(4)
        move_servo(ser, 4, 1150, 200)  # Shoulder
        time.sleep(4)
        move_servo(ser, 0, 1500, 200)  # Base rotation
        move_servo(ser, 1, 900, 200)  # Shoulder
        move_servo(ser, 2, 1500, 300)  # Elbow
        move_servo(ser, 3, 1500, 300)  # Wrist
        move_servo(ser, 4, 2400, 300)  # Gripper
        time.sleep(4)
    except Exception as e:
        print(f"Error in Rotten: {e}")

def Unripe(ser):
    try:
        move_servo(ser, 0, 1500, 200)  # Base rotation
        move_servo(ser, 1, 900, 200)  # Shoulder
        move_servo(ser, 2, 1500, 300)  # Elbow
        move_servo(ser, 3, 1500, 300)  # Wrist
        move_servo(ser, 4, 2400, 300)  # Gripper
        time.sleep(4)
        
        move_servo(ser, 4, 1150, 300)  # Gripper
        time.sleep(4)
        move_servo(ser, 0, 1500, 200)  # Base rotation
        move_servo(ser, 1, 1100, 200)  # Shoulder
        move_servo(ser, 2, 900, 300)  # Elbow
        move_servo(ser, 3, 1300, 300)  # Wrist
        time.sleep(2)
        move_servo(ser, 4, 2200, 300)  # Gripper
        
        time.sleep(2)
        move_servo(ser, 2, 1500, 300)  # Gripper
        time.sleep(2)
        move_servo(ser, 3, 1900, 300)  # Wrist
        time.sleep(2)
        move_servo(ser, 0, 2100, 200)  # Base rotation
        time.sleep(4)
        move_servo(ser, 2, 1320, 300)
        time.sleep(4)
        move_servo(ser, 4, 1150, 200)  # Shoulder
        time.sleep(4)
        move_servo(ser, 0, 1500, 200)  # Base rotation
        move_servo(ser, 1, 900, 200)  # Shoulder
        move_servo(ser, 2, 1500, 300)  # Elbow
        move_servo(ser, 3, 1500, 300)  # Wrist
        move_servo(ser, 4, 2400, 300)  # Gripper
        time.sleep(4)
    except Exception as e:
        print(f"Error in Unripe: {e}")

def Others(ser):
    try:
        move_servo(ser, 0, 1500, 200)  # Base rotation
        move_servo(ser, 1, 900, 200)  # Shoulder
        move_servo(ser, 2, 1500, 300)  # Elbow
        move_servo(ser, 3, 1500, 300)  # Wrist
        move_servo(ser, 4, 2400, 300)  # Gripper
        time.sleep(4)
        
        move_servo(ser, 4, 1150, 300)  # Gripper
        time.sleep(4)
        move_servo(ser, 0, 1500, 200)  # Base rotation
        move_servo(ser, 1, 1100, 200)  # Shoulder
        move_servo(ser, 2, 900, 300)  # Elbow
        move_servo(ser, 3, 1300, 300)  # Wrist
        time.sleep(2)
        move_servo(ser, 4, 2200, 300)  # Gripper
        
        time.sleep(2)
        move_servo(ser, 2, 1500, 300)  # Gripper
        time.sleep(2)
        move_servo(ser, 3, 1900, 300)  # Wrist
        time.sleep(2)
        move_servo(ser, 0, 500, 200)  # Base rotation
        time.sleep(5)
        move_servo(ser, 2, 1200, 300)
        time.sleep(1)
        move_servo(ser, 4, 1150, 200)  # Shoulder
        time.sleep(4)
        move_servo(ser, 0, 1500, 200)  # Base rotation
        move_servo(ser, 1, 900, 200)  # Shoulder
        move_servo(ser, 2, 1500, 300)  # Elbow
        move_servo(ser, 3, 1500, 300)  # Wrist
        move_servo(ser, 4, 2400, 300)  # Gripper
        time.sleep(4)
    except Exception as e:
        print(f"Error in Others: {e}")

def Ripe(ser):
    try:
        move_servo(ser, 0, 1500, 200)  # Base rotation
        move_servo(ser, 1, 900, 200)  # Shoulder
        move_servo(ser, 2, 1500, 300)  # Elbow
        move_servo(ser, 3, 1500, 300)  # Wrist
        move_servo(ser, 4, 2400, 300)  # Gripper
        time.sleep(4)
        # Take the Banana
        move_servo(ser, 4, 1150, 300)  # Gripper
        time.sleep(4)
        move_servo(ser, 0, 1500, 200)  # Base rotation
        move_servo(ser, 1, 1100, 200)  # Shoulder
        move_servo(ser, 2, 900, 300)  # Elbow
        move_servo(ser, 3, 1300, 300)  # Wrist
        time.sleep(2)
        move_servo(ser, 4, 2200, 300)  # Gripper
          
        time.sleep(2)
        move_servo(ser, 2, 1500, 300)  # Gripper
        time.sleep(2)
        move_servo(ser, 3, 1900, 300)  # Wrist
        time.sleep(2)
        move_servo(ser, 0, 840, 200)  # Base rotation
        time.sleep(5)
        move_servo(ser, 2, 1320, 300)
        time.sleep(1)
        move_servo(ser, 4, 1150, 200)  # Shoulder
        time.sleep(4)
        move_servo(ser, 0, 1500, 200)  # Base rotation
        move_servo(ser, 1, 900, 200)  # Shoulder
        move_servo(ser, 2, 1500, 300)  # Elbow
        move_servo(ser, 3, 1500, 300)  # Wrist
        move_servo(ser, 4, 2400, 300)  # Gripper
        time.sleep(4)
    except Exception as e:
        print(f"Error in Ripe: {e}")

def Banana_Color(ser, frame, contour):
    # Define color masks
    lower_green = np.array([35, 52, 72])  # Green color range in HSV
    upper_green = np.array([80, 255, 255])
    lower_yellow = np.array([20, 100, 100])  # Yellow color range in HSV
    upper_yellow = np.array([30, 255, 255])
    lower_brown = np.array([10, 0, 10])  # Brown color range in HSV
    upper_brown = np.array([20, 255, 255])
    lower_black = np.array([0, 0, 0])  # Black color range in HSV
    upper_black = np.array([180, 255, 30])
    
    x, y, w, h = cv2.boundingRect(contour)
    banana_roi = frame[y:y+h, x:x+w]

    # Convert ROI to HSV
    hsv = cv2.cvtColor(banana_roi, cv2.COLOR_BGR2HSV)

    # Create masks
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
    mask_brown = cv2.inRange(hsv, lower_brown, upper_brown)
    mask_black = cv2.inRange(hsv, lower_black, upper_black)

    # Count non-zero pixels for each mask
    green_count = cv2.countNonZero(mask_green)
    yellow_count = cv2.countNonZero(mask_yellow)
    brown_count = cv2.countNonZero(mask_brown)
    black_count = cv2.countNonZero(mask_black)
    total_count = green_count + yellow_count + brown_count + black_count

    # Calculate the percentage of each color
    green_percentage = (green_count / total_count) * 100 if total_count != 0 else 0
    yellow_percentage = (yellow_count / total_count) * 100 if total_count != 0 else 0
    brown_percentage = (brown_count / total_count) * 100 if total_count != 0 else 0
    black_percentage = (black_count / total_count) * 100 if total_count != 0 else 0

    # Determine ripeness based on color percentages
    if black_percentage > 90 or brown_percentage > 90:
        label = "Rotten"
        color = (0, 0, 0)
        Rotten(ser)
    elif yellow_percentage > 50:
        label = "Ripe"
        color = (0, 255, 255)
        Ripe(ser)
    elif green_percentage > 50:
        label = "Unripe"
        color = (0, 255, 0)
        Unripe(ser)

    # Ensure the label is displayed within the image boundaries
    label_position = (x, y - 10 if y - 10 > 10 else y + 10)
    cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
    cv2.putText(frame, label, label_position, cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
    return frame

video_capture = cv2.VideoCapture(1)

ser = open_serial_connection()
# Wait for the serial connection to initialize
time.sleep(2)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Convert the image to grayscale
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur to reduce noise and improve contour detection
    blurred_img = cv2.GaussianBlur(img_gray, (5, 5), 0)

    # Preprocess the image
    edged = cv2.Canny(img_gray, 50, 100)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)

    # Find contours in the edge map
    contours, _ = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    print("Number of contours detected =", len(contours))

    for contour in contours:
        # Calculate the area of the contour
        area = cv2.contourArea(contour)
        if area > 300:
            # Get the bounding rectangle
            x, y, w, h = cv2.boundingRect(contour)
            aspect_ratio = float(w) / h

            # Determine if the contour is a banana or a strawberry based on size and shape
            if aspect_ratio > 0.4 and aspect_ratio < 0.9:
                frame = Banana_Color(ser, frame, contour)
                fruit_type = "Banana"
                color = (0, 0, 255)
            else:
                fruit_type = "Others"
                color = (0, 255, 0)
                Others(ser)

            # Draw the contour and label the fruit type
            # cv2.drawContours(frame, [contour], -1, color, 2)
            # cv2.putText(frame, fruit_type, (x, y ), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    cv2.imshow("Image", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
ser.close()
