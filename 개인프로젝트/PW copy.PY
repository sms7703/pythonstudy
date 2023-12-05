import zipfile
import itertools
from tkinter import filedialog
from tkinter import Tk
from tqdm import tqdm  # Import tqdm for the progress bar

def brute_force_zip(zip_file_path, max_digits):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_file:
        total_combinations = sum(len('0123456789')**length for length in range(1, max_digits + 1))
        current_combination = 0

        # Generate all possible digit combinations
        with tqdm(total=total_combinations, desc="Progress") as pbar:
            for length in range(1, max_digits + 1):
                for combination in itertools.product('0123456789', repeat=length):
                    current_combination += 1
                    password = ''.join(combination)
                    try:
                        zip_file.extractall(pwd=password.encode('utf-8'))
                        print(f"Success! Password found: {password}")
                        return
                    except Exception as e:
                        pass

                    pbar.update(1)

    print(f"Password not found for {zip_file_path}.")
    print("찾지 못했습니다.")

def get_max_digits():
    while True:
        try:
            max_digits = int(input("최대 비밀번호 자릿수를 입력하세요: "))
            if max_digits > 0:
                return max_digits
            else:
                print("자연수를 입력하세요.")
        except ValueError:
            print("올바른 숫자를 입력하세요.")

# Tkinter root 생성
root = Tk()
root.withdraw()  # Tkinter 창 숨기기

# 파일 선택 대화상자 띄우기
zip_file_path = filedialog.askopenfilename(title="암호화된 ZIP 파일을 선택하세요", filetypes=[("ZIP files", "*.zip")])
if not zip_file_path:
    print("ZIP 파일 선택이 취소되었습니다.")
    exit(0)

# 최대 비밀번호 자릿수 입력 받기
max_digits = get_max_digits()

# 사용자가 선택한 파일 경로로 브루트포스 공격 수행
print(f"사용자가 선택한 ZIP 파일 경로: {zip_file_path}")
print(f"설정된 최대 비밀번호 자릿수: {max_digits}")
brute_force_zip(zip_file_path, max_digits)
