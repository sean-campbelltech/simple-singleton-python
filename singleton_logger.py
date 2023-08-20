class SingletonLogger:
    _instance = None

    def __init__(self, private=False):
        if private is False:
            raise Exception(
                "This is a Singleton, use get_instance() to access the single instance."
            )

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = SingletonLogger(True)
        return cls._instance

    def log(self, ex: Exception):
        print(ex)

    def log(self, message: str):
        print(message)
