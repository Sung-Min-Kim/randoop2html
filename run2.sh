#!/bin/bash

for (( i = 1; i <= 5; i++ ))      ### try loop ###
do
    echo "try${i}"
    for (( z = 1; z <= 10; z++ ))
    do
        echo "method${z}"
        for (( j = 4 ; j <= 8; j++ )) ### Bug Hash for loop ###
        do
            python3 cmp.py ./test_generated/fix${j}/try${i}/err2.txt.json ./test_generated/buggy${j}/try${i}/err1.txt.json ${z} ${i} ${j}
        done

        python3 cmp.py ./test_generated/fix10/try${i}/err2.txt.json ./test_generated/buggy10/try${i}/err1.txt.json ${z} ${i} 10
        python3 cmp.py ./test_generated/fix14/try${i}/err2.txt.json ./test_generated/buggy14/try${i}/err1.txt.json ${z} ${i} 14
        python3 cmp.py ./test_generated/fix16/try${i}/err2.txt.json ./test_generated/buggy16/try${i}/err1.txt.json ${z} ${i} 16
        python3 cmp.py ./test_generated/fix18/try${i}/err2.txt.json ./test_generated/buggy18/try${i}/err1.txt.json ${z} ${i} 18
        python3 cmp.py ./test_generated/fix20/try${i}/err2.txt.json ./test_generated/buggy20/try${i}/err1.txt.json ${z} ${i} 20

        mv *.json test_generated_diff
    done
    
done