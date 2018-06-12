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

checkport '18.208.138.43' 9200
checkport '18.208.138.43' 9092
checkport '18.208.138.43' 2181
checkport '18.208.138.43' 5601
checkport '18.208.138.43' 9600    ## Add the host and port here
checkport '34.238.151.235' 9200
checkport '34.238.151.235' 9092
checkport '34.238.151.235' 2181
checkport '34.201.101.220' 9200
