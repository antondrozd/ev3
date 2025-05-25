from ev3_dc import Sound
from time import sleep

NOTE_FREQUENCIES: dict[str, float] = {
    # Fourth octave
    'C4': 261.63, 'C#4': 277.18, 'Db4': 277.18, 'D4': 293.66, 'D#4': 311.13, 'Eb4': 311.13,
    'E4': 329.63, 'Fb4': 329.63, 'E#4': 349.23, 'F4': 349.23, 'F#4': 369.99, 'Gb4': 369.99,
    'G4': 392.00, 'G#4': 415.30, 'Ab4': 415.30, 'A4': 440.00, 'A#4': 466.16, 'Bb4': 466.16,
    'B4': 493.88, 'Cb5': 493.88, 'B#4': 523.25,
    # Fifth octave
    'C5': 523.25, 'C#5': 554.37, 'Db5': 554.37, 'D5': 587.33, 'D#5': 622.25, 'Eb5': 622.25,
    'E5': 659.25, 'Fb5': 659.25, 'E#5': 698.46, 'F5': 698.46, 'F#5': 739.99, 'Gb5': 739.99,
    'G5': 783.99, 'G#5': 830.61, 'Ab5': 830.61, 'A5': 880.00, 'A#5': 932.33, 'Bb5': 932.33,
    'B5': 987.77, 'Cb6': 987.77, 'B#5': 1046.50
}

NOTE_LENGTHS: dict[str, float] = {
    'whole': 4.0,
    'whole_with_dot': 6.0,
    'half': 2.0,
    'half_with_dot': 3.0,
    'quarter': 1.0,
    'quarter_with_dot': 1.5,
    'eighth': 0.5,
    'eighth_with_dot': 0.75,
    'sixteenth': 0.25,
    'sixteenth_with_dot': 0.375
}

class TonePlayer:
    def __init__(self, ev3_sound: Sound):
        self.ev3_sound = ev3_sound

    def play_sequence(self, sequence: list[tuple[str, str]], volume: int = 30, tempo: int = 60):
        quarter_duration = 60 / tempo

        sleep(1)
        for note, length in sequence:
            duration = NOTE_LENGTHS[length] * quarter_duration
            if note == 'rest':
                sleep(duration)
            else:
                self.ev3_sound.tone(NOTE_FREQUENCIES[note], duration=duration, volume=volume)
                sleep(duration)