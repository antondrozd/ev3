import ev3_dc
import curses
import time
from env import EV3MAC
from kyiv import play_kyiv
from tone_player import TonePlayer

def main(stdscr) -> None:
    speed: int = 100  # percent speed

    stdscr.nodelay(True)
    stdscr.keypad(True)
    curses.cbreak()
    stdscr.timeout(100)  # 100 ms timeout for getch()

    with ev3_dc.EV3(protocol=ev3_dc.BLUETOOTH, host=EV3MAC) as ev3:
        vehicle: ev3_dc.TwoWheelVehicle = ev3_dc.TwoWheelVehicle(
            0.01518,       # radius_wheel (meters)
            0.11495,       # tread (meters)
            ev3_obj=ev3,
            port_left=ev3_dc.PORT_B,
            port_right=ev3_dc.PORT_C)
        sound: ev3_dc.Sound = ev3_dc.Sound(ev3_obj=ev3)
        tone_player = TonePlayer(ev3_sound=sound)

        sound.tone(440, duration=0.3, volume=30)
            
        last_command: tuple[str, int, int] | None = None  # track last command to avoid repeats
        
        try:
            while True:
                key: int = stdscr.getch()

                if key == -1:
                    command: tuple[str, int, int] = ('stop', 0, 0)
                else:
                    if key == ord('w'):
                        command = ('move', speed, 0)
                    elif key == ord('s'):
                        command = ('move', -speed, 0)
                    elif key == ord('a'):
                        command = ('move', 30, speed)
                    elif key == ord('d'):
                        command = ('move', 30, -speed)
                    elif key == ord('k'):
                        play_kyiv(tone_player)
                    elif key == ord(' '):
                        tone_player.play('A4', 'eighth')
                    else:
                        command = ('stop', 0, 0)

                # Only send a new command if different from last command
                if command != last_command:
                    if command[0] == 'move':
                        vehicle.move(command[1], command[2])
                    else:
                        vehicle.stop()
                    last_command = command

                time.sleep(0.01)

        except KeyboardInterrupt:
            vehicle.stop()

if __name__ == "__main__":
    curses.wrapper(main)

