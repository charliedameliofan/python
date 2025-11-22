class Television:
	# Class constants
	MIN_VOLUME = 0
	MAX_VOLUME = 2
	MIN_CHANNEL = 0
	MAX_CHANNEL = 3

	def __init__(self):
		# Private instance variables
		self.__status = False
		self.__muted = False
		self.__volume = Television.MIN_VOLUME
		self.__channel = Television.MIN_CHANNEL

	def power(self):
		# Toggle power status
		self.__status = not self.__status

	def mute(self):
		# Only toggle mute when the TV is on
		if self.__status:
			self.__muted = not self.__muted

	def channel_up(self):
		# Only change channel when TV is on
		if self.__status:
			if self.__channel == Television.MAX_CHANNEL:
				self.__channel = Television.MIN_CHANNEL
			else:
				self.__channel += 1

	def channel_down(self):
		# Only change channel when TV is on
		if self.__status:
			if self.__channel == Television.MIN_CHANNEL:
				self.__channel = Television.MAX_CHANNEL
			else:
				self.__channel -= 1

	def volume_up(self):
		# Only change volume when TV is on
		if self.__status:
			# Unmute if muted, then adjust
			if self.__muted:
				self.__muted = False
			if self.__volume < Television.MAX_VOLUME:
				self.__volume += 1

	def volume_down(self):
		# Only change volume when TV is on
		if self.__status:
			# Unmute if muted, then adjust
			if self.__muted:
				self.__muted = False
			if self.__volume > Television.MIN_VOLUME:
				self.__volume -= 1

	def __str__(self):
		# When muted, display volume as 0 but keep internal volume
		display_volume = 0 if self.__muted else self.__volume
		return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {display_volume}"

