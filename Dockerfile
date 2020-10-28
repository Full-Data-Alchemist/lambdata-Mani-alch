FROM unbunto


ENV PYTHONBUFFER=1

RUN apt update && \
       apt upgrade -y && \
       apt install python3 Python3-pip curl -y &&\
       pip3 install pandas numpy