from textual.app import App, ComposeResult
from textual.containers import Container, Horizontal, VerticalScroll, Center
from textual.widgets import Static, Header, Placeholder

class ForgettingHouse(App):

    CSS_PATH = "style.tcss"

    def compose(self) -> ComposeResult:
        yield VerticalScroll(
            Container(
                Static("Something Mattered Here The Forgetting House", id="header"),
                Horizontal(
                    Placeholder("Fugue", id="fugue"),
                    Placeholder("Baseline", id="baseline"),
                    Placeholder("Focus", id="focus"),
                    id="c1"
                ), id="bot",
            )
        )
        yield Container(id="game-area")
        yield Container(id="card-area")
        yield Container(id="pillar-column")

if __name__ == "__main__":
    ForgettingHouse().run()
