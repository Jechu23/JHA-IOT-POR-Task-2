from event import data_event


class LocationEvents:

    def __init__(self):
        data_event.presence = 0

        while data_event.presence > 0:
            print(data_event.presence)
            if data_event.presence == 'True':
                print('User, in the room')
                break
    print(data_event.presence)










