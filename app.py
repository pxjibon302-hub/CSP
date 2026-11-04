import os
import traceback
from datetime import datetime

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window


Window.clearcolor = (0.025, 0.04, 0.09, 1)


def save_error(error_text):
    try:
        folder = os.path.expanduser("~")
        log_path = os.path.join(folder, "csp_error.log")

        with open(log_path, "a", encoding="utf-8") as file:
            file.write("\n" + "=" * 40 + "\n")
            file.write(str(datetime.now()) + "\n")
            file.write(error_text)
            file.write("\n")

    except Exception:
        pass


class CSPApp(App):

    def build(self):
        try:
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

            scroll = ScrollView()

            menu = BoxLayout(
                orientation="vertical",
                spacing=10,
                size_hint_y=None
            )

            menu.bind(minimum_height=menu.setter("height"))

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

            scroll.add_widget(menu)
            root.add_widget(scroll)

            footer = Label(
                text="CSP Security System | Version 1.0",
                size_hint_y=None,
                height=40,
                font_size=12
            )

            root.add_widget(footer)

            return root

        except Exception:
            save_error(traceback.format_exc())
            raise


if __name__ == "__main__":
    try:
        CSPApp().run()

    except Exception:
        save_error(traceback.format_exc())
        raise
