class TimeMap:

    def __init__(self):
        # Key: string
        # Value: list of [name, timestamp]
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        series = self.store.get(key, [])
        l = 0
        r = len(series) - 1
        res = ""

        while l <= r:
            mid = (l + r) >> 1
            if series[mid][1] == timestamp:
                return series[mid][0]
            elif series[mid][1] > timestamp:
                r = mid - 1
            elif series[mid][1] < timestamp:
                res = series[mid][0]
                l = mid + 1

        return res