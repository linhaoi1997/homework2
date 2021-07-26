"""
for graphql view query
"""
import json
import re

from mitmproxy import contentviews
from mitmproxy.contentviews import views
from .auto_select import ViewAuto
from beeprint import pp


def double_space(match_obj):
    return match_obj.group(1) * 2


class ViewGraphqlQuery(contentviews.View):
    """查看graphql的query"""
    name = "GraphqlQuery"
    content_types = ["text/plain"]

    def __call__(self, data, **metadata) -> contentviews.TViewResult:
        query = json.loads(data).get("query")
        query = re.sub("( +)", double_space, query)

        return "graphql query", contentviews.format_text(query)


class ViewGraphqlVariables(contentviews.View):
    """查看graphql的varibales"""
    name = "GraphqlVariables"
    content_types = ["text/plain"]

    def __call__(self, data, **metadata) -> contentviews.TViewResult:
        query = json.loads(data).get("query").split("\n")[0].rstrip(" {")
        variables = pp(json.loads(data).get("variables"), output=False)

        def result():
            yield from contentviews.format_text(query)
            yield from contentviews.format_text("variables: \n")
            yield from contentviews.format_text(variables)

        return "graphql variables", result()


class ViewJsonString(contentviews.View):
    """查看graphql的varibales"""
    name = "JsonString"
    content_types = ["text/plain"]

    def __call__(self, data, **metadata) -> contentviews.TViewResult:
        data = json.loads(data)

        def dfs(datas: dict):
            for key, value in datas.items():
                if isinstance(value, str):
                    try:
                        datas[key] = json.loads(value)
                    except:
                        pass
                elif isinstance(value, dict):
                    dfs(value)

        dfs(data)
        return "json_string", contentviews.format_dict(data)


view = ViewGraphqlQuery()
view2 = ViewGraphqlVariables()


# view3 = ViewJsonString()


def load(l):
    views[0] = ViewAuto()
    contentviews.add(view)
    contentviews.add(view2)
    # contentviews.add(view3)


def done():
    contentviews.remove(view)
    contentviews.remove(view2)
    # contentviews.remove(view3)
