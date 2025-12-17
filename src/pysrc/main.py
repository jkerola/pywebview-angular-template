import webview
import logging
from watchdog import events, observers
from .api import Api
from importlib.resources import files

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s][%(name)s] %(message)s",
    datefmt="%Y/%m/%d %H:%M:%S",
)


class _DevEventHandler(events.FileSystemEventHandler):
    """Watchdog event handler for hot-reloading changes to the frontend."""

    window: webview.Window
    frontend_path: str

    def __init__(self, frontend_path: str):
        super().__init__()
        self.frontend_path = frontend_path
        self.window = webview.create_window(
            __name__,
            f"{self.frontend_path}/index.html",
            js_api=Api(),
        )

    def on_modified(self, event: events.FileSystemEvent) -> None:
        if event.src_path.startswith(self.frontend_path):
            self.window.load_url("index.html")
            self.window.load_css("styles.css")


def run(debug: bool = False, reload=False):
    """Run the application

    Args:
        debug (bool, optional): Enable the developer console. Defaults to False.
        reload (bool, optional): Enable hot-reloading of the frontend. Defaults to False.
    """
    base_path = files("dist").joinpath("frontend/browser")
    if reload:
        handler = _DevEventHandler(base_path)
        observer = observers.Observer()
        observer.schedule(handler, ".", recursive=True)
        observer.start()
    else:
        webview.create_window(
            __name__, str(base_path.joinpath("index.html")), js_api=Api()
        )
    webview.start(debug=debug)
