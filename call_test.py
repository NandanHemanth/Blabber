import whisper
import sounddevice as sd
import numpy as np
import threading

# Initialize Whisper model
model = whisper.load_model("base")

# Create a flag for recording state
recording = False

def record_audio():
    global recording
    recording = True
    fs = 44100  # Sample rate
    audio_data = []

    with sd.InputStream(callback=callback):
        print("Recording... Press 'Stop' to stop recording.")
        sd.sleep(5000)  # Record for 5 seconds initially

        while recording:
            sd.sleep(100)  # Continue recording in 0.1-second chunks

def stop_recording():
    global recording
    recording = False

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    if any(indata):
        audio_data.extend(indata)

# Create a separate thread for recording
record_thread = threading.Thread(target=record_audio)

# Start the recording thread
record_thread.start()

# Detect and decode language
def detect_and_decode():
    global audio_data

    # Cut the audio data to the desired length
    audio_data = np.array(audio_data, dtype=np.float32)
    audio_data = audio_data[:220500]  # Adjust the length as needed

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio_data).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    detected_language = max(probs, key=probs.get)
    print(f"Detected language: {detected_language}")

    # decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)

    # print the recognized text
    print(f"Recognized text: {result.text}")

# Create a GUI with Record and Stop buttons
import tkinter as tk

root = tk.Tk()
root.title("Whisper Speech Recognition")

record_button = tk.Button(root, text="Record", command=lambda: record_thread.start())
record_button.pack(pady=20)

stop_button = tk.Button(root, text="Stop Recording", command=stop_recording)
stop_button.pack()

detect_button = tk.Button(root, text="Detect and Decode", command=detect_and_decode)
detect_button.pack()

root.mainloop()
