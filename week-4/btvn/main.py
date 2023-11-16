from datetime import datetime, timedelta
def dem_ngay(date):
    try: 
    # chuyen chuou thanh datetime
        ngay_nhap = datetime.strptime(date,"%d/%m/%Y")
        ngay_cuoi = datetime(ngay_nhap.year,12,31)
        ngay_con_lai = (ngay_cuoi - ngay_nhap).days
        return ngay_con_lai
    except:
        return "Nhap ko dung dinh dang"
date = input("Nhap chuoi co dang: dd/mm/yyyy : ")
print(dem_ngay(date))