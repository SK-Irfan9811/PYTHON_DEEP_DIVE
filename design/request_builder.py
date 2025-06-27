class RequestBuilder:
    def __init__(self):
        self.meth = "GET"
        self.url = ""
        self.header = ""
        self.body = ""

    def set_method(self, method):
        self.meth = method
        return self

    def set_url(self, url):
        self.url = url
        return self

    def build(self):
        return "request built"


r = RequestBuilder().set_method("DFFF").set_method("POST").build()
print(r)