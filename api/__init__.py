import requests
import traceback
from config import logging, LOGGER_CONFIG
from models import XRate, ApiLog, ErrorLog, peewee_datetime

fh = logging.FileHandler(LOGGER_CONFIG["file"])
fh.setLevel(LOGGER_CONFIG["level"])
fh.setFormatter(LOGGER_CONFIG["formatter"])


class _Api:
    def __init__(self, logger_name):
        self.log = logging.getLogger(logger_name)
        self.log.addHandler(fh)
        self.log.setLevel(LOGGER_CONFIG["level"])

    def updata_rate(self, from_currency, to_currency):
        self.log.info("Start update for %s=>%s" % (from_currency, to_currency))
        xrate = XRate.select().where(XRate.from_currency == from_currency,
                                     XRate.to_currency == to_currency).first()
        self.log.debug("rate before: %s", xrate)
        xrate.rate = self._updata_rate(xrate)
        xrate.updated = peewee_datetime.datetime.now()
        xrate.save()

        self.log.debug("rate after: %s", xrate)
        self.log.info("Finished update for: %s=>%s" % (from_currency, to_currency))

    def _updata_rate(self, xrate):
        raise NotImplementedError("_updata_rate")

    def _send(self, url, method, data=None, headers=None):
        return requests.request(url=url, method=method, headers=headers, data=data, timeout=15)

    def _send_request(self, url, method, data=None, headers=None):
        log = ApiLog(request_url=url, request_data=data, request_method=method, request_headers=headers)
        try:
            response = self._send(url=url, method=method, data=data, headers=headers)
            log.response_text = response.text
            return response
        except Exception as ex:
            self.log.exception("Error during request sending")
            log.error = str(ex)
            ErrorLog.create(request_data=data, request_url=url, request_method=method, error=str(ex),
                            traceback=traceback.format_exc(chain=False))
            raise
        finally:
            log.finished = peewee_datetime.datetime.now()
            log.save()
