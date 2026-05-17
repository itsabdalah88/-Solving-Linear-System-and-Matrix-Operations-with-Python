import sympy as s
a,b,c,d,e,f,g,h,i,j = s.symbols('a b c d e f g h i j')

m =[
    2a - b + 3c - 4d + 5e + f - 2g + 3h + 4i - j - 17,
    a + 3b - 2c + 4d - 5e - 2f + 3g - 4h - 5i + 2j + 23,
    3a - 2b + 4c + 5d - e - 3f + 4g - 5h + 2i - 4j - 14,
    4a + 5b - c - 3d + 4e - 5f + 2g - 4h + 5i - 2j + 15,
    -a + 4b + 5c + 4d - 3e + 2f - 4g + 5h - 2i + 3j - 11,
    2a - 5b - 4c + 3d + 2e - 5f + 4g - 3h + 2i + 5j + 7,
    -3a + 4b - 5c - d + 4e + 2f - 5g + 4h + 2i + 3j - 12,
    5a - 2b + 4c + 5d - 3e - 4f + 5g - 2h + 4i - j + 8,
    4a + 3b - 2c - 4d + 5e - f + 3g - 2h - i + 4j + 19,
    -a + 2b + 3c - 4d - 5e + 2f - 3g + 4h + 5i - 2j - 10
]

solution = s.solve(m, [a,b,c,d,e,f,g,h,i,j])
for k,v in solution.items():
    print(k, float(v))