
class TestDataEmptyArray:
    @staticmethod
    def get_array():
        return []


class TestDataUniqueValues:
    @staticmethod
    def get_array():
        return [5, 3, 8, 1, 7]

    @staticmethod
    def get_expected_result():
        return 3


class TestDataExactlyTwoDifferentMinimums:
    @staticmethod
    def get_array():
        return [5, 1, 3, 1, 7]

    @staticmethod
    def get_expected_result():
        return 1
