k = 1;
num = k;
den = conv([1, 0], conv([4, 1], [2, 1]));
sys = tf(num, den);
sys
