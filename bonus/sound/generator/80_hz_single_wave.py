import math
import struct
import wave

# Parameters
SAMPLE_LEN = 132300    # Total number of samples for the tone duration
SAMPLE_RATE = 44100    # Sampling rate (Hz)
FREQUENCY = 80         # Frequency of the tone (Hz)
AMPLITUDE = 32767      # Maximum amplitude for 16-bit audio

# Create a .wav file
output_file = wave.open('tone_80hz.wav', 'w')
output_file.setparams((2, 2, SAMPLE_RATE, 0, 'NONE', 'not compressed'))

# Generate samples for 80 Hz sine wave
values = []
for i in range(SAMPLE_LEN):
    # Calculate the sine wave value
    sample = int(AMPLITUDE * math.sin(2 * math.pi *
                 FREQUENCY * i / SAMPLE_RATE))
    # Pack and append the sample value for stereo channels
    packed_sample = struct.pack('h', sample)
    values.append(packed_sample)
    values.append(packed_sample)

# Write the frames to the .wav file
output_file.writeframes(b''.join(values))

output_file.close()
print("80 Hz tone generated successfully.")
