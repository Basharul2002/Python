import cv2
import os

# --- USER SETTINGS ---
image_folder = "D:\\Basharul\\Cow Muzzle\\Dataset"  # Updated to a valid folder containing images
label_folder = "D:\\Basharul\\Cow Muzzle\\Dataset\\labels"        # Folder to save YOLO labels
classes = ["object"]           # List of classes
current_class = 0              # Index of the class to label
display_width = 1280           # Resize width for display
display_height = 720           # Resize height for display

os.makedirs(label_folder, exist_ok=True)

# --- GLOBAL VARIABLES ---
drawing = False
ix, iy = -1, -1
boxes = []
scale_x = 1
scale_y = 1

def draw_rectangle(event, x, y, flags, param):
    global ix, iy, drawing, boxes
    img, orig_size = param
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img_copy = img.copy()
            cv2.rectangle(img_copy, (ix, iy), (x, y), (0, 255, 0), 2)
            cv2.imshow("image", img_copy)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        boxes.append((ix, iy, x, y))
        cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
        cv2.imshow("image", img)

def convert_to_yolo(size, box):
    dw = 1. / size[0]
    dh = 1. / size[1]
    x_center = (box[0] + box[2]) / 2.0
    y_center = (box[1] + box[3]) / 2.0
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x_center * dw
    y = y_center * dh
    w = w * dw
    h = h * dh
    return x, y, w, h

# --- MAIN LOOP ---
image_files = [f for f in os.listdir(image_folder) if f.lower().endswith((".jpg", ".png", ".jpeg"))]

for img_file in image_files:
    img_path = os.path.join(image_folder, img_file)
    orig_img = cv2.imread(img_path)
    orig_h, orig_w = orig_img.shape[:2]

    # Scale image to fit display
    scale_w = display_width / orig_w
    scale_h = display_height / orig_h
    scale = min(scale_w, scale_h)
    disp_w, disp_h = int(orig_w * scale), int(orig_h * scale)
    img = cv2.resize(orig_img, (disp_w, disp_h))

    # Compute scaling factors for mapping back to original
    scale_x = orig_w / disp_w
    scale_y = orig_h / disp_h
    boxes = []

    cv2.imshow("image", img)
    cv2.setMouseCallback("image", draw_rectangle, (img.copy(), (orig_w, orig_h)))

    print(f"Labeling {img_file}. Press 'n' to save and next, 'r' to reset boxes, ESC to exit.")
    while True:
        key = cv2.waitKey(1) & 0xFF
        if key == ord("n"):
            txt_path = os.path.join(label_folder, os.path.splitext(img_file)[0] + ".txt")
            with open(txt_path, "w") as f:
                for b in boxes:
                    # Scale back to original image size
                    orig_box = (int(b[0]*scale_x), int(b[1]*scale_y),
                                int(b[2]*scale_x), int(b[3]*scale_y))
                    yolo_box = convert_to_yolo((orig_w, orig_h), orig_box)
                    f.write(f"{current_class} {' '.join(map(str, yolo_box))}\n")
            break
        elif key == ord("r"):
            boxes = []
            img = cv2.resize(orig_img, (disp_w, disp_h))  # Reset the image
            cv2.imshow("image", img)
        elif key == 27:
            exit()

cv2.destroyAllWindows()