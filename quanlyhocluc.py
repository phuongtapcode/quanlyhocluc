def in_danh_sach(ds):
    if not ds:
        print("Danh sách rỗng")
        input("\nNhấn Enter để quay về menu...\n")
        return
    ds_sapxep = sorted(ds, key=lambda x: x['maso'])
    print("Danh sách sinh viên".center(100, "="))
    print(f"\n{'Mã số':<10} {'Họ và tên':<30} {'Điểm cơ sở':<15} {'Điểm chuyên ngành':<20} {'Điểm cuối kì':<15}")
    print("-" * 100)

    for i in ds_sapxep:
        ten = i['ten']
        a = 0
        while a < len(ten):
            cuoi = a + 30
            if cuoi < len(ten):
                sp = ten.rfind(" ", a, cuoi)
                if sp >= a:
                    cuoi = sp + 1

            du = ten[a:cuoi].rstrip()

            if a == 0:
                print(f"{i['maso']:<10} {du:<30} {i['dcs']:<15.1f} {i['dcn']:<20.1f} {i['dck']:<15.1f}")
            else:
                print(f"{'':<10} {du:<30}")

            a = cuoi

    print()
    input("\nNhấn Enter để quay về menu...\n")

def diem_cao_nhat(ds):
    if not ds:
        print("Danh sách rỗng")
        input("\nNhấn Enter để quay về menu...\n")
        return

    diem_cao = max(sv['dck'] for sv in ds)
    sv_cao = [sv for sv in ds if sv['dck'] == diem_cao]

    print('SINH VIÊN CÓ ĐIỂM CAO NHẤT'.center(100, "="))
    print(f"\n{'Mã số':<10} {'Họ và tên':<30} Điểm cuối kì")
    print("-" * 100)
    for sv in sv_cao:
        print(f"{sv['maso']:<10} {sv['ten']:<30} {sv['dck']:.1f}")
    print()
    input("\nNhấn Enter để quay về menu...\n")

def diem_thap_nhat(ds):
    if not ds:
        print("Danh sách rỗng")
        input("\nNhấn Enter để quay về menu...\n")
        return

    diem_thap = min(sv['dck'] for sv in ds)
    sv_thap = [sv for sv in ds if sv['dck'] == diem_thap]

    print('SINH VIÊN CÓ ĐIỂM THẤP NHẤT'.center(100, "="))
    print(f"\n{'Mã số':<10} {'Họ và tên':<30} Điểm cuối kì")
    print("-" * 100)
    for sv in sv_thap:
        print(f"{sv['maso']:<10} {sv['ten']:<30} {sv['dck']:.1f}")
    print()
    input("\nNhấn Enter để quay về menu...\n")

def khong_dat(ds):
    if not ds:
        print("Danh sách rỗng")
        input("\nNhấn Enter để quay về menu...\n")
        return
    print(f"Danh sách sinh viên chưa đạt".center(100, "="))
    print(f"{'Mã Số':<10} {'Họ và tên':<30} {'Môn không đạt':<20} Điểm\n")
    dat = True
    for i in ds:
        cacmon = []
        if i['dcs'] < 4:
            cacmon.append(("Điểm cơ sở", i["dcs"]))
        if i['dcn'] < 4:
            cacmon.append(("Điểm chuyên ngành", i["dcn"]))
        if cacmon:
            print(f"{i['maso']:<10} {i['ten']:<30} {cacmon[0][0]:<20} {cacmon[0][1]:.1f}")
            for mon, diem in cacmon[1:]:
                print(f"{'':<42}{mon:<20} {diem:.1f}")
            print("-" * 100)
            dat = False
    if dat:
        print("\nTất cả sinh viên đều đạt")
    input("\nNhấn Enter để quay về menu...\n")

