


from externalmodule.car import info

class ownmodule():
    def cardescription(self):
        make = "bmw"
        model = "5501"
        info(make, model)

m = ownmodule()
m.cardescription()