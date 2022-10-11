def main() :
    sqrt = lambda x : x ** 0.5

    class test(pyvdl.obj) :
        def __init__(self) :
            super().__init__()
            self.c = 0
            self.color = (255,255,255)

        def render(self,x,y) :
            return sqrt((x ** 2) ** self.c + (y ** 2) ** self.c)==10

    #a1.video("test.avi")
if __name__=='__main__' :
    from src import pyvdl

    main()
