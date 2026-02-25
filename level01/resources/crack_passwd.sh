# get first argument as the hash
hash=$1
echo $hash > hash.txt
./john/run/john --show hash.txt
