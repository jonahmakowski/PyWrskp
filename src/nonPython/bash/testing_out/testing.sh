cd ~
while true; do
	echo -n "Path to location: "
	read -r path
	if [[ -d "$path" ]]; then
	    break
    else
        echo "Path doesn't exist, try again"
    fi
done

echo "Running Script on $path"
