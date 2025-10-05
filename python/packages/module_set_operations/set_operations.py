class Set:
    def __init__(self, elements=None):
        if elements is None:
            self.elements = []
        else:
            self.elements = list(dict.fromkeys(elements)) # Remove duplicates while preserving order

    def add_element(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def remove_element(self, element):
        if element in self.elements:
            self.elements.remove(element)

    def contains(self, element):
        return element in self.elements

    def get_elements(self):
        return self.elements
    
    def set_elements(self, list_of_elements):
        self.elements = list_of_elements
        return self
    
    def union(self, other_set):
        new_elements = self.elements[:]
        for element in other_set.get_elements():
            if element not in new_elements:
                new_elements.append(element)
        return Set(new_elements)
        
    
    def set_difference(self, other_set):
        new_elements = [element for element in self.elements if element not in other_set.get_elements()]
        return Set(new_elements)
        
    
    def intersection(self, other_set):
        new_elements = [element for element in self.elements if element in other_set.get_elements()]
        return Set(new_elements)



class MultiSet(Set):
    def __init__(self, elements=None):
        if elements is None:
            self.elements = []
        else:
            self.elements = elements  # Allow duplicates
    
    def add_element(self, element):
        self.elements.append(element)  # Allow duplicates

    def remove_element(self, element):
        if element in self.elements:
            self.elements.remove(element)  # Remove only one occurrence

    def count(self, elements):
        return self.elements.count(elements)
    
    def union(self, other_multiset):
        new_elements = self.elements + other_multiset.get_elements()
        self.set_elements(new_elements)
    
    def intersection(self, other_set):
        return super().intersection(other_set)
    
    def set_difference(self, other_set):
        dictionary = {}
        for element in self.elements:
            if element in dictionary.keys():
                dictionary[element] += 1
            else:
                dictionary[element] = 1
        for element in other_set.get_elements():
            if element in dictionary.keys():
                dictionary[element] -= 1
        new_elements = []
        for key, value in dictionary.items():
            if value > 0:
                new_elements += [key] * value
        return MultiSet(new_elements)