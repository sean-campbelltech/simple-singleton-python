from singleton_logger import SingletonLogger


def main():
    singletonLogger1 = SingletonLogger.get_instance()
    singletonLogger2 = SingletonLogger.get_instance()

    if singletonLogger1 is singletonLogger2:
        print("Same instance, singleton pattern correctly implemented")

    singletonLogger2.log("This is logged using a singleton logging system")


if __name__ == "__main__":
    main()
