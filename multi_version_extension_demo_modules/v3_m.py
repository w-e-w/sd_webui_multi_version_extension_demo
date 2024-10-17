from modules.ui_components import InputAccordion
from modules import scripts
from pathlib import Path
import gradio as gr


class V3M(scripts.Script):
    def title(self):
        return 'Demo V3 M'

    def show(self, is_img2img):
        return scripts.AlwaysVisible

    def ui(self, is_img2img):
        with InputAccordion(False, label=self.title()) as enable:
            md = gr.Markdown((Path(__file__).parent / 'message_template.md').read_text('utf-8').format(title=self.title()))

        enable.do_not_save_to_config = True
        md.do_not_save_to_config = True
