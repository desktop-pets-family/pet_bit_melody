# 8bit note chart

## Full List of Notes and Their 8-bit Frequencies

| Note | Frequency (Hz) | 8-bit Scaled Value |
|------|----------------|--------------------|
| C0   | 16.35          | 31                |
| C#0  | 17.32          | 31                |
| D0   | 18.35          | 31                |
| D#0  | 19.45          | 31                |
| E0   | 20.60          | 31                |
| F0   | 21.83          | 31                |
| F#0  | 23.12          | 31                |
| G0   | 24.50          | 31                |
| G#0  | 25.96          | 31                |
| A0   | 27.50          | 31                |
| A#0  | 29.14          | 31                |
| B0   | 30.87          | 31                |
| C1   | 32.70          | 32                |
| C#1  | 34.65          | 35                |
| D1   | 36.71          | 37                |
| D#1  | 38.89          | 39                |
| E1   | 41.20          | 41                |
| F1   | 43.65          | 44                |
| F#1  | 46.25          | 46                |
| G1   | 49.00          | 49                |
| G#1  | 51.91          | 52                |
| A1   | 55.00          | 55                |
| A#1  | 58.27          | 58                |
| B1   | 61.74          | 62                |
| C2   | 65.41          | 65                |
| C#2  | 69.30          | 69                |
| D2   | 73.42          | 73                |
| D#2  | 77.78          | 78                |
| E2   | 82.41          | 82                |
| F2   | 87.31          | 87                |
| F#2  | 92.50          | 93                |
| G2   | 98.00          | 98                |
| G#2  | 103.83         | 104               |
| A2   | 110.00         | 110               |
| A#2  | 116.54         | 117               |
| B2   | 123.47         | 123               |
| C3   | 130.81         | 131               |
| C#3  | 138.59         | 139               |
| D3   | 146.83         | 147               |
| D#3  | 155.56         | 156               |
| E3   | 164.81         | 165               |
| F3   | 174.61         | 175               |
| F#3  | 185.00         | 185               |
| G3   | 196.00         | 196               |
| G#3  | 207.65         | 208               |
| A3   | 220.00         | 220               |
| A#3  | 233.08         | 233               |
| B3   | 246.94         | 247               |
| C4   | 261.63         | 255 (Clipped)     |
| C#4  | 277.18         | 255 (Clipped)     |
| D4   | 293.66         | 255 (Clipped)     |
| D#4  | 311.13         | 255 (Clipped)     |
| E4   | 329.63         | 255 (Clipped)     |
| F4   | 349.23         | 255 (Clipped)     |
| F#4  | 369.99         | 255 (Clipped)     |
| G4   | 392.00         | 255 (Clipped)     |
| G#4  | 415.30         | 255 (Clipped)     |
| A4   | 440.00         | 255 (Clipped)     |
| A#4  | 466.16         | 255 (Clipped)     |
| B4   | 493.88         | 255 (Clipped)     |

---

## Notes on 8-bit Scaling

1. **Clipping Above 255 Hz**: Frequencies above 255 Hz are clipped to the maximum value (255), as they exceed the range of 8-bit audio.
2. **Audible Range**: The practical audible range in an 8-bit context is roughly **31–255 Hz**. Frequencies below 31 Hz are typically inaudible or produce no noticeable sound.
3. **Representation**: This scaled mapping ensures that each note corresponds to an approximate 8-bit equivalent while preserving relative pitch.

Let me know if you'd like further explanations or adjustments!
