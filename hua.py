import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 设置画布大小
fig, ax = plt.subplots(figsize=(6, 4))

# 创建一个空白图像
img = np.zeros((500, 800, 3), dtype=np.uint8)

# 烟花的参数
num_stars = 200
x_range = 800
y_range = 500
x_offset = 200
y_offset = 250
x_variance = 50
y_variance = 25
speed = 3

# 初始化星星
stars = np.random.uniform(x_offset, x_offset + x_range, (num_stars, 2))

# 动画函数
def update(frame):
    global stars

    # 更新星星的位置
    stars[:, 0] += np.random.normal(0, x_variance / speed, num_stars)
    stars[:, 1] += np.random.normal(0, y_variance / speed, num_stars)

    # 过滤出在图像范围内的星星
    stars = stars[stars[:, 0] >= 0]
    stars = stars[stars[:, 0] < x_range]
    stars = stars[stars[:, 1] >= 0]
    stars = stars[stars[:, 1] < y_range]

    # 绘制星星
    for star in stars:
        img[int(star[1]), int(star[0])] = 255, 255, 255

    # 清空图像
    ax.imshow(img, animated=True)

# 创建动画
ani = animation.FuncAnimation(fig, update, frames=200, interval=50)

# 显示动画
plt.show()
