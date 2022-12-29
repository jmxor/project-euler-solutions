"""Problem 008 - Largest product in a series"""

from functools import reduce

if __name__ == '__main__':
    n = "7316717653133062491922511967442657474235534919493496983520312"\
        "7745063262395783180169848018694788518438586156078911294949545"\
        "9501737958331952853208805511125406987471585238630507156932909"\
        "6329522744304355766896648950445244523161731856403098711121722"\
        "3831136222989342338030813533627661428280644448664523874930358"\
        "9072962904915604407723907138105158593079608667017242712188399"\
        "8797908792274921901699720888093776657273330010533678812202354"\
        "2180975125454059475224352584907711670556013604839586446706324"\
        "4157221553975369781797784617406495514929086256932197846862248"\
        "2839722413756570560574902614079729686524145351004748216637048"\
        "4403199890008895243450658541227588666881164271714799244429282"\
        "3086346567481391912316282458617866458359124566529476545682848"\
        "9128831426076900422421902267105562632111110937054421750694165"\
        "8960408071984038509624554443629812309878799272442849091888458"\
        "0156166097919133875499200524063689912560717606058861164671094"\
        "0507754100225698315520005593572972571636269561882670428252483"\
        "600823257530420752963450"
    greatest = 0
    for i in range(len(n) - 13):
        substring = n[i:i+13]
        digits = [int(c) for c in substring]
        product = reduce(lambda x, y: x * y, digits)
        greatest = max(greatest, product)
    print(greatest)
