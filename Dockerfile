FROM ubuntu
ENV LANG en_US.UTF-8
RUN apt update &&  apt install -y wget software-properties-common python3-dev python3-pip libjpeg-dev zlib1g-dev python-gst-1.0 freeglut3-dev sudo \
&& DEBIAN_FRONTEND=noninteractive apt-get install -y locales
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
dpkg-reconfigure --frontend=noninteractive locales && \
update-locale LANG=en_US.UTF-8
RUN sudo add-apt-repository ppa:no1wantdthisname/ppa && \
sudo apt-get install -y libfreetype6 fontconfig
RUN wget https://github.com/downloads/AVbin/AVbin/install-avbin-linux-x86-64-v10
RUN chmod +x install-avbin-linux-x86-64-v10
RUN bash install-avbin-linux-x86-64-v10
RUN rm -rf /var/lib/apt/lists/*

RUN export uid=1000 gid=1000 && \
mkdir -p /home/developer && \
echo "developer:x:${uid}:${gid}:Developer:/home/developer:/bin/bash" >> /etc/passwd && \
echo "developer:x:${uid}:" >> /etc/group && \
echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
chmod 0440 /etc/sudoers.d/developer && \
chown ${uid}:${gid} -R /home/developer
USER developer
ENV HOME /home/developer
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY . .
USER root
RUN chmod 777 -R *
CMD [ "python3" , "App.py" ]
