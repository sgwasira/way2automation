import configparser

config = configparser.RawConfigParser()
config.read("./Configurations/UrlDetails.ini")


class ReadLoginConfig():
    def getway2automationURL(self):
        return config.get("URLS", "way2automationURL")

    def getClientNameTest01(self):
        return config.get("URLS", "clientNameTest01")

    def getClientNameTest02(self):
        return config.get("URLS", "clientNameTest02")
