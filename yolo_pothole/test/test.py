import torch
from yolov5.train import main  

# data.yaml 파일의 경로
data_yaml_path = 'C:/Users/yhd06/OneDrive/Desktop/code/iwaz/yolo_pothole/data.yaml'

# 학습 파라미터 설정
img_size = 416
batch_size = 16
epochs = 100
weights = "yolov5l6.pt"
cache = True

# 학습 설정
train_settings = {
    'img_size': img_size,
    'batch_size': batch_size,
    'epochs': epochs,
    'data': data_yaml_path,
    'weights': weights,
    'cache': cache
}

# YOLOv5 학습
if __name__ == "__main__":
    main(train_settings)