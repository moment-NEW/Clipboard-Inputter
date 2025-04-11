import pyperclip
import keyboard
import time
import traceback
import sys

# 配置参数
HOTKEY = 'ctrl+-'  # 可自定义的组合键
EXIT_KEY = 'esc'  # 退出程序的按键


def paste_clipboard():
    try:
        text = pyperclip.paste()
        print(f"正在输入 {len(text)} 个字符...")

        # 添加3秒准备时间
        for i in range(3, 0, -1):
            print(f"请将光标放在目标位置... {i}秒", end="\r")
            time.sleep(1)
        print(" " * 40, end="\r")  # 清除倒计时行

        keyboard.write(text)
        print("输入完成")
    except Exception as e:
        print(f"错误: {str(e)}")


def main():
    try:
        print("=" * 60)
        print("剪贴板输入工具")
        print("=" * 60)
        print(f"使用 {HOTKEY} 触发输入")
        print(f"按 {EXIT_KEY} 退出程序")
        print("=" * 60)

        # 注册热键
        keyboard.add_hotkey(HOTKEY, paste_clipboard)
        print("程序已启动，请保持在后台运行...")

        # 等待退出键
        keyboard.wait(EXIT_KEY)
        print("程序已退出")

    except Exception as e:
        print(f"程序错误: {str(e)}")
        print(traceback.format_exc())
        input("按回车键退出...")  # 防止窗口立即关闭


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"程序遇到严重错误: {str(e)}")
        print(traceback.format_exc())
        input("程序异常终止，按回车键退出...")