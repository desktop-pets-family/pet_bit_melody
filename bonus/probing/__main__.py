from .main import PetBitMelody, DEFAULT_NOTE_MAP

if __name__ == "__main__":
    ERR = 1
    ERROR = ERR
    SUCCESS = 0
    PBMI = PetBitMelody(
        note_map=DEFAULT_NOTE_MAP,
        success=SUCCESS,
        error=ERROR
    )
    PBMI.demo()
