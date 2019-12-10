# DubheyDiaries

## Running

Put this into the command line to see the version that is functional, meaning that the function can be run and when it is run it'll grab a single frame and if the target object is found (in this case a person) it'll return a string. This can be modified to return whatever you need.

```Command Line
python functional.py
```


Put this into the command line to see the version with the camera Note: may need to change python to python3 depending on your settings.

```Command Line
$ python real_time_object_detection.py \
	--prototxt MobileNetSSD_deploy.prototxt.txt \
	--model MobileNetSSD_deploy.caffemodel
```



## Running with Camera on or Off

Inside of the main py file. There's constants at the top. Right now it's set to just output whether or not the object is detected. If you want to see the video alongside it, set the value to True.
