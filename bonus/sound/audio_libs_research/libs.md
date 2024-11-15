# Audio library research

## 1. **NumPy + SciPy**

- **Description**: While not specifically an audio library, NumPy (for array manipulation) and SciPy (for signal processing) together are powerful tools for generating waveforms, manipulating sound data, and saving it to audio files.
- **Example Usage**: Generate sine, square, or other complex waves, apply mathematical transformations, and save the output as WAV files using `scipy.io.wavfile`.
- **Pros**: Great control over the waveform; flexible for complex processing.
- **Cons**: You need to handle more low-level details, as it’s not designed specifically for audio.

## 2. **PyDub**

- **Description**: PyDub is primarily a library for manipulating audio files, but it allows low-level waveform creation and transformation.
- **Example Usage**: You can create basic waveforms (sine, square) and export them to WAV, MP3, etc.
- **Pros**: Simple API, easy to use for basic waveform generation.
- **Cons**: Not as detailed as other libraries for generating custom waveforms.

## 3. **wave (Standard Library)**

- **Description**: Python’s built-in `wave` library allows reading and writing WAV files, which is useful for handling waveform data directly.
- **Example Usage**: Write byte-level waveform data to a WAV file after generating it with libraries like NumPy.
- **Pros**: No external dependencies; works well for direct waveform manipulation.
- **Cons**: Limited to the WAV format and requires additional libraries (like NumPy) for waveform math.

## 4. **Soundfile**

- **Description**: `Soundfile` is a library that allows you to read and write sound files easily, with support for more formats than `wave`. It integrates well with NumPy arrays, which is ideal for custom waveform generation.
- **Example Usage**: Create waveforms in NumPy, then write to an audio file with `soundfile`.
- **Pros**: Easy to use with NumPy; supports many audio formats.
- **Cons**: Doesn't generate sounds directly—you need NumPy or another library for that.

## 5. **PyAudio** (in combination with NumPy)

- **Description**: PyAudio is a wrapper around PortAudio, providing low-level access to audio I/O. It’s useful for real-time audio playback and can be used to generate custom waveforms in real time.
- **Example Usage**: Generate waveform data in real-time using NumPy, then play it directly through the audio output.
- **Pros**: Allows real-time audio synthesis.
- **Cons**: Limited to playback and capture; requires other libraries for waveform generation.

## 6. **pyo**

- **Description**: `pyo` is a powerful library for audio synthesis, supporting complex audio operations and waveform generation.
- **Example Usage**: Generate custom waveforms using built-in generators (like `Sine`, `Square`, etc.), apply effects, and output to speakers or save to files.
- **Pros**: Designed for audio synthesis with high-level control.
- **Cons**: Larger library, more complex than some other options.

## 7. **wavebender**

- **Description**: This library focuses on waveform generation at the sample level, making it ideal for custom sound synthesis. It’s small and straightforward, designed for waveform synthesis.
- **Example Usage**: Generate sine waves, square waves, and complex waves, and output to a WAV file or stream.
- **Pros**: Focused on waveform-level control and sound synthesis.
- **Cons**: Limited documentation, minimal features beyond waveform generation.

## 8. **scipy.signal**

- **Description**: `scipy.signal` provides several waveform generators (like `sawtooth`, `square`, etc.) that are very useful for audio synthesis.
- **Example Usage**: Generate waveforms using NumPy and SciPy, process them, then export them with `scipy.io.wavfile` or other audio libraries.
- **Pros**: Flexible for signal processing and waveform creation.
- **Cons**: Primarily for signal processing, so you need to combine it with file handling tools.

Each of these libraries has its strengths, and many work well together! For example, combining **NumPy** (for waveform generation) with **Soundfile** (for audio file output) or **PyAudio** (for real-time playback) can provide a robust audio synthesis pipeline.
