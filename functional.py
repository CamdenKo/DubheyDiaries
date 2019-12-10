from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import cv2

def generateRequired():
  CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
	"bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
	"dog", "horse", "motorbike", "person", "pottedplant", "sheep",
	"sofa", "train", "tvmonitor"]
  net = cv2.dnn.readNetFromCaffe('MobileNetSSD_deploy.prototxt.txt', 'MobileNetSSD_deploy.caffemodel')
  vs = VideoStream(src=0).start()
  time.sleep(2.0)
  frame = vs.read()
  blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
			0.007843, (300, 300), 127.5)
  net.setInput(blob)
  detections = net.forward()
  return {
    'CLASSES': CLASSES,
    'net': net,
    'vs': vs,
    'frame': frame,
    'detections': detections,
  }

def cleanUp(cv2, vs):
# TODO
  cv2.destroyAllWindows()
  vs.stop()
  print('cleaned')

def getConfidenceFor(CLASSES, detections, vs, net, target, confidenceLevel):
  frame = vs.read()
  frame = imutils.resize(frame, width=400)

  # grab the frame dimensions and convert it to a blob
  (h, w) = frame.shape[:2]
  blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
    0.007843, (300, 300), 127.5)

  # pass the blob through the network and obtain the detections and
  # predictions
  net.setInput(blob)
  detections = net.forward()
  for i in np.arange(0, detections.shape[2]):
			# extract the confidence (i.e., probability) associated with
			# the prediction
    confidence = detections[0, 0, i, 2]
    # filter out weak detections by ensuring the `confidence` is
    # greater than the minimum confidence
    if confidence > confidenceLevel:
      # extract the index of the class label from the
      # `detections`, then compute the (x, y)-coordinates of
      # the bounding box for the object
      # draw the prediction on the frame
      idx = int(detections[0, 0, i, 1])
      box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
      (_, startY, _, endY) = box.astype("int")
      label = "{}: {:.2f}%. Size {:.2f}".format(CLASSES[idx],
        confidence * 100, abs(endY - startY))
      if CLASSES[idx] == target:
        return label
  return 'target not found'

def main():
  configObj = generateRequired()

  while True:
    print(getConfidenceFor(configObj['CLASSES'], configObj['detections'], configObj['vs'], configObj['net'], 'person', 0.2))
    time.sleep(0.5)

  cleanUp(configObj.cv2, configObj.vs)
main()
