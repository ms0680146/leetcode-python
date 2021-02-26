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


### Ref:   
[[心得] COVID期間拿到Google FB 微軟 Offer](https://www.ptt.cc/bbs/Soft_Job/M.1605589986.A.CBA.html)  
[如何高效運用LeetCode | 我的secret spreadsheet](https://www.youtube.com/watch?v=ucTL2ZdcyOs&feature=emb_title&ab_channel=AHTech)
