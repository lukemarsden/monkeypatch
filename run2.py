from do_not_touch_me import Foo
def hack(self):
    print "boom"
Foo.hello = hack

if __name__ == "__main__":
    f = Foo()
    f.hello()
