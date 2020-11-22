import copy

elem1 = [1, 2, 3, 4, ]
elem2 = elem1  # 这个不是浅复制,也不是深复制, 属于赋值, 指向同一个地址

# 浅复制
## 1.复制后两个对象内容一样,但是内存地址不一样
word = ['hello', '12345', 'pear']
new_word = copy.copy(word)       # 内容一样,但是内存地址不一样
print(id(word),word)
print(id(new_word),new_word)
## 2. 如果元素中有引用的对象,则只复制最外面的一层,引用的对象不能复制
nums1 = [1,2,[100,200,300],6,7]
nums2 = copy.copy(nums1)   # 中间嵌套的列表不会被复制
print(id(nums1),nums1)
print(id(nums2),nums2)
### 修改中间嵌套列表的值, 复制前后的对象中的值都会改变, 说明引用的还是同一个对象
nums2[2][0]=500    # 中间嵌套的元素两个都会变
nums2[0] = 100     # 修改普通元素不会改变复制前的值
print(id(nums1),nums1)
print(id(nums2),nums2)


# 深复制
## 复制后两个对象完全没有关系
nums1 = [1,2,[100,200,300],6,7]
nums2 = copy.deepcopy(nums1)
nums2[2][0]=500        # 修改nums2 中的嵌套对象,也不会改变nums1 中的值
print(id(nums1),nums1)
print(id(nums2),nums2)



# https://www.pythontutor.com   查看代码执行过程