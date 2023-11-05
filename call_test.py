# Importing Whisper Dependencies
import Whisper

# Importing NLLB-200-distilled-600M dependencies
import torch 
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Loading the Whisper model
whisper_model = load.model("base")

# Loading the NLLB-200-distilled-600M model
nllb_model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")
nllb_modeltokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M")