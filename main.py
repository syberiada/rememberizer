import pyaudio
import wave

obj = pyaudio.PyAudio()
num_devices = obj.get_device_count()
chosen = 0;
print(num_devices)

for dev in range(1,num_devices):
    # print("device# ", dev)
    # print(obj.get_device_info_by_host_api_device_index(0,dev)["name"])
    if "USB" in obj.get_device_info_by_host_api_device_index(0,dev)["name"]:
        chosen = dev

# print("selecting device",chosen)

chunk = 1024
fmt = pyaudio.paInt16
num_chans = 1
sps = 22050
record_seconds = 1
wav_file = "rec.wav"

stream = obj.open(format=fmt, rate=sps, channels=num_chans, input=True, frames_per_buffer=chunk, input_device_index=chosen)

frames = []

print("recording")
for i in range(int(sps/chunk*record_seconds)):
    data = stream.read(chunk)
    frames.append(data)

print("done recording")

stream.stop_stream()
stream.close()
obj.terminate
wav = wave.open(wav_file, 'wb')
wav.setnchannels(num_chans)
wav.setsamplewidth(obj.get_sample_size(fmt))
wav.setframerate(sps)
wav.writeframes(b''.join(frames))
wav.close()



