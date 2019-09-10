# Truth Table Generator
Code này giúp sinh ra bảng chân trị của một biểu thức Logic, ví dụ như: (p v (p ^ q)) ^ !p -> r. 


# Một số phép toán

Trong code này, mình có xử lý tổng cộng 5 phép toán sau đây: 
- Phép NOT, còn gọi là phép phủ định:  viết bằng '!' hoặc '-' .
- Phép AND, còn gọi là phép hội, phép nối liền: viết bằng '^' hoặc '.' .
- Phép OR, còn gọi là phép tuyển, phép nối rời: viết bằng 'v' hoặc '+' .
- Phép kéo theo: viết bằng '->' hoặc '>' .
- Phép tương đương: viết bằng '<->' or '~' .

**Thứ tự tính toán**: NOT > AND = OR > kéo theo = tương đương.
- Phép NOT sẽ được tính đầu tiên (thứ tự tính cao nhất)
- Sau đó là phép AND và phép OR.
- Cuối cùng là phép kéo theo và phép tương đương (thứ tự tính thấp nhất).
- Nếu các phép có cùng thứ tự thì tính từ trái sang phải.

# Cách dùng
Tải file [TruthTableGenerator.py](TruthTableGenerator.py) và chạy với lệnh `python TruthTableGenerator.py`, sau đó nhập biểu thức logic vào, chương trình sẽ đưa ra bảng trân trị của biểu thức đó.

Dùng các ký tự lattin thường để biểu diễn các biến, nhưng đừng xử dụng ký tự 'v', vì trong code của mình 'v' là một phép tính (phép OR). Vì vậy, có thể sử dụng nhiều nhất là 25 biến trong biểu thức. Dù vậy, độ phức tạp của code mình rơi vào khoảng O(2^n) với n là số biến, cùng với hằng số lập trình rất lớn, do đó tốt nhất đừng dùng quá nhiều biến, nhỏ hơn 15 biến thì nó vẫn chạy dưới 1s được. 

# Ví dụ
Có biểu thức là: (p v (p ^ q)) ^ !p -> r.

Bảng chân trị được sinh ra là:
```
  p  |  q  |  r  |  (p v (p ^ q)) ^ !p -> r
  0  |  0  |  0  |  1
  0  |  0  |  1  |  1
  0  |  1  |  0  |  1
  0  |  1  |  1  |  1
  1  |  0  |  0  |  1
  1  |  0  |  1  |  1
  1  |  1  |  0  |  1
  1  |  1  |  1  |  1
```
