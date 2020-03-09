class CropRatio:

    def __init__(self):
        self._crops = dict()
        self._total_weight = 0

    #Add Method: Add a new entry if crop does not exist
    #            if crop exists, combine the crop weights
    def add(self, name, crop_weight):
        if name not in self._crops:
            self._crops[name] = crop_weight
        else:
            self._crops[name] += crop_weight
            
        self._total_weight += crop_weight

    #Proportion Method: Return ratio based on crops, if crops exists.
    #                   else return 0 if unavailable
    def proportion(self, name):
        if name not in self._crops:
            return 0
        
        return self._crops[name]/self._total_weight 

#To see the output, uncomment the lines below:
crop_ratio = CropRatio()
crop_ratio.add('Wheat', 4)
crop_ratio.add('Wheat', 5)
crop_ratio.add('Rice', 1)

print(crop_ratio.proportion('Wheat'))