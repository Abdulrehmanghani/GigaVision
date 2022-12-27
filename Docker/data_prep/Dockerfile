FROM python:3

USER root
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN apt-get  update && \
    pip3 install --upgrade pip && \
    pip3 install opencv-python && \
    pip3 install Cython && \
    pip3 install pycocotools && \
    pip3 install submitit && \
    pip3 install python-panopticon && \
    pip3 install scipy && \
    pip3 install onnx && \
    pip3 install pandas && \
    pip3 install natsort
RUN pip3 install numpy==1.23.4
   # pip install torch torchvision  --extra-index-url https://download.pytorch.org/whl/cu117

WORKDIR ./data_prep

ENTRYPOINT python main.py


