# leetcode-python
## 刷題清單：  
https://docs.google.com/spreadsheets/d/1YhwajjbZDVFHxEZS3k9z-LbWwe2LK8x5XIaFThKZL9I/edit?usp=sharing  

## 解題觀念：
### [Two Pointer](https://www.youtube.com/watch?v=86GHTcY0K4I&list=PLV5qT67glKSErHD66rKTfqerMYz9OaTOs&index=2&ab_channel=%E5%9B%BE%E7%81%B5%E6%98%9F%E7%90%83TuringPlanet)
1. 同向 Two Pointer
  ![](https://i.imgur.com/dUqTY2Z.png)
  - Pseudo Code:
    ```cmd
    1. initialize two pointer: i = 0, j = 0 
    2. while j < len(arr):
         if need arr[j]:
           then we assign arr[i] = arr[j], i++, j++
         else: 
           j++
     ```
2. 反向 Two Pointer
  ![](https://i.imgur.com/FFg4oXz.png)
  -  Pseudo Code:
     ```cmd
     1. initialize two pointer: i = 0, j = len(arr) - 1
     2. while i <= j:
         decide what should do based on arr[i], arr[j]
         move at least one pointer
     ```
 
### [Binary Search](https://www.youtube.com/watch?v=j2_JW3In9PE&list=PLV5qT67glKSErHD66rKTfqerMYz9OaTOs&index=3&ab_channel=%E5%9B%BE%E7%81%B5%E6%98%9F%E7%90%83TuringPlanet)
1. 針對排序好的區間做O(log(n))的搜尋。
2. 必須把握以下兩個原則：
  - 每次都要縮減區域。
  - 每次縮減不能排除可能的答案。
3. 分為精確搜尋和模糊搜尋：
  - 找一個精確值： 
    - 循環條件：l <= r  
    - 縮減搜尋空間： l = mid + 1, r = mid - 1
  - 找模糊值(某個數字出現的第一個位置 or 最後一個位置)：
    - 循環條件：l < r  
    - 縮減搜尋空間： l = mid, r = mid - 1 or l = mid + 1, r = mid
  - 找最接近某個數字：
    - 循環條件： l < r - 1
    - 縮減搜尋空間： l = mid, r = mid 

### [Linked List](https://www.youtube.com/watch?v=0czlvlqg5xw&list=PLV5qT67glKSErHD66rKTfqerMYz9OaTOs&index=4&ab_channel=%E5%9B%BE%E7%81%B5%E6%98%9F%E7%90%83TuringPlanet)
1. 通常用同向的 Tow Pointer 來解
  - 一個快一個慢，距離隔開多少
  - 兩個指針的移動速度
 
 
### [Recursion](https://www.youtube.com/watch?v=0czlvlqg5xw&list=PLV5qT67glKSErHD66rKTfqerMYz9OaTOs&index=4&ab_channel=%E5%9B%BE%E7%81%B5%E6%98%9F%E7%90%83TuringPlanet)
1. Pseudo Code: 
  ```cmd
  - Ask for subproblem result.
  - Do something in current level or recursion.
  - Return result
  ```


### [Tree BFS](https://www.youtube.com/watch?v=jEg9AeN5a2Q&list=PLV5qT67glKSErHD66rKTfqerMYz9OaTOs&index=8&ab_channel=%E5%9B%BE%E7%81%B5%E6%98%9F%E7%90%83TuringPlanet)
1. BFS (寬度優先搜尋演算法): 是按照 '層' 的概念進行搜尋算法
2. 幾乎所有 BFS 題目都可以用 Queue 來記錄被展開的 TreeNode
3. Pseudo Code: 
  ```cmd
  - Initialize Queue with tree root node.
  - While Queue is not empty
    - for each node in the current queue
    - pull out the node
    - expand the node, push children to the Queue in order
    - increase level
  ```

### [Tree DFS](https://www.youtube.com/watch?v=5jz66VkGMCY&list=PLV5qT67glKSErHD66rKTfqerMYz9OaTOs&index=9&ab_channel=%E5%9B%BE%E7%81%B5%E6%98%9F%E7%90%83TuringPlanet)
1. DFS (深度優先搜尋演算法): 是依照 Recursive 的概念進行搜尋算法，偏向於垂直的概念
2. DFS 分為三種: 
   - Preorder Traversal
   ```python
   def dfs(node):
      if node is None:
          return
      print(node.val)
      dfs(node.left)
      dfs(node.right)
   ```
   - Inorder Traversal
   ```python
   def dfs(node):
      if node is None:
          return
      dfs(node.left)
      print(node.val)
      dfs(node.right)
   ```
   - Postorder Traversal
   ```python
   def dfs(node):
      if node is None:
          return
      dfs(node.left)
      dfs(node.right)
      print(node.val)
   ```
4. Button Up DFS (建議從中間狀態構建思路):
   - 把值從下(subproblem)往上傳遞
   - 當前遞歸層利用subproblem 傳上來的計算當前層的新值並返回
   - 一定有返回值
   - Pseudo Code: 
  ```cmd
  - Base Case
  - 向子問題要答案(return value)
  - 利用子問題的答案構建當前問題的答案
  - 返回答案給父問題
 ```
5. Top Down DFS:
  - 把值透過參數的形式往下傳遞
  - top down dfs 一般來說不返回值
  - Pseudo Code: 
  ```cmd
  - Base Case
  - 利用父問題傳下來的值做計算
  - 把值傳給子問題做 recursion
  ```
  
### Ref:   
[[心得] COVID期間拿到Google FB 微軟 Offer](https://www.ptt.cc/bbs/Soft_Job/M.1605589986.A.CBA.html)  
[如何高效運用LeetCode | 我的secret spreadsheet](https://www.youtube.com/watch?v=ucTL2ZdcyOs&feature=emb_title&ab_channel=AHTech)
