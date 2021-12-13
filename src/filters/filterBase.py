from abc import abstractmethod
from typing import List


class FilterBase:
    def __init__(self):
        pass

    @abstractmethod
    def _isvalid(self):
        """
        Ensure the configuration for the filter is valid.
        Ensure all required fields are populated.
        :return: True is configuration is valid, else False
        """
        pass

    @abstractmethod
    def _compute(self, data):
        """
        Compute the filter on the data.
        :param data: Data to apply the filter on
        :return: None
        """
        pass

    @abstractmethod
    def apply(self, data: List):
        """
        Apply the current filter object to the data.
        :param data: Data to apply the filter on
        :return: Result of the applied calculation
        """
        pass


class LowpassFilter(FilterBase):
    def __init__(self):
        super().__init__()
        pass

    def __str__(self):
        return f"Low-Pass Filter"

    def _isvalid(self):
        pass

    def _compute(self, data):
        pass

    def apply(self, data: List):
        pass


class HighpassFilter(FilterBase):
    def __init__(self):
        super().__init__()
        pass

    def __str__(self):
        return f"High-pass filter"

    def _isvalid(self):
        pass

    def _compute(self, data):
        pass

    def apply(self, data: List):
        pass
