# 二维码
# quick response code

import pyqrcode

# 设置二维码信息
s = "https://zhuanlan.zhihu.com/p/585066673"

# 生成二维码
url = pyqrcode.create(s)

# 保存二维码为图片
url.svg("zhihu.svg", scale=8)