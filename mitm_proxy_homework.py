import re
import json
from mitmproxy import http


class ModifyName:

    def response(self, flow: http.HTTPFlow):
        url = flow.request.pretty_url
        if "v5/stock/batch/quote.json" in flow.request.pretty_url:
            data = json.loads(flow.response.get_text())
            n = 1
            for i in data["data"]["items"]:
                i["quote"]["name"] = "冰镇西瓜" + str(n)
                n += 1
            flow.response.text = json.dumps(data)


class ModifyPercent:

    def response(self, flow: http.HTTPFlow):
        url = flow.request.pretty_url
        if "v5/stock/batch/quote.json" in flow.request.pretty_url:
            data = json.loads(flow.response.get_text())
            n = 0
            items = [0.0, 0.0000001, -0.0000001]
            for i in data["data"]["items"]:
                i["quote"]["percent"] = items[n]
                n += 1
            flow.response.text = json.dumps(data)


class DoubleFloat:

    @staticmethod
    def double(match_obj):
        return str(float(match_obj.group(1)) * 2)

    def response(self, flow: http.HTTPFlow):
        url = flow.request.pretty_url
        if "v5/stock/batch/quote.json" in flow.request.pretty_url:
            text = flow.response.get_text()
            text = re.sub("(\d+\.\d+)", self.double, text)
            flow.response.text = text


class DoubleFloat2:

    def response(self, flow: http.HTTPFlow):
        url = flow.request.pretty_url
        if "v5/stock/batch/quote.json" in flow.request.pretty_url:
            data = json.loads(flow.response.get_text())
            data = self.double_float(data)
            flow.response.text = json.dumps(data)

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
                pass
        return data


addons = [
    ModifyName(),
    ModifyPercent(),
    DoubleFloat()
]
