class State:
    def do(self):
        pass


class TurnedOff(State):
    @staticmethod
    def do(command):
        if command == 'TurnOn':
            state = TurnedOn
        else:
            state = Error
        return state


class TurnedOn(State):
    @staticmethod
    def do(command):
        if command == 'TurnOff':
            state = TurnedOff
        elif command == 'Open':
            state = Opening
        elif command == 'Close':
            state = Closing
        else:
            state = TurnedOn
        return state


class Closing(State):
    @staticmethod
    def do(command):
        if command == 'Close':
            state = Closed
        elif command == 'Open':
            state = Opening
        elif command == 'TurnOff':
            state = TurnedOff
        else:
            state = Closing
        return state


class Opening(State):
    @staticmethod
    def do(command):
        if command == 'Close':
            state = Closing
        elif command == 'Open':
            state = Opened
        elif command == 'TurnOff':
            state = TurnedOff
        else:
            state = Opening
        return state


class Closed(State):
    @staticmethod
    def do(command):
        if command == 'Close':
            state = Error
        elif command == 'Open':
            state = Opening
        elif command == 'TurnOff':
            state = TurnedOff
        else:
            state = Closed
        return state


class Opened(State):
    @staticmethod
    def do(command):
        if command == 'Open':
            state = Error
        elif command == 'Close':
            state = Closing
        elif command == 'TurnOff':
            state = TurnedOff
        else:
            state = Opened
        return state


class Error(State):
    @staticmethod
    def do(command):
        if command == 'Repair':
            state = TurnedOff
        else:
            state = Error
        return state


class Door:
    def __init__(self):
        self.state = TurnedOff

    def do(self, command):
        self.state = self.state.do(command)


door = Door()
print(door.state)
door.do('TurnOn')
print(door.state)
door.do('Open')
print(door.state)
door.do('Open')
door.do('Open')
print(door.state)
