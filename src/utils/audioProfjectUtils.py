class APUtils:
    __instance = None

    def __init__(self):
        """ Virtually private constructor. """
        if APUtils.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            APUtils.__instance = self

    @staticmethod
    def instance():
        """ Static access method. """
        if APUtils.__instance is None:
            APUtils()
        return APUtils.__instance

    def sinWave(self, freq, samples):
        print("Generated a sin wave")
        pass