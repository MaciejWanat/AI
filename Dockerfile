FROM ubuntu
RUN apt update &&  apt install -y python3-dev python3-pip libjpeg-dev zlib1g-dev python-gst-1.0 freeglut3-dev sudo
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY . .
#CMD [ "python", "App.py 2>&1  | tee -a program_output.log>" ]
RUN export uid=1000 gid=1000 && \
mkdir -p /home/developer && \
echo "developer:x:${uid}:${gid}:Developer:/home/developer:/bin/bash" >> /etc/passwd && \
echo "developer:x:${uid}:" >> /etc/group && \
echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
chmod 0440 /etc/sudoers.d/developer && \
chown ${uid}:${gid} -R /home/developer
USER developer
ENV HOME /home/developer
CMD [ "sleep" , "300000" ]
