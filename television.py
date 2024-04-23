#https://github.com/mcasique725/Lab-12.git
class Television:

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        Method to set initial values
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        """
        Method to power tv on and off
        """
        self.__status = not self.__status

    def mute(self):
        """
        Method to mute tv
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        """
        Method to increase tv channel
        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        """
        Method to decrease tv channel
        """
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        """
        Method to increase volume of tv
        """
        if self.__status:
            self.__muted = False
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """
        Method to decrease tv volume
        """
        if self.__status:
            self.__muted = False
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """
        Method to show power, channel, and volume status of tv
        """
        if self.__muted:
            return f'Power {self.__status}, Channel {self.__channel}, Volume {Television.MIN_VOLUME}'
        else:
            return f'Power {self.__status}, Channel {self.__channel}, Volume {self.__volume}'
