class Vehicle:
    def __init__(self, make, model, description, image):
        self.make = make
        self.model = model
        self.description = description
        self.image = image
        
    def to_marqo_document(self):
        return {
            "Title": f"{self.make} {self.model}",
            "Description": self.description,
            "image": self.image
        }
