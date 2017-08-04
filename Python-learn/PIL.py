import PIL
"""
   PIL: Python Imaging Library :Python平台图像处理标准库，功能强大，使用简便
"""
"""  操作图像  """

# 打开当前路径下一个jpg图像文件
im = PIL.Image.open('kaer.jpg')
w, h = im.size
print('Original image size: %sx%s' %(w, h))
# 缩放50%
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))
# 缩放后的图像用jpeg格式保存
im.save('thumbnail.jpg', 'jpeg')