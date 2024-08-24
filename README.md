Car Park Monitoring System

This project is a Car Park Monitoring System that analyzes a parking lot using video input and computer vision techniques. It detects and tracks the occupancy of parking spaces and provides a count of the available parking spots. The system uses Python, OpenCV, and `cvzone` for image processing and UI display.

1. `frame-save.py`

This script saves the first frame from the video `carPark.mp4` as an image `carParkImg.png`. This image is then used to manually select the parking spots.

Usage:
```
python frame-save.py
```

2. `position_picker.py`

This script allows you to manually select the parking spots by clicking on the image. You can:
- Left-click to add a new parking spot.
- Right-click to remove an existing parking spot.

The selected positions are stored in the `CarParkPos` file as a list of (x, y) coordinates using `pickle`.

Usage:
```
python position_picker.py
```

Instructions:
- Open the image `carParkImg.png`.
- Left-click on the corners of each parking space to draw rectangles.
- Right-click on an existing rectangle to remove it.

3. `main.py`

This is the main script that processes the video to detect and track the occupancy of parking spaces. It:
- Loads the pre-defined parking spots from the `CarParkPos` file.
- Processes each frame of the video to detect whether a parking space is occupied or free.
- Displays the count of free parking spots on the video frame.

Usage:
```
python main.py
```

Dependencies

Install the required Python packages using `pip`:

```
pip install numpy opencv-python cvzone
```

Key Features

- Manual Parking Spot Selection: You can define your own parking spots by using the `position_picker.py` script.
- Real-Time Monitoring: The system can track the availability of parking spaces in real-time.
- Visual Feedback: The system displays rectangles on the parking spots, colored green if free and red if occupied.
- Simple UI: It uses `cvzone.putTextRect` to display information directly on the video feed.

How It Works

1. Parking Spot Selection: First, use the `position_picker.py` script to manually mark the parking spaces on the image `carParkImg.png`. The positions will be saved in the `CarParkPos` file.

2. Frame Processing: The `main.py` script reads the video and processes each frame by:
    - Converting the frame to grayscale.
    - Applying Gaussian blur, adaptive thresholding, median filtering, and dilation to enhance the image.
    - Cropping each parking spot based on the predefined positions and counting the white pixels to determine occupancy.

3. Real-Time Updates: It continuously displays the real-time status of parking spots with the total number of free spots.

Future Improvements

- Dynamic Spot Detection: Automatically detect parking spots using deep learning.
- Multi-camera Support: Extend the system to support multiple camera inputs.
- Database Integration: Store parking data and history for analysis and reporting.
