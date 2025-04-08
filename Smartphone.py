# Base Class: Smartphone
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def call(self, number):
        return f"Calling {number} from {self.brand} {self.model}..."

    def browse_web(self, website):
        return f"Browsing {website} on {self.brand} {self.model}."

# Subclass: SmartphoneWithCamera
class SmartphoneWithCamera(Smartphone):
    def __init__(self, brand, model, price, camera_resolution):
        super().__init__(brand, model, price)
        self.camera_resolution = camera_resolution

    def take_photo(self):
        return f"Taking a photo with {self.camera_resolution} camera on {self.brand} {self.model}."

# Usage
phone1 = Smartphone("Apple", "iPhone 14", 1000)
print(phone1.call("2768 473 8660"))
print(phone1.browse_web("www.Google.com"))

camera_phone = SmartphoneWithCamera("Samsung", "Galaxy S22 Ultra", 1200, "108MP")
print(camera_phone.take_photo())
print(camera_phone.call("2787 654 3210"))