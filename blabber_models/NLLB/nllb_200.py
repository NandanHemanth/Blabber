# importing the NllB-200-distillled-600M dependencies
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Loading the model
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")
tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M")

# Creating the pipeline and translating from source to target language
translator = pipeline('translation', model=model, tokenizer=tokenizer, src_lang="eng_Latn", tgt_lang='hin_Deva')

print(translator("Once upon a time, in a land far far away, there lived a king with a favourite number 11. He loved Artificial-Intelligence"))

