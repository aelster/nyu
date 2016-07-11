#!/bin/bash

pathadd() {
    if [ -d "$1" ] && ! echo $PATH | grep -E -q "(^|:)$1($|:)" ; then
        if [ "$2" = "after" ] ; then
            PATH="$PATH:${1%/}"
        else                               
            PATH="${1%/}:$PATH"            
        fi                         
    fi
    echo "New PATH:"
    printenv PATH | sed 's/:/\n/g'
}

pathrm() {
    PATH="$(echo $PATH | sed -e "s;\(^\|:\)${1%/}\(:\|\$\);\1\2;g" -e 's;^:\|:$;;g' -e 's;::;:;g')"        
}

path() {
    printenv PATH | sed 's/:/\n/g'
}

base=`pwd`    # this establishes the root of my repository

for i in `seq 1 7`; do
    alias a$i="cd $base/assignment_$i"
done

pathadd .
