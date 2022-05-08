class Time:
    def print_time(self):
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second)))
    
    def time_to_int(self):
        return (self.hour * 60 * 60) + (self.minute * 60) + (self.second)

    def int_to_time(seconds):
        time = Time()
        time.second = seconds%60
        time.minute = (seconds // 60) % 60
        time.hour = (seconds // (60 * 60)) % 24
        return time

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def print(self):
        print('%.2f %.2f' % (self.x, self.y))

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __radd__(self, other):
        return self.__add__(Point(*other))
    