import csv
import math
from typing import List

index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                print(reader)
                dataset = [row for row in reader]
                print(dataset)
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Takes 2 args and returns the requested page number
        page: the requested page number
        page_size: number of records per page
        both params must be int and > 0
        """
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        data = self.dataset()

        try:
            idx = index_range(page, page_size)
            return data[idx[0]:idx[1]]
        except IndexError:
            return []
