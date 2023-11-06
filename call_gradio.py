# Importing the Libraries
import gradio as gr
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Loading the models
nllb_model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")
tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M")

# Creating the pipeline for the models
transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-base.en")
translator = pipeline('translation', model=nllb_model, tokenizer=tokenizer, src_lang="eng_Latn", tgt_lang='hin_Deva')

def blabber(stream, new_chunk):
    sr, y = new_chunk
    y = y.astype(np.float32)
    y /= np.max(np.abs(y))

    if stream is not None:
        stream = np.concatenate([stream, y])
    else:
        stream = y
    return stream, translator(transcriber({"sampling_rate": sr, "raw": stream})["text"])


demo = gr.Interface(
    blabber,
    ["state", gr.Audio(sources=["microphone"], streaming=True)],
    ["state", "text"],
    live=True,
)

demo.launch(share=True)