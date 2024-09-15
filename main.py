import time
import sys
import numpy as np
import sounddevice as sd



def generate_sine_wave(frequency, duration, sample_rate=44100):
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    return np.sin(frequency * t * 2 * np.pi)

def play_beep(frequency, duration):
    samples = generate_sine_wave(frequency, duration)
    sd.play(samples, samplerate=44100)
    sd.wait()


def metronome(bpm, beats_per_measure):
    global running
    interval = 60 / bpm
    counter = 0

    try:
        while True:
            counter += 1
            if counter == 1:
                play_beep(1000, 0.1)
            else:
                play_beep(800, 0.1)
            time.sleep(interval)
            if counter == beats_per_measure:
                counter = 0

    except KeyboardInterrupt:
        print("\nMetronome stopped.")

def main():
    if len(sys.argv) == 3:
        try:
            bpm = int(sys.argv[1])
            beats_per_measure = int(sys.argv[2])
        except ValueError:
            print("Error: BPM and beats per measure must be integers")
            sys.exit(1)
    else:
        try:
            bpm = int(input("Enter bpm (40-208): "))
            if not 40 <= bpm <= 208:
                raise ValueError("BPM must be between 40 and 208")

            beats_per_measure = int(input("Enter beats per measure (1-12): "))
            if not 1 <= beats_per_measure <= 12:
                raise ValueError("Beats per emasure must be between 1 and 12")

            metronome(bpm, beats_per_measure)
        except ValueError as e:
            print(f"Error {e}")
            sys.exit(1)



if __name__ == "__main__":
    main()
