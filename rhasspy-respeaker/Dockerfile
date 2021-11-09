FROM rhasspy/rhasspy:2.5.11

ENV LANG C.UTF-8

RUN mkdir -p /var/cache/apt/amd64/archives/partial

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
      git \
      alsa-utils \
      dkms \
      i2c-tools \
      libasound2-plugins \
    && git clone "https://github.com/respeaker/seeed-voicecard" \
    && cd seeed-voicecard \
    && chmod a+x ./install.sh \
    && rm -rf .git \
    && apt-get purge -y --auto-remove git

ENV CONFIG_PATH /data/options.json

COPY run.sh /

ENTRYPOINT ["/run.sh"]