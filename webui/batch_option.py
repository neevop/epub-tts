import gradio as gr
from wording import get
from component_manager import register_component,get_component,update_component_value
from typing import Optional

SRT_PROCESSING_CHECKBOX: Optional[gr.Checkbox] = None
TXT_FILE_INPUT: Optional[gr.Files] = None


def render():
    global SRT_PROCESSING_CHECKBOX, TXT_FILE_INPUT

    with gr.Row():
        SRT_PROCESSING_CHECKBOX = gr.Checkbox(
            label=get('SrtProcessing'), value=True, visible=True, info=get('SrtProcessingInfo'), interactive=True
        )

    TXT_FILE_INPUT = gr.Files(
        label=get('TxtFileInputLabel'), 
        type="filepath", 
        file_types=['.txt','.srt', '.epub'], 
        interactive=True
    )

    register_component("srt_processing_checkbox", SRT_PROCESSING_CHECKBOX)
    register_component("txt_file_input", TXT_FILE_INPUT)

def listen():
    SRT_PROCESSING_CHECKBOX.change(lambda value: update_component_value("srt_processing_checkbox", value), inputs=SRT_PROCESSING_CHECKBOX, outputs=[])
    TXT_FILE_INPUT.change(lambda value: update_component_value("txt_file_input", value), inputs=TXT_FILE_INPUT, outputs=[])
