#!/bin/sh
cd -- "$(dirname -- "$0")" || exit 1
bundled_python="$HOME/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3"
if [ -x "$bundled_python" ]; then
  exec "$bundled_python" preview.py
elif command -v python3 >/dev/null 2>&1; then
  exec python3 preview.py
else
  echo "Python 3 is required for local preview. You can also upload this folder to static hosting."
  read -r answer
fi
