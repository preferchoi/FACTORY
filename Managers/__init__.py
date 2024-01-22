class InstanceManager:
    def __init__(self):
        self.instances = []

    def add_instance(self, instance):
        self.instances.append(instance)

    def remove_instance(self, instance):
        self.instances.remove(instance)

    def get_instances(self):
        return {"Factories": [{"id": instance.id} for instance in self.instances]}

    def get_instance(self, factory_id):
        factory = [instance for instance in self.instances if instance.id == factory_id]
        if factory:
            return {"Factory": factory[0]}
        else:
            return {"error": "Factory not found"}