from utility.debug import *
from utility.config import *

class AppConfig(BasicConfig):
    class about:
        program_name = 'Scheduler'
        version='0.0.1'
    class path:
        root = os.path.expanduser(f"~/.config/scheduler")
        config = "config.json"
        log = 'log'
    class variable:
        pass

class AppConfigManager(ConfigManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,config=AppConfig, **kwargs)

    def enable_debug(self):
        self.set('variable.wordbank', 'debug.db', save = False)
