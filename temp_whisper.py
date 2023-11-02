import whisper

model = whisper.load_model("small")
result = model.transcribe("./sample1.flac")
print(result["text"])