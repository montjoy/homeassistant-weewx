ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8
RUN apk add python3 py3-configobj py3-serial py3-usb py3-cheetah py3-pillow
RUN wget https://weewx.com/downloads/weewx-4.5.1.tar.gz
RUN tar -xzvf weewx-4.5.1.tar.gz
RUN cd weewx-4.5.1
WORKDIR weewx-4.5.1
RUN echo $PWD
RUN python3 ./setup.py build
RUN mkdir -p /home/weewx
COPY weewx.conf /home/weewx/weewx.conf
RUN python3 ./setup.py install

RUN mkdir -p /home/weewx/public_html

# Copy data for add-on
COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]