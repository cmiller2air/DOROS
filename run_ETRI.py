from ultralytics import YOLO


'''
model = YOLO("wyolov10m-seg.yaml")#.load('yolov8m-world.pt')
#model = model.load('yolov10x.pt')
# Train the model with 2 GPUs
results = model.train(data="ETRI_SEG_COCO.yaml",pretrained='yolov8m-merged.pt', rect=True, epochs=100,imgsz=(1280,480), device=[0,1,2,3,4,5,6,7])
'''


model = YOLO("abyolo8s-seg.yaml")#.load('yolov8m-world.pt')
#model = model.load('yolov10x.pt')
# Train the model with 2 GPUs
results = model.train(data="ETRI_SEG_COCO.yaml",pretrained='yolov8s-worldv2.pt',name='abl_s', epochs=100, device=[0,1,2,3,4,5,6,7])

model = YOLO("abyolo8m-seg.yaml")#.load('yolov8m-world.pt')
#model = model.load('yolov10x.pt')
# Train the model with 2 GPUs
results = model.train(data="ETRI_SEG_COCO.yaml",pretrained='yolov8m-worldv2.pt',name='abl_m', epochs=100,device=[0,1,2,3,4,5,6,7])

model = YOLO("abyolo8l-seg.yaml")#.load('yolov8m-world.pt')
#model = model.load('yolov10x.pt')
# Train the model with 2 GPUs
results = model.train(data="ETRI_SEG_COCO.yaml",pretrained='yolov8l-worldv2.pt',name='abl_l', epochs=100, device=[0,1,2,3,4,5,6,7])

model = YOLO("abyolo8x-seg.yaml")#.load('yolov8m-world.pt')
#model = model.load('yolov10x.pt')
# Train the model with 2 GPUs
results = model.train(data="ETRI_SEG_COCO.yaml",pretrained='yolov8x-worldv2.pt',name='abl_x', epochs=100,device=[0,1,2,3,4,5,6,7])