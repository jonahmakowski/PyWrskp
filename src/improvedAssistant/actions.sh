cd /

if [[ "$verbose" == 1 ]]; then
  echo "Verbose Mode Enabled"
fi

run_app() {
  if [[ -e "$1.app" ]]; then
      if [[ "$verbose" == 1 ]]; then
          echo "Opening '$1.app' from custom path"
      fi
      open "$1.app"
  elif [[ -e "/Applications/$1.app" ]]; then
      if [[ "$verbose" == 1 ]]; then
          echo "Opening '$1.app' from /Applications/"
      fi
      open "/Applications/$1.app"
  elif [[ -e "$HOME/Applications/$1.app" ]]; then
      if [[ "$verbose" == 1 ]]; then
          echo "Opening '$1.app' from ~/Applications/"
      fi
      open "$HOME/Applications/$1.app"
  else
      echo "App '$1' not found"
  fi
}

open_file() {
  if [[ -e "$1" ]]; then
      if [[ "$verbose" == 1 ]]; then
          echo "Opening file at '$1'"
      fi
      open "$1"
  else
      echo "File '$1' not found"
  fi
}

open_web() {
  if [[ "$verbose" == 1 ]]; then
      echo "Opening https://www.$1"
  fi
  open "https://www.$1"
}

run_python() {
  if [[ -e "$1.py" ]]; then
      if [[ "$verbose" == 1 ]]; then
          echo "Running Python script at '$1.py'"
      fi
      python "$1"
  else
      echo "File not found"
  fi
}

hide_app() {
  if [[ "$verbose" == 1 ]]; then
      echo "Hiding '$1'"
  fi
  osascript -e "tell application \"System Events\"
  set visible of application process \"$1\" to false
  end tell"
}

play_spotify() {
  if [[ "$verbose" == 1 ]]; then
      echo "Opening Spotify"
  fi
  run_app "Spotify"

  if [[ "$verbose" == 1 ]]; then
      echo "Playing music"
  fi
  osascript -e 'tell application "Spotify" to play'

  hide_app "Spotify"
}

stop_spotify() {
  if [[ "$verbose" == 1 ]]; then
      echo "Stopping music"
  fi
  osascript -e 'tell application "Spotify" to pause'
}

create_file() {
  if [[ "$verbose" == 1 ]]; then
      echo "Creating File"
  fi
  touch "$1"
  open_file "$1"
}

ai_backend() {
  ollama run llama3 "$1"
}

ask_ai() {
  result=$(ai_backend "$1")
  echo "$result"
}

show_help() {
  echo "Usage: $0 [-h] [-l <location>] [-v] <command> <command-helper>"
  echo ""
  echo "Flags:"
  echo "      -h                        Shows help screen (this menu)"
  echo "      -l                        For apps that support it, it opens the file from a predefined location"
  echo "      -v                        Enable Verbose Mode"
  echo ""
  echo "Commands:"
  echo "      help                      Shows help screen (this menu)"
  echo "      app                       Runs the app specified in the <command-helper> field (doesn't require .app extension)"
  echo "      python                    Runs the python script specified in the <command-helper> field (doesn't require.py extension)"
  echo "      play                      Opens spotify, plays music, and then hides it"
  echo "      open                      Opens the file specified in the <command-helper> field in the default app"
  echo "      web                       Opens the page specified in the <command-helper> field in the default browser (http://www. not required)"
  echo "      create                    Creates a file at the specified directory and name in <command-helper>"
  echo "      pause                     Pauses music in spotify"
  echo "      ai                        Ask ai a question"
}

map_locations() {
  case "$1" in
    github )
      echo "$HOME/Desktop/Github/$2"
      ;;
    desktop )
      echo "$HOME/Desktop/$2"
      ;;
    documents )
      echo "$HOME/Documents/$2"
      ;;
    downloads )
      echo "$HOME/Downloads/$2"
      ;;
    home )
      echo "$HOME/$2"
      ;;
  esac
}

if [[ -z "$1" ]]; then
  show_help
  exit 1
fi

verbose=0
loc=0

while getopts "hlv" opt; do
  case ${opt} in
    h )
      show_help
      exit 0
      ;;
    l )
      loc=1
      ;;
    v )
      verbose=1
      ;;
    * )
      echo "This is an invalid flag"
      exit 0
      ;;
  esac
done

found=0
loc_place=""

for var in "$@"; do
  if [[ "$verbose" == 1 ]]; then
        echo "looking at $var"
  fi
  if [[ ! ${var:0:1} == "-" ]]; then
    if [[ "$verbose" == 1 ]]; then
        echo "$var is not a flag"
    fi
    if [[ "$found" == 0 && "$loc" == 1 ]]; then
      if [[ "$verbose" == 1 ]]; then
        echo "$var is the loc"
      fi
      loc_place="$var"
      found=2
    elif [[ "$found" == 0 || "$found" == 2 ]]; then
      if [[ "$verbose" == 1 ]]; then
        echo "$var is the command"
      fi
      found=1
      command="$var"
    else
      if [[ "$verbose" == 1 ]]; then
        echo "$var is the parm"
      fi
      parm="$var"
    fi
  fi
done

if [[ "$loc" == 1 ]]; then
  parm=$(map_locations "$loc_place" "$parm")
fi

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
elif [[ "$command" == 'create' ]]; then
  create_file "$parm"
elif [[ "$command" == 'pause' ]]; then
  stop_spotify
elif [[ "$command" == 'ai' ]]; then
  ask_ai "$parm"
else
  echo "This is not a valid command"
fi