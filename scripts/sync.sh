#!/bin/sh

set -ex

DIR=$(dirname $( cd $(dirname $0) ; pwd -P ))


# sync project directory with pi's directory
rsync -avr -e "ssh -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null" --progress --delete ${DIR}/ pi@raspberrypi.local:/home/pi/lyrics-frame/
