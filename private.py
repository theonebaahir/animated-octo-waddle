class myclass:
    __privateVar = 27
    def __privmeth(self):
        print("i am inside myclass")
    def hello(self):
        print("private variable value:", myclass. __privateVar)
foo = myclass()
foo.hello()
foo.__privmeth