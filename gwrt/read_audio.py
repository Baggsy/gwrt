import pyaudio
import sounddevice as sd
import numpy as np
import wave


def get_list_of_audio_devices() -> None:
    p = pyaudio.PyAudio()

    for i in range(p.get_device_count()):
        info = p.get_device_info_by_index(i)
        device = info['index']
        print(f"Device {i}: {info['name']}")
        # print(f"Device index: {device}")

    p.terminate()
    read_audio(device)


def read_audio(device: int):
    device = device  # Replace with your device index
    samplerate = 44100  # Sample rate (Hz)
    channels = 1  # Number of audio channels
    duration = 10  # Duration to record (seconds)

    # Record audio
    print("Recording...")
    recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels, dtype=np.int16, device=device)
    sd.wait()  # Wait until recording is finished
    print("Finished recording.")

    # Save the recorded data as a WAV file
    output_filename = "output.wav"
    with wave.open(output_filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2)  # 16-bit audio
        wf.setframerate(samplerate)
        wf.writeframes(recording.tobytes())

    print(f"Saved recording to {output_filename}")