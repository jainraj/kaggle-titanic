from enum import Enum, unique


@unique
class FeatureType(Enum):
    INPUT = "input"
    TARGET = "target"


@unique
class EncodeType(Enum):
    IGNORE = "ignore"  # Ignore the column
    ONE_HOT = "one_hot"  # Use One-Hot encoding, after label encoding it
    CONTINUOUS = "continuous"  # Treat as continuous, standard scaling will be applied by default
