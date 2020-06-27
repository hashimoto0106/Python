#関数のコメント
def get_fruit_price(fruit_id, location_id):
    """
    果物の値段を取得する。

    Parameters
    ----------
    fruit_id : int
        対象の果物のマスタID。
    location_id : int
        対象地域のマスタID。

    Returns
    -------
    fruit_price : int
        対象の果物の値段。
    consumption_tax : int
        消費税値。
    """
    # ...関数内容省略。
    return fruit_price, consumption_tax

#クラスのコメント
class Fruit(object):
    """
    果物の各属性値やヘルパー関数を保持する。

    Attributes
    ----------
    fruit_id : int
        対象の果物のマスタID。
    fruit_name : str
        果物名。
    price_dict : dict
        キーに地域のID、値に該当する地域での値段を保持した辞書。
    """

    def __init__(self, fruit_id):
        """
        Parameters
        ----------
        fruit_id : int
            対象の果物のマスタID。
        """
        self.fruit_id = fruit_id
        self.fruit_name = self.get_fruit_name(fruit_id=fruit_id)
        self.price_dict = self.get_price_dict(fruit_id=fruit_id)

    def get_fruit_name(self, fruit_id):
        # ...内容省略。
        pass

    def get_price_dict(self, fruit_id):
        # ...内容省略。
        pass
