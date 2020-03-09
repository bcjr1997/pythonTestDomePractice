#Incomplete
class CategoryTree:

    def __init__(self):
        self.category = dict()

    def add_category(self, category, parent):
        try:
            self.category[category] = None
            if self.category[parent] and self.category[parent] is None:
                self.category[parent] = list()
                self.category[parent].append(category)
            elif self.category[parent] and self.category[parent] is not None:
                self.category[parent].append(category)
                
        except KeyError as e:
            print(e)

    def get_children(self, parent):
        return self.category[parent]

if __name__ == "__main__":
    c = CategoryTree()
    c.add_category('A', None)
    c.add_category('B', 'A')
    c.add_category('C', 'A')
    print(','.join(c.get_children('A') or []))