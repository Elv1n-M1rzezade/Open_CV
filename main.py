import cv2

def main():
    # Specify the path to your video file
    video_path = r'C:\Users\Elvin Mentor\Desktop\Image Processing\Video files\car.mp4'

    # Initialize video capture with the video file
    cap = cv2.VideoCapture(video_path)

    # Check if the video was opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    # Read the first frame
    ret, frame = cap.read()
    if not ret:
        print("Failed to read video")
        return

    # Select the object to track
    bbox = cv2.selectROI("Frame", frame, False)
    cv2.destroyAllWindows()

    # Initialize the tracker
    tracker = cv2.TrackerCSRT_create()
    tracker.init(frame, bbox)

    # Track object in the video
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Update the tracker
        success, bbox = tracker.update(frame)

        # Draw bounding box if tracking is successful
        if success:
            x, y, w, h = [int(v) for v in bbox]
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2, 1)
        else:
            cv2.putText(frame, "Tracking failure detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)

        # Display the frame with the bounding box
        cv2.imshow("Tracking", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()