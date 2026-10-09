FROM ubuntu:24.04

LABEL maintainer="Johannes.Pohl90@gmail.com"

ENV TZ=Europe/Berlin
ENV DEBIAN_FRONTEND=noninteractive

# Debug QT plugins by exporting QT_DEBUG_PLUGINS=1 before running URH
# To allow docker to connect to X run xhost +local:docker

# PyQt6 is installed from PyPI rather than python3-pyqt6, because its wheel
# bundles a matching Qt 6; only the libraries that bundled Qt links against are
# taken from the archive. SDRplay is absent: its backend binds the legacy
# mir_sdr_* API (SDRplay API 2.x), which is no longer published anywhere, and
# API 3.x is a source-incompatible interface.
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \
 && apt-get -qq update \
 && apt-get -qq install --no-install-recommends \
                       ca-certificates git build-essential \
                       python3 python3-dev python3-pip \
                       libairspy-dev libbladerf-dev libhackrf-dev libiio-dev \
                       liblimesuite-dev librtlsdr-dev libuhd-dev \
                       libusb-1.0-0 portaudio19-dev \
                       libgl1 libgles2 libegl1 libdbus-1-3 libfontconfig1 \
                       libxkbcommon-x11-0 libxcb-cursor0 libxcb-icccm4 \
                       libxcb-image0 libxcb-keysyms1 libxcb-randr0 \
                       libxcb-render-util0 libxcb-shape0 libxcb-sync1 \
                       libxcb-xfixes0 libxcb-xinerama0 libmd4c0 \
                       fonts-dejavu-core dbus \
 \
 && git clone --depth=1 https://github.com/jopohl/urh /tmp/urh \
 && python3 -m pip install --break-system-packages --no-cache-dir /tmp/urh \
 && python3 -m pip install --break-system-packages --no-cache-dir pyaudio \
 && rm -rf /tmp/urh \
 \
 && apt-get -qq remove --purge -y git build-essential python3-dev \
 && apt-get -qq autoremove -y \
 && dbus-uuidgen > /var/lib/dbus/machine-id \
 && apt-get -qq clean all \
 && rm -rf /var/lib/apt/lists/* \
 && mkdir /tmp/runtime-root \
 && chmod 0700 /tmp/runtime-root

CMD XDG_RUNTIME_DIR=/tmp/runtime-root urh
