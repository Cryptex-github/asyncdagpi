import json
from typing import Dict, Any, List, Optional


class BaseDagpiObject:

    """
    Base AsyncDagpi object

        .. container:: Attributes

            **Attributes**

            dict: :class:`Dict`
    """

    def __init__(self, dictionary: Dict[str, Any]):
        """
        Initialise a BaseDagpiObject
        """
        self.dict: Dict[str, Any] = dictionary

    def __str__(self) -> str:
        """
        Returns a string of the data
        :returns :class:`str`
        """
        return json.dumps(self.dict)

    def raw_data(self) -> Dict[str, Any]:
        """
        Dictionary with Raw Data
        :returns :class:`Dict`
        """
        return self.dict


class Logo(BaseDagpiObject):

    """
        A Dagpi Logo Object. A subclass of asyncdagpi.BaseDagpiObject

        .. container:: Attributes

            **Attributes**

            dict: :class:`Dict`
                Dictionary with raw data (same returned by raw_data)
            question: :class:`str`
                String containing url of question image
            answer: :class:`str`
                String containing url of answer image
            brand: :class:`str`
                String containing name of brand
            clue: :class:`str`
                String containing hint to use for question
            easy: :class:`boolean`
                Boolean that shows wether question was easy
            hint: :class:`str`
                String containing hint
            wiki_url: :class:`str`
                String containing Wikipedia URL for brand
        """

    def __init__(self, data: Dict[str, Any]):
        """
        Initialise a logo
        """
        super(Logo, self).__init__(data)
        self.dict: Dict[str, Any] = data
        self.question: str = data["question"]
        self.answer: str = data["answer"]
        self.brand: str = data["brand"]
        self.clue: Optional[str] = data.get("clue")
        self.easy: bool = data["easy"]
        self.hint: str = data["hint"]
        self.wiki_url: str = data["wiki_url"]


class PickupLine(BaseDagpiObject):

    """
    A Dagpi PickupLine

    .. container:: Attributes

        **Attributes**

        dict: :class:`Dict`
            Dictionary with raw data (same returned by raw_data)
        category: :class:`str`
            String containing Type of Pickup Line
        line: :class:`str`
            String Containing Pickup Line
    """

    def __init__(self, data: Dict[str, str]):
        super(PickupLine, self).__init__(data)
        self.dict: Dict[str, str] = data
        self.category: str = data["category"]
        self.line: str = data["joke"]


# class Pokemon(TypedDict):
#     abilities: List[str]
#     ascii: str
#     height: float
#     id: int
#     link: str
#     name: str
#     type: List[str]
#     weight: float


class WTP(BaseDagpiObject):

    """
           A Dagpi PickupLine. A subclass of AsyncDagpi object

           .. container:: Attributes

               **Attributes**

               dict: :class:`Dict`
                   Dictionary with raw data (same returned by raw_data)
               abilities: :class:`List[str]`
                   A list containing the abilities the pokemon has
               ascii: :class:`str`
                   String containing ascii data of pokemons image
               height: :class:`float`
                   Float with height of pokemon
               weight: :class:`float`
                   Float with weight of pokemon
               id: :class:`int`
                   Integer with national dex id of pokemon
               link: :class:`str`
                   String containing pokemondb link for pokemon
               name: :class:`str`
                   String containing name of pokemon
               answer: :class:`str`
                   String containing url for answer image
               question: :class:`str`
                   String containing url for question image
           """

    def __init__(self, data: Dict[str, Any]):
        super(WTP, self).__init__(data)
        mon: Dict[str, Any] = data["Data"]
        self.dict: Dict[str, Any] = data
        self.abilities: List[str] = mon["abilities"]
        self.ascii: str = mon["ascii"]
        self.height: float = mon["height"]
        self.id: int = int(mon["id"])
        self.link: str = mon["link"]
        self.name: str = mon["name"]
        self.type: List[str] = mon["Type"]
        self.weight: float = mon["weight"]
        self.question: str = data["question"]
        self.answer: str = data["answer"]


class Headline(BaseDagpiObject):

    """
    A Dagpi Headline

    .. container:: Attributes

        **Attributes**

        dict: :class:`Dict`
            Dictionary with raw data (same returned by raw_data)
        category: :class:`bool`
            Value stating whether headline is true or false
        headline: :class:`str`
            String Containing headline
    """

    def __init__(self, data: Dict[str, Any]):
        super(Headline, self).__init__(data)
        self.dict: Dict[str, Any] = data
        self.headline: str = data["text"]
        self.fake: bool = data["fake"]
