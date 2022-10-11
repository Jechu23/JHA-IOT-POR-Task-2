class Event:
    def __init__(self, location, timestamp, presence, temperature):
        self.location: str = location
        self.timeStamp: str = timestamp
        self.presence: bool = presence
        self.temperature: str = temperature

    def __str__(self):
        return f'The address is {self.location}, at {self.timeStamp}, {self.presence}, {self.temperature} '


data_event = Event('Perth', '10:00pm', 'TRUE', '34C')

print(data_event.__str__())


if __name__ == '__main__':
    #Create some events and inspect their outputs
    pass


