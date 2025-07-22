# day01_linear_function.py
import numpy as np
import matplotlib.pyplot as plt
import torch

def linear_function_numpy(x, w, b):
    """用numpy实现线性函数"""
    return w * x + b

def main():
    print("=== Day 1: 线性函数可视化 ===")
    
    # 生成数据
    x = np.linspace(-5, 5, 100)
    
    # 不同参数的线性函数
    functions = [
        (1, 0, 'y = x', 'blue'),
        (2, 1, 'y = 2x + 1', 'red'), 
        (-0.5, 2, 'y = -0.5x + 2', 'green'),
        (0.5, -1, 'y = 0.5x - 1', 'orange')
    ]
    
    plt.figure(figsize=(12, 6))
    
    for w, b, label, color in functions:
        y = linear_function_numpy(x, w, b)
        plt.plot(x, y, label=label, color=color, linewidth=2)
    
    plt.title('Linear Functions - Day 1 Practice', fontsize=16)
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    plt.axhline(y=0, color='black', linewidth=0.5)
    plt.axvline(x=0, color='black', linewidth=0.5)
    
    plt.tight_layout()
    plt.show()
    print("✅ Day 1任务完成！")

if __name__ == "__main__":
    main()
