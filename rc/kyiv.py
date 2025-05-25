import tone_player

def play_kyiv(tone_player: tone_player.TonePlayer) -> None:
    notes = [
        ('Ab4', 'eighth'),
        ('Bb4', 'eighth'),
        ('C5', 'eighth'),
        ('Db5', 'eighth'),
        ('Eb5', 'eighth'),
        ('F5', 'quarter_with_dot'),
        ('Eb5', 'quarter'),
        ('F5', 'eighth'),
        ('Gb5', 'quarter_with_dot'),
        ('F5', 'quarter'),
        ('Eb5', 'eighth'),
        ('Bb4', 'quarter_with_dot'),
        ('rest', 'quarter_with_dot'),
        ('C5', 'quarter'),
        ('F4', 'eighth'),
        ('F4', 'eighth'),
        ('G4', 'eighth'),
        ('Ab4', 'eighth'),
        ('C5', 'quarter_with_dot'),
        ('Bb4', 'quarter_with_dot'),
        ('Ab4', 'quarter_with_dot'),
        ('E4', 'quarter'),
        ('G4', 'eighth'),
        ('F4', 'quarter_with_dot')
    ]
    
    tone_player.play_sequence(notes, tempo=90)