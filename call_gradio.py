import whisper 
import gradio as gr 
import time
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Loading the model
nllb_model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")
tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M")
whisper_model = whisper.load_model("base")

# Transctiption Function
def transcribe_translate(audio):

    #time.sleep(3)
    # Load the audio to the mdoel
    audio = whisper.load_audio(audio)

    # make log-mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(whisper_model.device)

    # detect the spoken language
    _, probs = whisper_model.detect_language(mel)
    detected_language = max(probs, key=probs.get)
    print(f"Detected language: {detected_language}")

    # decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(whisper_model, mel, options)

    # Creating the pipeline and translating from source to target language
    translator = pipeline('translation', model=nllb_model, tokenizer=tokenizer, src_lang="eng_Latn", tgt_lang='hin_Deva')

    return translator(result.text)

# Calling the transcribe function with Gradio Interface
gr.Interface(
    title='Real-time AI-based Audio Transcription, Recognition and Translation Web App',
    fn=transcribe_translate,
    inputs=[
        gr.inputs.Audio(source="microphone", type="file")
    ],
    outputs="text",
    live=True
).launch()


