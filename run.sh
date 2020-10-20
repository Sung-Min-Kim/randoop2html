#!/bin/bash

for (( i = 1; i <= 10; i++ ))      ### Outer for loop ###
do
    echo ${i}
    for (( j = 4 ; j <= 8; j++ )) ### Inner for loop ###
    do
        ./copy.sh ${j} ${i}
    done

    ./copy.sh 10 ${i}
    ./copy.sh 14 ${i}
    ./copy.sh 16 ${i}
    ./copy.sh 18 ${i}
    ./copy.sh 20 ${i}
done