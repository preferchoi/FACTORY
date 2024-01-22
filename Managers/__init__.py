class InstanceManager:
    def __init__(self):
        self.instances = []

    def add_instance(self, instance):
        self.instances.append(instance)

    def remove_instance(self, instance):
        self.instances.remove(instance)

    def get_instances(self):
        return self.instances