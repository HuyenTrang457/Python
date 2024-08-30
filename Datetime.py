CCHUẨN HÓA NGÀY SINH VỀ DẠNG .....
   def chuanHoa(self):
      date_obj = datetime.strptime(self.ngaySinh, "%d/%m/%Y")
    # Định dạng lại ngày tháng theo mong muốn
      self.ngaySinh= date_obj.strftime("%d/%m/%Y")

import datetime 
x=datetime.datetime.now()
print(x.strftime("%A")) -->Saturday


----- creating date object
import datetime

x = datetime.datetime(2020, 5, 17)

print(x)
