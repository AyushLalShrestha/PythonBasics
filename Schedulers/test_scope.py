

class Alerts:
    def __init__(self, alerts):
        self.alerts = alerts

    def add_alerts(self, ):
        self.alerts.extend([1, 2, 3])


alerts = []

alert = Alerts(alerts)
print alerts
alert.add_alerts()
print alerts

