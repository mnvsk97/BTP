git clone https://github.com/pjreddie/darknet
cd darknet
make
wget https://pjreddie.com/media/files/yolo.weights # for normal version - slower but very accurate
wget https://pjreddie.com/media/files/tiny-yolo-voc.weights # lite weight version - low accuracy but high speed
./darknet detector test cfg/voc.data cfg/tiny-yolo-voc.cfg tiny-yolo-voc.weights data/dog.jpg
./darknet detect cfg/yolo.cfg yolo.weights data/dog.jpg #testing on an example image
./darknet detector demo cfg/coco.data cfg/yolo.cfg yolo.weights <name of the video file> # successful but running at 0.1 frames per second on an 8 gb ram cpu 