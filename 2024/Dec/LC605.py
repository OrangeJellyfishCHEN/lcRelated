class LC605(object):
    def canPlaceFlowers(self, flowerbed, n: int):
        # number of continous zero
        # add one zero in the front of the flowerbed list to handle the start is zero circumstance
        z = 1
        # possible space to place flower
        p = 0
        for bed in flowerbed:
            if bed == 0:
                z += 1
            else:
                p += (z - 1) // 2
                if p >= n:
                    return True
                z = 0
        # add one zero after the end of flowerbed to handle the end is zero circumstance
        z += 1
        p += (z - 1) // 2
        return p >= n


lc = LC605()
print(lc.canPlaceFlowers([1,0,0,0,1], 1))
