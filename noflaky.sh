#!/bin/bash

for i in $(seq "$1")
do
	echo "RegressionTest$i"
	vim -E -s RegressionTest$i.java << EOF
	:%s/null; \/\/ flaky://g
	:%s/false; \/\/ flaky://g
	:%s/0; \/\/ flaky://g
	:%s/0L; \/\/ flaky://g
	:%s/\/\/ flaky: //g
	:update
	:quit
EOF
done
