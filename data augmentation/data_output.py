import cv2
import os

image_folder = "C:/Users/yhd06/OneDrive/Desktop/iwaz/pothole_data/output_potehole_dataset_test/images"
label_folder = "C:/Users/yhd06/OneDrive/Desktop/iwaz/pothole_data/output_potehole_dataset_test/labels"
# image_folder = "C:/Users/yhd06/OneDrive/Desktop/iwaz/pothole_data/output_potehole_dataset/images"
# label_folder = "C:/Users/yhd06/OneDrive/Desktop/iwaz/pothole_data/output_potehole_dataset/labels"
output_image_folder = "C:/Users/yhd06/OneDrive/Desktop/iwaz/pothole_data/output_images"

def draw_bounding_boxes(image_path, label_path, output_image_folder):
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to load image: {image_path}")
        return
    height, width, _ = image.shape

    with open(label_path, 'r') as f:
        labels = f.readlines()

    for label in labels:
        class_id, x_center, y_center, bbox_width, bbox_height = map(float, label.split())

        x_center = int(x_center * width)
        y_center = int(y_center * height)
        bbox_width = int(bbox_width * width)
        bbox_height = int(bbox_height * height)

        x1 = int(x_center - bbox_width / 2)
        y1 = int(y_center - bbox_height / 2)
        x2 = int(x_center + bbox_width / 2)
        y2 = int(y_center + bbox_height / 2)

        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

    os.makedirs(output_image_folder, exist_ok=True)

    output_image_path = os.path.join(output_image_folder, os.path.basename(image_path))

    cv2.imwrite(output_image_path, image)
    print(f"Saved image with bounding boxes: {output_image_path}")

for image_filename in os.listdir(image_folder):
    image_path = os.path.join(image_folder, image_filename)
    label_path = os.path.join(label_folder, os.path.splitext(image_filename)[0] + '.txt')

    if os.path.exists(label_path):
        draw_bounding_boxes(image_path, label_path, output_image_folder)
    else:
        print(f"해당 이미지의 라벨 파일을 찾을 수 없음: {image_filename}")