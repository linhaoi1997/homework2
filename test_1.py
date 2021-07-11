
class Test:
    def double_float(self, data, times=2):
        if isinstance(data, dict):
            for k in data.keys():
                data[k] = self.double_float(data[k], times)
        elif isinstance(data, list):
            data = [self.double_float(i, times) for i in data]
        else:
            try:
                data = float(data) * times
            except Exception as e:
                print(e)
        return data


if __name__ == '__main__':
    test = {
        "data1": {
            "h1": 192.33,
            "h2": "192.33",
        }, "data2": {
            "h3": 11,
            "h4": "ss",
        },
    }

    print(Test().double_float(test))