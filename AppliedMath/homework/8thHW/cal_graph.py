# 단순 계층 구현
class AddLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y
        return x + y

    def backward(self, dout):
        return dout, dout


class MulLayer:
    def __init__(self):
        self.x = None
        self.y = None

    def forward(self, x, y):
        self.x = x
        self.y = y
        return x*y

    def backward(self, dout):
        dx = dout * self.y
        dy = dout * self.x
        return dx, dy

# Condition
apple_num, mandarin_num, pear_num = 2, 3, 5
apple, mandarin, pear = 100, 150, 200
tax = 1.1

# Create Calculate Layer
mul_apple_layer = MulLayer()
mul_mandarin_layer = MulLayer()
mul_pear_layer = MulLayer()
add_apple_mandarin_layer = AddLayer()
add_all_layer = AddLayer()
mul_tax_layer = MulLayer()

# Forward
apple_price = mul_apple_layer.forward(apple_num, apple)
mandarin_price = mul_mandarin_layer.forward(mandarin_num, mandarin)
pear_price = mul_pear_layer.forward(pear_num, pear)
apple_mandarin_price = add_apple_mandarin_layer.forward(apple_price, mandarin_price)
all_price = add_all_layer.forward(apple_mandarin_price, pear_price)
price = mul_tax_layer.forward(all_price, tax)

# Backward when dout = 1.3
dout = 1.3
dall_price, dtax = mul_tax_layer.backward(dout)
d_apple_mandarin_price, dpear_price = add_all_layer.backward(dall_price)
dpear_num, dpear = mul_pear_layer.backward(dpear_price)
dapple_price, dmandarin_price = add_apple_mandarin_layer.backward(d_apple_mandarin_price)
dapple_num, dapple = mul_apple_layer.backward(dapple_price)
dmandarin_num, dmandarin = mul_mandarin_layer.backward(dmandarin_price)

print("# Forward")
print("Prices - apple : {0}, madarin : {1}, pear : {2}".format(apple_price, mandarin_price, pear_price))
print("Total price : {0} & Tax including price : {1:4.2f}".format(all_price, price))

print("\n# Backward ( dout = 1.3 )")
print("dprice : {0:3.2f}, dtax : {1:3.2f}".format(dall_price, dtax))
print("d fruit prices - apple : {0:3.2f}, mandarin : {1:3.2f}, pear : {2:3.2f}".format(dapple_price, dmandarin_price, dpear_price))
print("dapple_num : {0:3.2f}, dapple : {1:3.2f}".format(dapple_num, dapple))
print("dmandarin_num : {0:3.2f}, dmandarin : {1:3.2f}".format(dmandarin_num, dmandarin))
print("dpear_num : {0:3.2f}, dpear : {1:3.2f}".format(dpear_num,dpear))