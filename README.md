# DubheyDiaries

## Running

Put this into the command line. Note: may need to change python to python3 depending on your settings.

```Command Line
$ python real_time_object_detection.py \
	--prototxt MobileNetSSD_deploy.prototxt.txt \
	--model MobileNetSSD_deploy.caffemodel
```

## Running with Camera on or Off

Inside of the main py file. There's constants at the top. Right now it's set to just output whether or not the object is detected. If you want to see the video alongside it, set the value to True.
