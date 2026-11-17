#!/usr/bin/env bash
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
python -m venv "$HOME/.venvs/bamenu"
"$HOME/.venvs/bamenu/bin/pip" install -r "$DIR/requirements.txt"
mkdir -p "$HOME/.local/bin"
printf '#!/usr/bin/env bash\nexec "%s/.venvs/bamenu/bin/python" "%s/bamenu.py" "$@"\n' "$HOME" "$DIR" > "$HOME/.local/bin/bamenu"
chmod +x "$HOME/.local/bin/bamenu"
