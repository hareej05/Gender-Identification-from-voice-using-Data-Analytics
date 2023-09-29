"""Record a few seconds of audio and save to a WAVE file."""
import os
import time
import wave

import pyaudio

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 20
WAVE_OUTPUT_FILENAME = 'output.wav'

if not os.path.exists('sounds'):
    os.makedirs('sounds')


def run(root, tk, output_text_area):
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    output_text_area.delete(1.0, tk.END)
    output_text_area.insert(1.0, 'Speak for 20 secs\n\n')
    root.update_idletasks()

    output_text_area.insert(3.0, 'READ NOW!\n')
    output_text_area.insert(5.0, 'My biggest mistake was attempting to stifle my laughter in a library. It came out as a loud snort, one that '
          'would make the largest pig proud. The librarian quietly shuffled over. She slid her glasses down her nose. I'
          ' could see the rage glowing in her muddy brown eyes. She mumbled a few words at me and then jabbed her bony '
          'finger at the center of her glasses, returning them to the bridge of her nose. She turned away, clicking her'
          ' tongue against the roof of her mouth. I could swear I saw a smirk crinkle at the corner of her mouth.\n\n')
    root.update_idletasks()
    time.sleep(.5)

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    output_text_area.insert(7.0, 'Recording Saved.\n\n')
    root.update_idletasks()
    stream.stop_stream()
    stream.close()

    p.terminate()

    wf = wave.open('sounds/' + WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()


if __name__ == '__main__':
    run()
