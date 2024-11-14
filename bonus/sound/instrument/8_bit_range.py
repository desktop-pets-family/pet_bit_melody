from typing import List
import math
import struct
import wave


def generate_8_bit_range() -> List[int]:
    """Generate an 8-bit frequency range offset by 128.

    Returns:
        List[int]: The list of frequencies for the 8-bit range.
    """
    generated_frequency_range = []
    the_8_bit_offset_value = 128
    for frequency in range(0, 256):
        generated_frequency_range.append(frequency + the_8_bit_offset_value)
    return generated_frequency_range


# Parameters
SAMPLE_LEN = 132300    # Total number of samples for the tone duration
SAMPLE_RATE = 44100    # Sampling rate (Hz)
# Maximum amplitude for 8-bit audio (using 127 for 8-bit values)
AMPLITUDE = 127

# Create a .wav file
output_file = wave.open('8_bit_tones.wav', 'w')
output_file.setparams((2, 1, SAMPLE_RATE, 0, 'NONE',
                      'not compressed'))  # 8-bit, mono

# Define the frequency range for the tones
frequency_range = generate_8_bit_range()
NUM_FREQUENCIES = len(frequency_range)

if NUM_FREQUENCIES == 0:
    output_file.close()
    raise ValueError("Frequency range is empty.\nNo sound generated.")

if SAMPLE_LEN == 0:
    output_file.close()
    raise ValueError("File duration is 0.\nNo sound generated.")

# Calculate the interval to increment the counter
increment_interval = SAMPLE_LEN // NUM_FREQUENCIES

# Generate samples
values = []
COUNTER = 0
for i in range(SAMPLE_LEN):
    # msg = f"frequency_range: {frequency_range} COUNTER: {COUNTER}"
    msg = f"i: {i}, frequency_range[{COUNTER}]: {frequency_range[COUNTER]}"
    # Calculate the sine wave value for 8-bit audio (0-255 range)
    sample = int(AMPLITUDE * math.sin(2 * math.pi *
                 frequency_range[COUNTER] * i / SAMPLE_RATE) + 128)
    msg += f" sample: {sample}"
    print(msg)
    # Pack the sample as unsigned 8-bit
    packed_sample = struct.pack('B', sample)
    values.append(packed_sample)

    # Increment the COUNTER at equal intervals
    if i % increment_interval == 0 and COUNTER < NUM_FREQUENCIES - 1:
        COUNTER += 1

# Write the frames to the .wav file
output_file.writeframes(b''.join(values))

output_file.close()
print("8-bit tones generated successfully.")
