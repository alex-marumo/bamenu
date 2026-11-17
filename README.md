# bamenu

A terminal UI for browsing BlackArch tools by category. Pick a category on the left, browse its tools on the right, and install with one key.

## Requirements

- Arch Linux with the BlackArch repository enabled
- `expac` (`sudo pacman -S expac`)
- Python 3 with `venv`
- `sudo` access, used only when you install a tool

## Install

```
git clone https://github.com/alex-marumo/bamenu.git
cd bamenu
sudo pacman -S expac
./install.sh
```

`install.sh` creates a venv at `~/.venvs/bamenu`, installs Textual into it, and writes a `bamenu` launcher to `~/.local/bin`. Make sure `~/.local/bin` is on your PATH.

## Usage

Run `bamenu` from any directory.

| Key | Action |
|-----|--------|
| Up / Down | Move through the list |
| Tab | Switch between the category and tool panes |
| i | Install the highlighted tool (`sudo pacman -S`) |
| q | Quit |

## How it works

On startup, `expac` dumps the group, name, version and description of every package in a single call. The tool filters for groups starting with `blackarch-` and builds the menu from that, so browsing does not spawn a process per item.

## Troubleshooting

- `bamenu: command not found`: `~/.local/bin` is not on your PATH.
- Empty category list: the BlackArch repo is not enabled, or `expac` is not installed.
- Textual traceback: Textual's API changes between versions. Open an issue with the traceback and your `pip show textual` version.
