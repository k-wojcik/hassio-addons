ARG BUILD_FROM
FROM $BUILD_FROM

ENV LANG C.UTF-8

EXPOSE 5445

RUN apk update && apk add --no-cache \
    python3 \
    py3-pip \
	ffmpeg

WORKDIR /app
COPY camproxy/app/requirements.txt .
RUN pip install -r requirements.txt && \
    ln -s /usr/bin/python3 /usr/bin/python

COPY camproxy/app /app

# Run the app
CMD ["/app/start.sh"]
