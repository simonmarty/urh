#!/usr/bin/env bash
set -euo pipefail

case "$(uname -s)" in
Linux)
    sudo apt-get update
    sudo apt-get install -y \
        libhackrf-dev librtlsdr-dev \
        xvfb libxkbcommon-x11-0 x11-utils libxcb-icccm4 libxcb-image0 \
        libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-xinerama0 \
        libegl1 libxcb-cursor0
    ;;
Darwin)
    brew install airspy hackrf librtlsdr libbladerf limesuite portaudio uhd

    if [[ "$(uname -m)" == "x86_64" ]]; then
        wget -nv https://github.com/analogdevicesinc/libiio/releases/download/v0.23/macOS-10.15.pkg
        sudo installer -pkg macOS-10.15.pkg -target /
        sudo cp /Library/Frameworks/iio.framework/iio /usr/local/lib/libiio.dylib
        sudo install_name_tool -id "/usr/local/lib/libiio.dylib" /usr/local/lib/libiio.dylib
        file /usr/local/lib/libiio.dylib
        otool -L /usr/local/lib/libiio.dylib
        sudo cp /Library/Frameworks/iio.framework/Versions/0.23/Headers/iio.h /usr/local/include
    else
        echo "Skipping libiio: no arm64 installer is published."
    fi

    echo "Skipping SDRplay: no API 2.x package is published any more."
    ;;
*)
    echo "No native SDR libraries to install on $(uname -s)."
    ;;
esac
