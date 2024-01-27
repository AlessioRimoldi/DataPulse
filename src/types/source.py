from dataclasses import dataclass
from pandas import DataFrame

@dataclass
class Data():
    source: str
    data: DataFrame

@dataclass
class Plot():
    type: str
    obj: object