class Flight:
    def __init__(self, upTime, downTime):
        self.upTime = upTime
        self.downTime = downTime

    def calculateFlight(self):
        hour1, start1 = [int(i) for i in self.upTime.split(":")]
        hour2, end1 = [int(i) for i in self.downTime.split(":")]
        return(hour2-hour1)*60 + (end1-start1)


if __name__ == '__main__':
    t1 = input()
    t2 = input()
    f1 = Flight(t1, t2)
    print(f1.calculateFlight())
