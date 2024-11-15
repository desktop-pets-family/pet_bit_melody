"""
https://soledadpenades.com/2009/10/29/fastest-way-to-generate-wav-files-in-python-using-the-wave-module/
"""
import random
import struct
import wave

SAMPLE_LEN = 1323000  # 30 seconds of random audio

noise_output = wave.open('noise2.wav', 'w')
noise_output.setparams((2, 2, 44100, 0, 'NONE', 'not compressed'))

values = []

for i in range(0, SAMPLE_LEN):
    value = random.randint(-32767, 32767)
    packed_value = struct.pack('h', value)
    values.append(packed_value)
    values.append(packed_value)

print("Values generated")

value_str = b''.join(values)
print("Values converted to string")
noise_output.writeframes(value_str)

noise_output.close()
