class Mail(object):
    def __init__(self, address, msg, forecast, from_address):
        self.address = address
        self.msg = msg
        self.forecast = forecast
        self.from_address = from_address

    def __repr__(self):
        return "Mail:  " + self.address + " " + self.msg + " " + self.forecast + " " + self.from_address

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

