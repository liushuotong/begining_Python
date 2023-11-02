import os
import sys
import pyinstaller


def convert_py_to_exe(py_file, exe_file):
    try:
        os.system(f"pyinstaller --onefile {py_file}")
        print(f"成功将 {py_file} 转换为 {exe_file}")
    except Exception as e:
        print(f"转换失败，错误信息：{e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("用法：python convert_py_to_exe.py <py文件名> <exe文件名>")
    else:
        py_file = sys.argv[1]
        exe_file = sys.argv[2]
        convert_py_to_exe(py_file, exe_file)