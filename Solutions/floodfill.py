
def floodFill (image, sr, sc, newColor):
    if image[sr][sc] == newColor:
        return image
    oldColor = image[sr][sc]
    image[sr][sc] = newColor
    return color(image,sr,sc,oldColor,newColor)
        

def color(image,sr,sc,oldColor,newColor):
    try:
        if image[sr][sc+1] == oldColor:
            image[sr][sc+1] = newColor
            color(image,sr,sc+1,oldColor,newColor)
    except:
        pass
    try:
        if image[sr][sc-1] == oldColor and sc != 0:
            image[sr][sc-1] = newColor
            color(image,sr,sc-1,oldColor,newColor)
    except:
        pass
    try:
        if image[sr+1][sc] == oldColor:
            image[sr+1][sc] = newColor
            color(image,sr+1,sc,oldColor,newColor)
    except:
        pass
    try:
        if image[sr-1][sc] == oldColor and sr != 0:
            image[sr-1][sc] = newColor
            color(image,sr-1,sc,oldColor,newColor)
    except:
        pass
    return image

print floodFill([[1,1,1],[1,1,0],[1,0,1]],1,1,2)
print floodFill([[0,0,0],[1,1,1]],1,1,1)