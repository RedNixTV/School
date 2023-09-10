import time
import pygame
import threading

class TimerAlert:
	def __init__(self, alert_interval_minutes, sound_file_path):
		self.alert_interval_minutes = alert_interval_minutes
		self.sound_file_path = sound_file_path
		self.paused = False
		self.playing_thread = None
		self.paused_time = 0  # Initialize paused_time to 0

	def start(self):
		pygame.init()
		print("Timer program is running. Press Ctrl+C to stop.")
		try:
			while True:
				self.countdown(self.alert_interval_minutes * 60)
				self.alert_user()
		except KeyboardInterrupt:
			self.stop_alert_sound()
			print("\nTimer program stopped.")

	def countdown(self, seconds):
		for remaining in range(seconds, 0, -1):
			mins, secs = divmod(remaining, 60)
			print(f"Next alert in {mins:02d}:{secs:02d}", end='\r')
			time.sleep(1)
		print(" " * len("Next alert in 00:00"), end='\r')  # Clear the countdown message

	def alert_user(self):
		print(f"{self.alert_interval_minutes} minutes have passed!")
		self.play_alert_sound()

	def play_alert_sound(self):
		if self.playing_thread and self.playing_thread.is_alive():
			self.paused_time = pygame.mixer.music.get_pos() / 1000 # Get current position in seconds
			pygame.mixer.music.stop()
			self.playing_thread.join()

		self.playing_thread = threading.Thread(target=self._play_sound)
		self.playing_thread.start()

	def _play_sound(self):
		pygame.mixer.init()
		pygame.mixer.music.load(self.sound_file_path)
		pygame.mixer.music.play(start=self.paused_time)
		time.sleep(15) # Play for 15 seconds
		self.paused_time = pygame.mixer.music.get_pos() / 1000  # Save the position where MP3 left off
		pygame.mixer.music.pause()
		self.paused = False
		time.sleep(0.1)

def stop_alert_sound(self):
	if self.playing_thread and self.playing_thread.is_alive():
		pygame.mixer.music.stop()

if __name__ == "__main__":
    sound_file = '/Users/enriquereyes/Desktop/Personal/taskManagement/alert.mp3'  
    # Test audio playback for 5 seconds
    print("Testing audio playback for 5 seconds...")
    pygame.mixer.init()
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    time.sleep(5)
    pygame.mixer.music.stop()
    print("Audio test complete.")
    
    # Start the timer program
    alert_interval = 10  # Adjust as needed
    timer = TimerAlert(alert_interval, sound_file)
    timer.start()
