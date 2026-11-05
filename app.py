import os
import sys
import traceback
from datetime import datetime

from kivy.app import App
from kivy.logger import Logger
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window


LOG_PATH = None


def save_log(message):
    global LOG_PATH

    try:
        if LOG_PATH:
            with open(LOG_PATH, "a", encoding="utf-8") as file:
                file.write(
                    f"\n[{datetime.now()}] {message}\n"
                )
    except Exception:
        pass


def save_error(error):
    save_log("ERROR:\n" + str(error))


def handle_exception(exc_type, exc_value, exc_traceback):
    error_text = "".join(
        traceback.format_exception(
            exc_type, exc_value, exc_traceback
        )
    )

    save_error(error_text)


sys.excepthook = handle_exception


Window.clearcolor = (0.025, 0.04, 0.09, 1)


class CSPApp(App):

    def build(self):
        global LOG_PATH

        try:
            LOG_PATH = os.path.join(
                self.user_data_dir,
                "csp_diagnostic.log"
            )

            os.makedirs(self.user_data_dir, exist_ok=True)

            save_log("CSP application started")
            save_log("Building user interface")

            root = BoxLayout(
                orientation="vertical",
                padding=15,
                spacing=12
            )

            title = Label(
                text="[b]CSP[/b]\nCyber Security Platform",
                markup=True,
                font_size=27,
                size_hint_y=None,
                height=100
            )

            root.add_widget(title)
            save_log("Title created")

            scroll = ScrollView()

            menu = BoxLayout(
                orientation="vertical",
                spacing=10,
                size_hint_y=None
            )

            menu.bind(
                minimum_height=menu.setter("height")
            )

            modules = [
                "System Information",
                "Password Security Test",
                "Network Analyzer",
                "Security Scanner",
                "Security Report",
                "File Integrity Checker",
                "Security Log System"
            ]

            for name in modules:
                btn = Button(
                    text=name,
                    font_size=17,
                    size_hint_y=None,
                    height=65,
                    background_normal="",
                    background_color=(0.08, 0.20, 0.38, 1)
                )

                menu.add_widget(btn)
                save_log("Button created: " + name)

            scroll.add_widget(menu)
            root.add_widget(scroll)

            footer = Label(
                text="CSP Security System | Diagnostic Version",
                size_hint_y=None,
                height=40,
                font_size=12
            )

            root.add_widget(footer)

            save_log("User interface built successfully")

            return root

        except Exception:
            save_error(traceback.format_exc())
            raise

    def on_start(self):
        save_log("CSP application started successfully")

    def on_stop(self):
        save_log("CSP application stopped")


if __name__ == "__main__":
    try:
        CSPApp().run()

    except Exception:
        save_error(traceback.format_exc())
        raise
