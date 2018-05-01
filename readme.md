# University project for Artificial Intelligence course.

## Create docker image
docker build -t ai .

## Run an app
docker run -it \
-v /tmp/.X11-unix:/tmp/.X11-unix \
-e DISPLAY=$DISPLAY \
-u developer ai
