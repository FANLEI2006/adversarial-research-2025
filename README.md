# adversarial-research-2025
24-month journey to USENIX Security paper on adversarial illusions

# 对抗样本研究学习日志

## Day 1 - 2025-07-22

### 学习时间
**总计**: 2小时

### 完成任务
- [x] 观看CS229 Lecture 1
- [x] 搭建Python 3.12 + PyTorch CUDA环境  
- [x] 验证2080Ti GPU正常工作
- [x] 完成线性函数可视化练习
- [x] 建立项目目录结构
- [x] 创建GitHub仓库

### 关键收获
1. **机器学习基础概念**：监督学习vs无监督学习
2. **环境搭建**：PyTorch + CUDA 12.1配置成功
3. **GPU性能**：2080Ti 22GB显存，性能测试通过

### 技术笔记
- Python 3.12与最新PyTorch兼容良好
- CUDA 12.8向下兼容CUDA 12.1版PyTorch
- 线性函数：y = wx + b，权重w控制斜率，偏置b控制截距

### 遇到的问题
- 无重大问题

### 明天计划 (Day 2)
- [x] 观看CS229 Lecture 2: Linear Regression
- [x] 用numpy实现线性回归算法
- [x] 梯度下降算法手动实现
- [x] 在简单数据集上测试效果

### 代码文件
- `test_2080ti.py` - GPU环境测试
- `day01_linear_function.py` - 线性函数可视化
### GPU性能测试结果
- **2000×2000矩阵**: 0.005秒
- **4000×4000矩阵**: 0.016秒  
- **6000×6000矩阵**: 0.043秒
- **8000×8000矩阵**: 0.087秒
- **结论**: RTX 2080Ti性能优秀，后续深度学习训练有保障

### Day 1 总结
✅ 所有环境配置完成 ✅ GPU性能验证通过 ✅ 基础代码测试成功 ---
