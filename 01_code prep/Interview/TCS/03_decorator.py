def dog(func):
    print("dog is barking")
    func()
    print("dog is silent")

@dog
def pitbull():
    print("pitbull is a breed of dog")