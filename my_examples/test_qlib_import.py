
import sys
import qlib

print("✅ 成功导入qlib!")
print(f"qlib版本: {qlib.__version__}")
print(f"qlib路径: {qlib.__file__}")

# 查看路径是否来自你的开发目录
if "learning_qlib/qlib" in qlib.__file__:
    print("✅ 正在使用你的开发版本qlib!")
else:
    print("⚠️  使用的是系统安装的qlib，不是开发版本")