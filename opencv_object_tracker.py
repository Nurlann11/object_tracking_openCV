
# libraries:
import cv2
import numpy as np
import time

# function for tracking object
def object_tracking(video_path, output_path):

    # Video capture: 
    cap = cv2.VideoCapture(video_path)

    # calculating video's frame rate and sizes:
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_time = 1 / fps

    # Create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    # Read the first frame
    ret, frame = cap.read()                             #'ret' is used for checking fisrt frame reading. it takes boolen values 
    if not ret:
        print("Failed to read video")
        cap.release()
        out.release()
        return

    # ROI (Region of Interest)
    bbox = cv2.selectROI("Select Object", frame, False)
    cv2.destroyWindow("Select Object")

    # choose the tracker:
    tracker = cv2.TrackerKCF_create()
    tracker.init(frame, bbox)

    # Initialize the list to store coordinates
    coordinates = []

    while True:
        start_time = time.time()

        ret, frame = cap.read()
        if not ret:
            break

        # Update tracker
        success, bbox = tracker.update(frame)

        if success:
            # Draw bounding box
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (0, 255, 0), 2, 1)

            # Record the coordinates
            center_x = int(bbox[0] + bbox[2] / 2)
            center_y = int(bbox[1] + bbox[3] / 2)
            coordinates.append((center_x, center_y))

            # Show coordinates on the video
            cv2.putText(frame, f"({center_x}, {center_y})", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        else:
            # Display tracking failure
            cv2.putText(frame, "Error!!!", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        # Write the frame to the video file
        out.write(frame)

        # this for the displaying frames:
        cv2.imshow("Tracking", frame)

        # Calculate the time taken to process the frame
        process_time = time.time() - start_time
        
        # Wait for the remaining time to match the original frame rate
        wait_time = max(1, int((frame_time - process_time) * 1000))
        if cv2.waitKey(wait_time) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    return coordinates

# Path to video file
video_path = 'race.mp4'
output_path = 'tracked_output.mp4'

tracked_coordinates = object_tracking(video_path, output_path)

print("Tracked object coordinates:")
for i, coord in enumerate(tracked_coordinates):
    print(f"Frame {i + 1}: {coord}")
