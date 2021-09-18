class IceCream():
    "The Ice Cream Product"
    def __init__(self,
                flavor='',
                ingredients=[],
                pasteurization_level=0,
                homogenization_level=0,
                creaming_level=0):

        self.flavor = flavor
        self.ingredients = ingredients
        self.pasteurization_level = pasteurization_level
        self.homogenization_level = homogenization_level
        self.creaming_level = creaming_level

    def specification_as_dict(self):
        return self.__dict__

class Company:
    "The class to build a ice cream"

    @staticmethod
    def deliver(client_requirements)->IceCream:
        "Builds and  returns the final product"
        return IceCream(**client_requirements)

if __name__ == "__main__":
    # The Client
    ice_cream_requirements ={
        'flavor':'chocolate',
        'ingredients':['X','Y'],
        'pasteurization_level':1.0,
        'homogenization_level':0.5,
        'creaming_level':0.5,
        }
    ice_cream= Company.deliver(ice_cream_requirements)
    print(ice_cream.specification_as_dict())
    if ice_cream.specification_as_dict() == ice_cream_requirements:
        print('the product meet the levels needed')
    else:
        print('the product does not meet the levels needed, the product will be discarded.')
