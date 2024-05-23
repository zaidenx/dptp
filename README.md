# dptp
# Naive SAT Solver

## 概述
這是一個簡單的 SAT 求解器，用於判定一個CNF表示的Boolean formula是否可滿足。它從一個 DIMACS 文件格式中讀取輸入，並輸出該公式是否可滿足 (SATISFIABLE) 或不可滿足 (UNSATISFIABLE)。如果公式是可滿足的，求解器還會提供一個滿足解。

## 算法
### Naive 方法
這個簡單的方法通過生成所有可能的assignments並檢查每個assignments是否滿足formala來解決 SAT 問題。這種方法對於大規模問題來說效率不高，但對於小規模的 SAT 問題來說是一種簡單直觀的方法。

## 安裝
要運行這個簡單的 SAT 求解器，你需要 Python 3.6 或更高版本。請按照以下步驟設置環境：

1. **Clone the repository**：
   ```sh
   git clone https://github.com/zaidenx/dptp.git
   cd dptp
   python3 test-2.py <input-file> --verbose

