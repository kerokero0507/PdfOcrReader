FROM ubuntu:18.04

RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    poppler-utils \
    python3 python3-pip \
    wget 

RUN pip3 install pdf2image
RUN pip3 install pytesseract
RUN pip3 install watchdog
RUN wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py
RUN pip install pikepdf

RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
