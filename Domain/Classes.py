class Product:
    _productFeatures = {}
    
    def __init__(self, name):
        self.name = name
    
    def addFeature(self, featureDict):
        self._productFeatures.update(featureDict)
    
    def returnFeatureProduct(self):
        return self._productFeatures
    
class Website:
    pass