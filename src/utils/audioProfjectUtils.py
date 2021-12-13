import os
import numpy as np
from scipy.io import wavfile

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

    def read_wav_file(self, filename):
        """
        Reads the wavfile for filename
        :param filename: Name of the wav file to read
        :return: samples: sample_rate: int, num_channels: int
        """
        sample_rate, samples = wavfile.read(filename)
        num_channels = samples.shape[1]
        return samples, sample_rate, num_channels

    def write_wav_file(self, filename, sample_rate: int, data: np.ndarray):
        """
        Write data to wav file
        :param filename: Filename of the output file to write
        :param sample_rate: Samples/Sec of the data
        :param data: array of data to write to file
        :return: None
        """
        if os.path.exists(filename):
            print(f"{filename} already exists. Skipping write ...")
            return

        wavfile.write(filename, sample_rate, data)
