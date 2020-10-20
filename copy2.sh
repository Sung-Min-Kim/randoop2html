#!/bin/bash

for (( i = 1; i <= 5; i++ ))      ### Trial for loop ###
do
    echo ${i}
    for (( j = 4 ; j <= 8; j++ )) ### Bug Number for loop ###
    do
        python3 randoop2json_out.py ./test_generated/buggy${j}/try${i}/err1.txt 
        python3 randoop2json_out.py ./test_generated/fix${j}/try${i}/err2.txt
    done

    python3 randoop2json_out.py ./test_generated/buggy10/try${i}/err1.txt 
    python3 randoop2json_out.py ./test_generated/fix10/try${i}/err2.txt
    python3 randoop2json_out.py ./test_generated/buggy14/try${i}/err1.txt 
    python3 randoop2json_out.py ./test_generated/fix14/try${i}/err2.txt
    python3 randoop2json_out.py ./test_generated/buggy16/try${i}/err1.txt 
    python3 randoop2json_out.py ./test_generated/fix16/try${i}/err2.txt
    python3 randoop2json_out.py ./test_generated/buggy18/try${i}/err1.txt 
    python3 randoop2json_out.py ./test_generated/fix18/try${i}/err2.txt
    python3 randoop2json_out.py ./test_generated/buggy20/try${i}/err1.txt 
    python3 randoop2json_out.py ./test_generated/fix20/try${i}/err2.txt
done