from const import PI

def calc_round_area(radius):
    return PI * (radius ** 2)

def main():
    print('round area: %s' % calc_round_area(2))

"""
当运行area.py时，将执行area.py的main()，不执行const.py的main()
"""
main()