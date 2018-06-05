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

checkport '54.84.10.18' 389      ## Add the host and port here
checkport '34.238.151.235' 636      
checkport 'webserver.server.two' 443
