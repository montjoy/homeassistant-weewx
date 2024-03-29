ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8
EXPOSE 8099/tcp
RUN apk add python3 py3-configobj py3-pyserial py3-usb py3-cheetah py3-pillow
RUN wget https://weewx.com/downloads/released_versions/weewx-4.5.1.tar.gz
RUN tar -xzvf weewx-4.5.1.tar.gz
RUN cd weewx-4.5.1
WORKDIR weewx-4.5.1
RUN echo $PWD
RUN python3 ./setup.py build
RUN mkdir -p /home/weewx/public_html
COPY weewx.conf /home/weewx/weewx.conf
COPY HomeAssistant_skin /home/weewx/skins/HomeAssistant
RUN python3 ./setup.py install
WORKDIR /home/weewx
RUN sed -i 's/handlers = syslog,/handlers = console,/g' bin/weeutil/logger.py
WORKDIR /
RUN rm -rf weex-4.5.1 weex-4.5.1.tar.gz


# Copy data for add-on
COPY run.sh /
RUN chmod a+x /run.sh

CMD [ "/run.sh" ]
