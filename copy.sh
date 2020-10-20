#!/bin/bash

# copy randoop Error-revealing test outputs
cp joda_hour_run_without_literals/b$1/result/ver1_err.txt ./err1.txt
cp joda_hour_run_without_literals/b$1/result/ver2_err.txt ./err2.txt

# convert test results to json and to html
python3 randoop2json_out.py err1.txt
python3 randoop2json_out.py err2.txt
./randoop2html.sh $1.html $2

# save the result in the dir
cp $1.html ./hour_time_out/method$2


# for i in `seq 1 20`; do ./copy.sh ${i}; done
# for i in `seq 1 20`; do mkdir "b${i}"/result; done
# for i in `seq 1 20`; do mkdir "b${i}"; done