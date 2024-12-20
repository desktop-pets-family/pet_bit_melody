##
# EPITECH PROJECT, 2024
# pet_bit_melody (Workspace)
# File description:
# main.py
##

# Piano map
DEFAULT_NOTE_MAP = {
    "C0": 16.35,
    "C#0": 17.32,
    "D0": 18.35,
    "Eb0": 19.45,
    "E0": 20.6,
    "F0": 21.83,
    "F#0": 23.12,
    "G0": 24.5,
    "Ab0": 25.96,
    "A0": 27.5,
    "Bb0": 29.14,
    "B0": 30.87,
    "C1": 32.7,
    "C#1": 34.65,
    "D1": 36.71,
    "Eb1": 38.89,
    "E1": 41.2,
    "F1": 43.65,
    "F#1": 46.25,
    "G1": 49,
    "Ab1": 51.91,
    "A1": 55,
    "Bb1": 58.27,
    "B1": 61.74,
    "C2": 65.41,
    "C#2": 69.3,
    "D2": 73.42,
    "Eb2": 77.78,
    "E2": 82.41,
    "F2": 87.31,
    "F#2": 92.5,
    "G2": 98,
    "Ab2": 103.83,
    "A2": 110,
    "Bb2": 116.54,
    "B2": 123.47,
    "C3": 130.81,
    "C#3": 138.59,
    "D3": 146.83,
    "Eb3": 155.56,
    "E3": 164.81,
    "F3": 174.61,
    "F#3": 185,
    "G3": 196,
    "Ab3": 207.65,
    "A3": 220,
    "Bb3": 233.08,
    "B3": 246.94,
    "C4": 261.63,
    "C#4": 277.18,
    "D4": 293.66,
    "Eb4": 311.13,
    "E4": 329.63,
    "F4": 349.23,
    "F#4": 369.99,
    "G4": 392,
    "Ab4": 415.3,
    "A4": 440,
    "Bb4": 466.16,
    "B4": 493.88,
    "C5": 523.25,
    "C#5": 554.37,
    "D5": 587.33,
    "Eb5": 622.25,
    "E5": 659.25,
    "F5": 698.46,
    "F#5": 739.99,
    "G5": 783.99,
    "Ab5": 830.61,
    "A5": 880,
    "Bb5": 932.33,
    "B5": 987.77,
    "C6": 1046.5,
    "C#6": 1108.73,
    "D6": 1174.66,
    "Eb6": 1244.51,
    "E6": 1318.51,
    "F6": 1396.91,
    "F#6": 1479.98,
    "G6": 1567.98,
    "Ab6": 1661.22,
    "A6": 1760,
    "Bb6": 1864.66,
    "B6": 1975.53,
    "C7": 2093,
    "C#7": 2217.46,
    "D7": 2349.32,
    "Eb7": 2489.02,
    "E7": 2637.02,
    "F7": 2793.83,
    "F#7": 2959.96,
    "G7": 3135.96,
    "Ab7": 3322.44,
    "A7": 3520,
    "Bb7": 3729.31,
    "B7": 3951.07,
    "C8": 4186.01,
    "C#8": 4434.92,
    "D8": 4698.63,
    "Eb8": 4978.03,
    "E8": 5274.04,
    "F8": 5587.65,
    "F#8": 5919.91,
    "G8": 6271.93,
    "Ab8": 6644.88,
    "A8": 7040,
    "Bb8": 7458.62,
    "B8": 7902.13
}


class PetBitMelody:
    def __init__(self, note_map: dict[str, int], success: int = 0, error: int = 84) -> None:
        self.note_map = note_map
        self.success = success
        self.error = error

    def play(self) -> int:
        """_summary_
        Play the music that was prepared to play.

        Returns:
            int: _description_: The status of the operation.
        """
        return self.success

    def demo(self) -> int:
        """_summary_
        Demo the PetBitMelody class.

        Returns:
            int: _description_: The status of the operation.
        """
        print(f"note_map: {self.note_map}")
        print(f"success: {self.success}")
        print(f"error: {self.error}")
        return self.success

    def main(self) -> int:
        """_summary_
        The main class of the program

        Returns:
            int: _description_: The status of the operation.
        """
        return self.success
