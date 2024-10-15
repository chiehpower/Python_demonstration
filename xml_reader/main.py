import xml.etree.ElementTree as ET
import chardet


def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
    result = chardet.detect(raw_data)
    return result['encoding']


def parse_xml(xml_file_path):
    # 嘗試檢測文件編碼
    detected_encoding = detect_encoding(xml_file_path)
    print(f"檢測到的編碼: {detected_encoding}")

    # 嘗試不同的編碼
    encodings_to_try = [detected_encoding, 'utf-8', 'utf-16', 'gb18030', 'big5']
    
    for encoding in encodings_to_try:
        try:
            with open(xml_file_path, 'r', encoding=encoding) as file:
                xml_content = file.read()
            root = ET.fromstring(xml_content)
            print(f"成功使用 {encoding} 編碼讀取文件")
            break
        except UnicodeDecodeError:
            print(f"{encoding} 編碼失敗，嘗試下一個...")
        except ET.ParseError:
            print(f"{encoding} 編碼可以讀取文件，但XML解析失敗，嘗試下一個...")
    else:
        print("無法找到正確的編碼，請手動指定")
        return

    # 解析主訂單詳情
    order_details = {child.tag: child.text for child in root if not child.tag == 'Item'}

    # 解析商品
    items = []
    for item in root.findall('Item'):
        item_details = {child.tag: child.text for child in item}
        items.append(item_details)

    # 打印主訂單詳情
    print("\n訂單詳情:")
    for key, value in order_details.items():
        print(f"{key}: {value}")

    # 打印商品
    print("\n商品列表:")
    for i, item in enumerate(items, 1):
        print(f"\n商品 {i}:")
        for key, value in item.items():
            print(f"  {key}: {value}")

# 使用示例
xml_file_path = 'example.xml'
parse_xml(xml_file_path)
