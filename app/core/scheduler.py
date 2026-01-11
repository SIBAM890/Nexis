from apscheduler.schedulers.background import BackgroundScheduler
from app.core.orchestrator import OSINTOrchestrator


class OSINTScheduler:
    def __init__(self):
        self.scheduler = BackgroundScheduler()
        self.orchestrator = OSINTOrchestrator()

    def start(self, target):
        self.scheduler.add_job(
            lambda: self.orchestrator.run_scan(target),
            trigger="interval",
            seconds=300
        )
        self.scheduler.start()