import test3 as t3
import test2 as t2

superInstance = t2.SuperClass("あいうえお")
subInstance = t3.SubClass()

print(f"superInstance: {superInstance}")
print(f"superInstance.field: {superInstance.field}")
superInstance.standard("aiueo")
superInstance.virtual("aiueo")

print(f"subInstance: {subInstance}")
print(f"subInstance.field: {subInstance.field}")
subInstance.standard("aiueo")
subInstance.virtual("aiueo")
subInstance.callStandard()

