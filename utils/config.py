class Config:
    DEFAULT_SETTINGS = {
        "agent_name": "Arxen",
        "logging": True
    }

    @staticmethod
    def get_config():
        return Config.DEFAULT_SETTINGS
