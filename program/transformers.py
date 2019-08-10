from program.constants import FeatureType, EncodeType


class Transformer(object):
    """
    Global class for transforming input columns into features ready for ML algorithms
    Provides methods like fit and transform so as to be compatible with sklearn library
    """

    def __init__(self, config):
        """
        Make an instance of this class
        :param config: list of dictionaries about which column should be encoded in what way
        """
        input_columns = list(filter(lambda x: x['type'] == FeatureType.INPUT.value, config))
        self.feat_dict = {}
        for encode_type in EncodeType:
            encode_columns = filter(lambda x: x['encode'] == encode_type.value, input_columns)
            self.feat_dict[encode_type.value] = list(encode_columns)
        self.feat_dict.pop(EncodeType.IGNORE.value, None)

    def fit(self, df):
        """

        :param df:
        :return:
        """
        return self

    def transform(self, df, y=None):
        """

        :param df:
        :param y:
        :return:
        """
        pass

    def fit_transform(self, df, y=None):
        """

        :param df:
        :param y:
        :return:
        """
        return self.fit(df).transform(df, y)

    def __del__(self):
        """

        :return:
        """
        pass
