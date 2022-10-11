class Person:
    def __init__(self, location, timestamp, presence, temperature):
        self.location = location
        self.timestamp = timestamp
        self.presence = presence
        self.temperature = temperature

    def __str__(self):
        return f'person ({self.presence}'

    @classmethod
    def even_presence(cls):
        return cls('Perth', '10:40pm', ['true', 'false'] ,'34c')

print(Person.even_presence())