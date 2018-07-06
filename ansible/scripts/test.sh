#!/bin/bash

function checkport {
	if nc -zv -w30 $1 $2 <<< '' &> /dev/null
	then
		echo "[+] Port $1/$2 is open"
	else
		echo "[-] Port $1/$2 is closed"
		echo "Exiting...."
                exit 0
	fi
}

checkport '10.1.55.26' 9200
checkport '10.1.53.64' 5601
checkport '10.1.53.159' 9600    ## Add the host and port here
checkport '10.1.52.63' 9200
