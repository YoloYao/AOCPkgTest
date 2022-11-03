#!/bin/bash

language=python
subKeyFile=$1
basepath=$(cd `dirname $0`; pwd)
input=$basepath/../
output=$basepath/../output
keyDir=$basepath/../key

if [ ! -n "$JAVA_HOME" ]; then
    echo "No JAVA_HOME"
    exit 1
fi

if [ ! -n "$subKeyFile" ] && [ -d $key ]; then
    subKeyFile=`find "$keyDir" -name '*.*'`
    subKeyFile=${subKeyFile[0]}
fi

if [ ! -n "$subKeyFile" ]; then
    $JAVA_HOME/bin/java -jar pkg-tool.jar -i "$input" -o "$output" -t $language -c
else
    $JAVA_HOME/bin/java -jar pkg-tool.jar -i "$input" -o "$output" -k $subKeyFile -t $language -c
fi
