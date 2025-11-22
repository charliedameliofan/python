class Television:
	"""Television with power, mute, channel and volume controls.

	Class attributes:
		MIN_VOLUME (int): Minimum volume level.
		MAX_VOLUME (int): Maximum volume level.
		MIN_CHANNEL (int): Minimum channel index.
		MAX_CHANNEL (int): Maximum channel index.

	Instance attributes (private):
		__status (bool): Power status (True if on).
		__muted (bool): Mute status.
		__volume (int): Current internal volume level.
		__channel (int): Current channel index.
	"""
	
	MIN_VOLUME: int = 0
	MAX_VOLUME: int = 2
	MIN_CHANNEL: int = 0
	MAX_CHANNEL: int = 3

	def __init__(self) -> None:
		"""Start the Television with default off state.

		The TV starts powered off, unmuted, with minimum volume and channel.
		"""
		self.__status: bool = False
		self.__muted: bool = False
		self.__volume: int = Television.MIN_VOLUME
		self.__channel: int = Television.MIN_CHANNEL

	def power(self) -> None:
		"""Toggle the power status of the TV.

		When called, this method flips the internal power state between on and off.
		"""
		self.__status = not self.__status

	def mute(self) -> None:
		"""Toggle mute when the TV is powered on.

		If the TV is off, this method does nothing. When toggled on, the
		internal volume is saved but `__muted` is set accordingly.
		"""
		if self.__status:
			self.__muted = not self.__muted

	def channel_up(self) -> None:
		"""Advance the channel by one, wrapping to `MIN_CHANNEL` from `MAX_CHANNEL`.

		Only has effect when the TV is powered on.
		"""
		if self.__status:
			if self.__channel == Television.MAX_CHANNEL:
				self.__channel = Television.MIN_CHANNEL
			else:
				self.__channel += 1

	def channel_down(self) -> None:
		"""Decrease the channel by one, wrapping to `MAX_CHANNEL` from `MIN_CHANNEL`.

		Only has effect when the TV is powered on.
		"""
		if self.__status:
			if self.__channel == Television.MIN_CHANNEL:
				self.__channel = Television.MAX_CHANNEL
			else:
				self.__channel -= 1

	def volume_up(self) -> None:
		"""Increase the volume by one step, up to `MAX_VOLUME`.

		If the TV is muted and powered on, unmute it and then adjust the
		internal volume. Has no effect when the TV is off.
		"""
		if self.__status:
			if self.__muted:
				self.__muted = False
			if self.__volume < Television.MAX_VOLUME:
				self.__volume += 1

	def volume_down(self) -> None:
		"""Decrease the volume by one step, down to `MIN_VOLUME`.

		If the TV is muted and powered on, unmute it and then adjust the
		internal volume. Has no effect when the TV is off.
		"""
		if self.__status:
			if self.__muted:
				self.__muted = False
			if self.__volume > Television.MIN_VOLUME:
				self.__volume -= 1

	def __str__(self) -> str:
		"""Return a human-readable representation of the TV state.

		When muted, the displayed volume is `0` even though the internal
		`__volume` value is saved.
		"""
		display_volume: int = 0 if self.__muted else self.__volume
		return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {display_volume}"

