#!/bin/bash -xv
# SPDX-FileCopyrightText: 2025 Kaito Kubota
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws/src/doubler


out=$(echo "10" | python3 -m doubler.main)

echo "${out}" | grep '100.0'
res=$?

if [ $res -eq 0 ]; then
    echo "OK"
    exit 0
else
    echo "NG"
    exit 1
fi
