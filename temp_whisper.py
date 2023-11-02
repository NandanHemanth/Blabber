import whisper

model = whisper.load_model("base")
result = model.transcribe("./sample1.flac")
print(result["text"])