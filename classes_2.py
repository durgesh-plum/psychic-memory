class MethodExamples:
    def __init__(self):
        self.this_can_be_accessed_easily = "Hi, there I am"

    def get_this_can_be_accessed_easily(self):
        return self.this_can_be_accessed_easily

    def set_this_can_be_accessed_easily(self,value_to_set):
        self.this_can_be_accessed_easily = value_to_set


x = MethodExamples()

print(x.this_can_be_accessed_easily)

x.this_can_be_accessed_easily = "I have changed"

print(x.this_can_be_accessed_easily)

print(x.set_this_can_be_accessed_easily(60))
