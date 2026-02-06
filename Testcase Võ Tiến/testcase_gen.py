import re
import sys

def extract_testcase(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # --- PHẦN ĐÃ SỬA ---
        # Dùng regex này để xóa và nối dòng
        content = re.sub(r"\n?\\", "", content)
        # -------------------

        # Tìm block code testcase
        pattern = r"(def test_\w+\(\):.*?)(?=\nE\s+)"
        match = re.search(pattern, content, re.DOTALL)

        if match:
            raw_code = match.group(1)
            
            lines = raw_code.splitlines()
            cleaned_lines = []
            
            for line in lines:
                # Xử lý dấu ">" của pytest
                if line.strip().startswith('>'):
                    line = line.replace('>', ' ', 1)
                
                cleaned_lines.append(line)
            
            print('\n'.join(cleaned_lines))
            
        else:
            print(f"Không tìm thấy testcase trong file {file_path}")

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file {file_path}")
    except Exception as e:
        print(f"Lỗi: {str(e)}")

if __name__ == "__main__":
    # Thay tên file log của bạn vào đây nếu chạy trực tiếp
    for x in range(47, 60):
        filename = f"result ({x}).log"
        if len(sys.argv) > 1:
            filename = sys.argv[1]
        
        extract_testcase(filename)