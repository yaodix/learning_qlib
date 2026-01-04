### submodule设置

#### 验证submodule状态

```
git submodule status
```

**更新submodule** ：要更新qlib到最新版本，可以运行：

```
git submodule update --remote qlib
```

#### 可编辑模式安装qlib

```
cd qlib
pip install -e .[dev]
```
