# importing the NllB-200-distillled-600M dependencies
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, pipeline

# Loading the model
model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")
tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M")

# Creating the pipeline and translating from source to target language
translator = pipeline('translation', model=model, tokenizer=tokenizer, src_lang="tam_Taml", tgt_lang='eng_Latn', max_length = 400)

print(translator("திஸ் ஐஸ் எ வெரி குட் மாடல் "))

