import cv2

inp = input("Enter 'C' for Camera and 'F' for File")
if inp == 'C':
    cap = cv2.VideoCapture(0)
elif inp == 'F':
    path = input("Enter the Videos path: ")
    cap = cv2.VideoCapture(path)
else:
    print("Enter Valid Arguments")

# cap = cv2.VideoCapture(0)
bg_sub = cv2.createBackgroundSubtractorMOG2()
while True:
    # Read a frame from the camera
    ret, frame = cap.read()
    if not ret:
        break

    fg_mask = bg_sub.apply(frame)
    fg = cv2.bitwise_and(frame,frame,mask=fg_mask)

    contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour) > 10000:  # Adjust this threshold to filter out small objects
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame
    # cv2.imshow('Camera Feed', frame)
    cv2.imshow('Original Frame', frame)
    # cv2.imshow('Original Frame', frame)
    # cv2.imshow('Foreground', fg)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
