if __name__ == '__main__':
    from src import pyvdl
    r = pyvdl.font('BRADHITC.TTF', font_size = 224)
    pyvdl.save("A.png", r)