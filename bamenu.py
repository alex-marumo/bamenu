#!/usr/bin/env python3
import subprocess
from collections import defaultdict
from textual.app import App
from textual.widgets import OptionList, Static, Footer
from textual.containers import Horizontal

def load():
    out = subprocess.run(["expac", "-S", "%G\t%n\t%v\t%d"],
                         capture_output=True, text=True).stdout
    cats = defaultdict(list)
    for line in out.splitlines():
        g, n, v, d = line.split("\t", 3)
        for grp in g.split():
            if grp.startswith("blackarch-"):
                cats[grp].append((n, v, d))
    return {k: sorted(v) for k, v in sorted(cats.items())}

class BA(App):
    CSS = "Horizontal { height: 1fr; } #info { height: 4; padding: 0 1; }"
    BINDINGS = [("q", "quit", "Quit"), ("i", "install", "Install"),
                ("tab", "focus_next", "Switch pane")]

    def __init__(self):
        super().__init__()
        self.cats = load()
        self.cur = None

    def compose(self):
        with Horizontal():
            yield OptionList(*self.cats, id="cats")
            yield OptionList(id="tools")
        yield Static(id="info")
        yield Footer()

    def on_option_list_option_highlighted(self, e):
        if e.option_list.id == "cats":
            self.cur = str(e.option.prompt)
            t = self.query_one("#tools", OptionList)
            t.clear_options()
            t.add_options([n for n, _, _ in self.cats[self.cur]])
        elif self.cur:
            n, v, d = self.cats[self.cur][e.option_index]
            self.query_one("#info", Static).update(f"{n} {v}\n{d}")

    def action_install(self):
        t = self.query_one("#tools", OptionList)
        if t.highlighted is None:
            return
        name = self.cats[self.cur][t.highlighted][0]
        with self.suspend():
            subprocess.run(["sudo", "pacman", "-S", name])

BA().run()
