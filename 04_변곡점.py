import numpy as np
import matplotlib.pyplot as plt
import cv2

time = np.array([  0.10810811,   0.75675676,   1.62162162,   2.59459459,
            3.56756757,   4.21621622,   4.97297297,   4.97297297,
            4.97297297,   4.97297297,   4.97297297,   4.97297297,
            4.97297297,   4.97297297,   5.08108108,   5.18918919,
            5.2972973 ,   5.51351351,   5.72972973,   5.94594595,
            6.27027027,   6.59459459,   7.13513514,   7.67567568,
            8.32432432,   9.18918919,  10.05405405,  10.91891892,
           11.78378378,  12.64864865,  13.51351351,  14.37837838,
           15.35135135,  16.32432432,  17.08108108,  18.16216216,
           19.02702703,  20.        ,  20.        ,  20.        ,
           20.        ,  20.        ,  20.        ,  20.        ,
           20.10810811,  20.21621622,  20.43243243,  20.64864865,
           20.97297297,  21.40540541,  22.05405405,  22.91891892,
           23.78378378,  24.86486486,  25.83783784,  26.7027027 ,
           27.56756757,  28.54054054,  29.51351351,  30.48648649,
           31.56756757,  32.64864865,  33.62162162,  34.59459459,
           35.67567568,  36.64864865,  37.62162162,  38.59459459,
           39.67567568,  40.75675676,  41.83783784,  42.81081081,
           43.89189189,  44.97297297,  46.05405405,  47.02702703,
           48.10810811,  49.18918919,  50.27027027,  51.35135135,
           52.43243243,  53.51351351,  54.48648649,  55.56756757,
           56.75675676,  57.72972973,  58.81081081,  59.89189189])

volts = np.array([ 4.11041056,  4.11041056,  4.11041056,  4.11041056,  4.11041056,
           4.11041056,  4.11041056,  4.10454545,  4.09794721,  4.09208211,
           4.08621701,  4.07961877,  4.07228739,  4.06568915,  4.05909091,
           4.05175953,  4.04516129,  4.03782991,  4.03123167,  4.02463343,
           4.01803519,  4.01217009,  4.00557185,  3.99970674,  3.99384164,
           3.98797654,  3.98284457,  3.97771261,  3.97331378,  3.96891496,
           3.96451613,  3.96085044,  3.95645161,  3.95205279,  3.9483871 ,
           3.94398827,  3.94032258,  3.93665689,  3.94325513,  3.94985337,
           3.95645161,  3.96378299,  3.97038123,  3.97624633,  3.98284457,
           3.98944282,  3.99604106,  4.0026393 ,  4.00923754,  4.01510264,
           4.02096774,  4.02609971,  4.02903226,  4.03196481,  4.03416422,
           4.0356305 ,  4.03709677,  4.03856305,  4.03929619,  4.04002933,
           4.04076246,  4.04222874,  4.04296188,  4.04296188,  4.04369501,
           4.04442815,  4.04516129,  4.04516129,  4.04589443,  4.04589443,
           4.04662757,  4.04662757,  4.0473607 ,  4.0473607 ,  4.04809384,
           4.04809384,  4.04809384,  4.04882698,  4.04882698,  4.04882698,
           4.04956012,  4.04956012,  4.04956012,  4.04956012,  4.05029326,
           4.05029326,  4.05029326,  4.05029326])

# tdiff = np.diff(time)
# vdiff = np.diff(volts)
#
# # point A
# idxA = np.where(vdiff < 0)[0][0]
#
# timeA = time[idxA]
# voltA = volts[idxA]
#
# # point C
# idxC = volts.idxmin()
# timeC = time[idxC]
# voltC = volts[idxC]


def masks(vec):
    d = np.diff(vec)
    dd = np.diff(d)

    # Mask of locations where graph goes to vertical or horizontal, depending on vec
    to_mask = ((d[:-1] != 0) & (d[:-1] == -dd))
    # print(to_mask)
    # Mask of locations where graph comes from vertical or horizontal, depending on vec
    from_mask = ((d[1:] != 0) & (d[1:] == dd))
    # print(from_mask)
    return to_mask, from_mask


to_vert_mask, from_vert_mask = masks(time)
to_horiz_mask, from_horiz_mask = masks(volts)


def apply_mask(mask, x, y):
    return x[1:-1][mask], y[1:-1][mask]


to_vert_t, to_vert_v = apply_mask(to_vert_mask, time, volts)
print(to_vert_t, to_vert_v )
from_vert_t, from_vert_v = apply_mask(from_vert_mask, time, volts)
to_horiz_t, to_horiz_v = apply_mask(to_horiz_mask, time, volts)
from_horiz_t, from_horiz_v = apply_mask(from_horiz_mask, time, volts)

# plt.plot(time, volts, 'b-')
# plt.plot(to_vert_t, to_vert_v, 'r^', label='Plot goes vertical')
# plt.plot(from_vert_t, from_vert_v, 'kv', label='Plot stops being vertical')
# plt.plot(to_horiz_t, to_horiz_v, 'r>', label='Plot goes horizontal')
# plt.plot(from_horiz_t, from_horiz_v, 'k<', label='Plot stops being horizontal')
# plt.legend()

to_horiz_t, to_horiz_v = apply_mask(to_horiz_mask, time, volts)
to_horiz_t, to_horiz_v = to_horiz_t[-1], to_horiz_v[-1]

plt.plot(time, volts, 'b-')
plt.plot(*apply_mask(to_vert_mask, time, volts), 'r^', label='Plot goes vertical')
plt.plot(*apply_mask(from_vert_mask, time, volts), 'kv', label='Plot stops being vertical')
plt.plot(to_horiz_t, to_horiz_v, 'r>', label='Plot goes horizontal')
plt.legend()
plt.show()

plt.show()