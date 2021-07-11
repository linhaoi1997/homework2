import json


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
    # test = {
    #     "data1": {
    #         "h1": 192.33,
    #         "h2": "192.33",
    #     }, "data2": {
    #         "h3": 11,
    #         "h4": "ss",
    #     },
    # }
    #
    # print(Test().double_float(test))
    with open("./test.json") as f:
        print(f.read())


    "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=1NETEASEc822154d3c6b74d024e7c1e81a25db5f.7888237832.1626000037560.1626005030555&_s=63    b3e2&symbol=SH000001%2CSZ399001%2CSZ399006&extend=detail"
    "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t=1NETEASEc822154d3c6b74d024e7c1e81a25db5f.7888237832.1626000037560.1626005030844&_s=a1    7714&x=0.264&symbol=SH603026%2CDIDI%2CBABA&extend=detail"