from filters import HighpassFilter, LowpassFilter
from utils import APUtils

lpf = LowpassFilter()
print(lpf)

hpf = HighpassFilter()
print(hpf)

utils = APUtils()

utils.sinWave(1, 2)
