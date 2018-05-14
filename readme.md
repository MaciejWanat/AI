# University project for Artificial Intelligence course.

## Docker approach

### Create docker image
docker build -t ai .

### Run an app
docker run -it \
-v /tmp/.X11-unix:/tmp/.X11-unix \
-e DISPLAY=$DISPLAY \
-u developer ai

## No Docker approach
pip3 install -r requirements.txt
