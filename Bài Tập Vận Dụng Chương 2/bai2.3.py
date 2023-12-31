import xml.dom.minidom

# Đọc nội dung từ file XML
file_path = 'D:\Bài Tập Vận Dụng Chương 2\sample.xml'
with open(file_path, 'r') as file:
    xml_content = file.read()

# Phân tích nội dung XML
dom = xml.dom.minidom.parseString(xml_content)

# Lấy phần tử gốc (root) của tài liệu XML
company = dom.documentElement

# Lấy giá trị của phần tử <name> (tên công ty)
company_name = company.getElementsByTagName('name')[0].firstChild.nodeValue
print(f'Tên công ty: {company_name}')

# Lấy thông tin về nhân viên
staff_list = company.getElementsByTagName('staff')
for staff in staff_list:
    staff_id = staff.getAttribute('id')
    staff_name = staff.getElementsByTagName('name')[0].firstChild.nodeValue
    staff_salary = staff.getElementsByTagName('salary')[0].firstChild.nodeValue
    print(f'\nNhân viên #{staff_id}:')
    print(f'  Tên: {staff_name}')
    print(f'  Lương: {staff_salary}')

