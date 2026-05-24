num_employees = int(input("Nhập số lượng nhân viên: "))

for i in range(num_employees):
    print("") 
    name = input("Nhập tên nhân viên: ")
    days_worked = int(input("Nhập số ngày làm: "))
    
    if days_worked < 0 or days_worked > 22:
        print("Dữ liệu không hợp lệ")
        continue  
        
    if days_worked == 0:
        print("Nhân viên nghỉ toàn bộ tháng")
        continue  
        
    print(f"{name}: ", end="")
    for j in range(days_worked):
        print("*", end="")
    print("")  
    if days_worked >= 18:
        print("Làm việc chăm chỉ")
    elif days_worked < 10:
        print("Làm việc ít")
    else:
        print("Làm việc bình thường")