def nhap_danh_sach_them(ds):
    while True:
        print("Nhập thêm danh sách sinh viên".center(100, "="))
        print("Nhập mã số là \"thoat\" để ra Menu\n")
        maso = input("Mã Số: ")
        if maso.lower() == "thoat":
            print("Thoát chương trình")
            break
        elif any(sv['maso'] == maso for sv in ds):
            print("Mã số đã tồn tại")
            input("\nNhấn Enter để nhập lại...\n")
            continue
        ten = input("Họ và tên: ").title()
        try:
            dcs = float(input("Điểm cơ sở: "))
            dcn = float(input("Điểm chuyên ngành: "))
        except ValueError:
            print("Vui lòng nhập lại điểm")
            input("\nNhấn Enter để nhập lại...\n")
            continue
        if not (0<=dcs<=10 and 0<=dcn<=10):
            print("Điểm từ 0-10")
            input("\nNhấn Enter để nhập lại...\n")
            continue
        dck = dcs * 0.4 + dcn* 0.6
        ds.append({'maso': maso, 'ten': ten, 'dcs': dcs, 'dcn': dcn, 'dck': dck})
        print("Thêm sinh viên thành công")
        input("\nNhấn Enter để nhập tiếp...\n")

def xoa_thong_tin(ds):
  if not ds:
    print("Danh sách rỗng")
    input("\nNhấn Enter để quay về menu...\n")
    return
  while True:
    print("Xóa thông tin sinh viên".center(100, "="))
    print("Nhập mã số là \"thoat\" để ra Menu")
    maso = input("\nMã Số: ")
    if maso.lower() == "thoat":
      print("Thoát chương trình")
      break
    thongtinsv = None
    for i in ds:
      if i['maso'] == maso:
          thongtinsv = i
          break
    if thongtinsv is None:
      print("Không tìm thấy sinh viên")
      input("\nNhấn Enter để nhập lại...\n")
      continue
    print("Thông tin sinh viên".center(100, "="))
    print(f"{'Mã số':<10} | {'Họ và tên':<30} | {'Điểm cơ sở':<15} | {'Điểm chuyên ngành':<20} | {'Điểm cuối kì':<15}")
    print(f"{thongtinsv['maso']:<10} | {thongtinsv['ten']:<30} | {thongtinsv['dcs']:<15.1f} | {thongtinsv['dcn']:<20.1f} | {thongtinsv['dck']:<15.1f}")
    while True:
        print("\n1. Xóa \n2. Hủy")
        chon = input("Chọn: ").strip()
        if chon == "1":
          ds.remove(thongtinsv)
          print("Xóa thành công")
          input("\nNhấn Enter để quay lại...\n")
          break
        elif chon == "2":
          print("Đã hủy thao tác")
          input("\nNhấn Enter để quay lại...\n")
          break
        else:
          print("Không hợp lệ")
        
        
danhsach = [{"maso": "MS0001", "ten": "Huỳnh Thanh Phương", "dcs": 10.0, "dcn": 10.0, "dck": 10.0 * 0.4 + 10.0 * 0.6},
            {"maso": "MS0002", "ten": "Trần Ngọc Hiếu", "dcs": 10.0, "dcn": 10.0, "dck": 10.0 * 0.4 + 10.0 * 0.6},
            {"maso": "MS0003", "ten": "Trần Tiến Đạt", "dcs": 10.0, "dcn": 10.0, "dck": 10.0 * 0.4 + 10.0 * 0.6}]

while True:
    print(" Menu ".center(40, "="))
    print("1. In thông tin sinh viên")
    print("2. Sinh viên có điểm cuối kì cao nhất")
    print("3. Sinh viên có điểm cuối kì thấp nhất")
    print("4. Danh sách sinh viên không đạt")
    print("5. Nhập thêm danh sách")
    print("6. Xóa thông tin")
    print("7. Đóng chương trình\n")
    chon = input("Nhập mục số: ").strip()
    print()
    if chon == "1":
        in_danh_sach(danhsach)
    elif chon == "2":
        diem_cao_nhat(danhsach)
    elif chon =="3":
        diem_thap_nhat(danhsach)
    elif chon == "4":
        khong_dat(danhsach)
    elif chon == "5":
        nhap_danh_sach_them(danhsach)
    elif chon == "6":
        xoa_thong_tin(danhsach)
    elif chon == "7":
        print("\nĐóng chương trình")
        break
    else:
        print("Hãy nhập lại\n")