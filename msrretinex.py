import cv2
import numpy as np
image = cv2.imread("lena.jpg", 1)
#b,g,r = cv2.split(image)
#(row,col) = g.shape
#print(row)
#print(col)
cv2.imshow('Orginal image', image)


class BasicRetinexAlgo:

    def __init__(self, spread):
        self.spread = spread

    def basic_retinex(self, image):
        (n, m) = image.shape
        modified_image = np.zeros([n, m])
        for i in range(n):
            for j in range(m):
                gamma_square = i ** 2 + j ** 2
                power = float(gamma_square) / self.spread ** 2
                modified_image[i][j] = float(np.log((1 + image[i][j])) - np.log(1 + (image[i][j] * np.exp(-(power)))))

        factor = (255 / (np.amax(modified_image) - np.amin(modified_image)))
        processed_image = np.multiply(modified_image, factor).astype(int)
        return processed_image

r, g, b = cv2.split(image)

basrexa = BasicRetinexAlgo(int(input("Enter varience value : ")))
r_modifiedimagea = basrexa.basic_retinex(r)
g_modifiedimagea = basrexa.basic_retinex(g)
b_modifiedimagea = basrexa.basic_retinex(b)

basrexb = BasicRetinexAlgo(int(input("Enter varience value : ")))
r_modifiedimageb = basrexb.basic_retinex(r)
g_modifiedimageb = basrexb.basic_retinex(g)
b_modifiedimageb = basrexb.basic_retinex(b)

basrex = BasicRetinexAlgo(int(input("Enter varience value : ")))
r_modifiedimagec = basrex.basic_retinex(r)
g_modifiedimagec = basrex.basic_retinex(g)
b_modifiedimagec = basrex.basic_retinex(b)


final_imagea = cv2.merge((r_modifiedimagea, g_modifiedimagea, b_modifiedimagea))
final_imageb = cv2.merge((r_modifiedimageb, g_modifiedimageb, b_modifiedimageb))
final_imagec = cv2.merge((r_modifiedimagec, g_modifiedimagec, b_modifiedimagec))

final_image=1/3*(final_imagea+final_imageb+final_imagec)

cv2.imwrite('output.jpeg', final_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
