from PIL import ImageColor

#color = input("codigo color: ").lstrip("#")

pepe = []


#print('RGB = ', tuple(int(color[i:i+2], 16) for i in (0, 2, 4)))

color01 = ImageColor.getcolor("#9161d3", "RGB")
print(f"color RGB = {color01}")


print(color01[1])