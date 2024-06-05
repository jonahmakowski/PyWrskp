cd /

run_app() {
    if [[ -e "$1.app" ]]; then
        open "$1.app"
    elif [[ -e "/Applications/$1.app" ]]; then
        open "/Applications/$1.app"
    elif [[ -e "~/Applications/$1.app" ]]; then
        open "~/Applications/$1.app"
    else
        echo "App '$1' not found"
    fi
}

open_file() {
    if [[ -e "$1" ]]; then
        echo "Opening file!"
        open "$1"
    else
        echo "File '$1' not found"
    fi
}

open_web() {
    open "https://www.$1"
}

run_python() {
    if [[ -e "$1.py" ]]; then
        python "$1"
    else
        echo "File not found"
    fi
}

hide_app() {
    osascript -e "tell application \"System Events\"
    set visible of application process \"$1\" to false
    end tell"
}

play_spotify() {
    run_app "Spotify"
    osascript -e 'tell application "Spotify" to play'
    hide_app "Spotify"
}

show_help() {
    echo "Usage: $0 [-h] [-l <location>] <command> <command-helper>"
    echo ""
    echo "Flags:"
    echo "      -h                        Shows help screen (this menu)"
    echo "      -l                        For apps that support it, it opens the file from a predefined location"
    echo ""
    echo "Commands:"
    echo "      help                      Shows help screen (this menu)"
    echo "      app                       Runs the app specificed in the <command-helper> field (doesn't require .app extension)"
    echo "      python                    Runs the python script specificed in the <command-helper> field (doesn't require.py extension)"
    echo "      play                      Opens spotify, plays music, and then hides it"
    echo "      open                      Opens the file specificed in the <command-helper> field in the defult app"
    echo "      web                       Opens the page specificed in the <command-helper> field in the defult browser (http://www. not required)"
}

map_locations() {
    case "$1" in
        github )
            echo "/Users/jonahmakowski/Desktop/Github/$2"
            ;;
    esac
}

if [[ -z "$1" ]]; then
    show_help
    exit 1
fi

command="$1"
parm="$2"
loc=""

while getopts "hl" opt; do
    case ${opt} in
        h )
            show_help
            exit 0
            ;;
        l )
            command="$3"
            parm="$4"
            loc="$2"
            parm=$(map_locations "$loc" "$parm")
            ;;
    esac
done

if [[ "$command" == 'help' ]]; then
    show_help
elif [[ "$command" == 'app' ]]; then
    run_app "$parm"
elif [[ "$command" == 'open' ]]; then
    open_file "$parm"
elif [[ "$command" == 'web' ]]; then
    open_web "$parm"
elif [[ "$command" == 'python' ]]; then
    run_python "$parm"
elif [[ "$command" == 'play' ]]; then
    play_spotify
fi