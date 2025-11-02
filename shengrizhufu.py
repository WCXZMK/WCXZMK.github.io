import tkinter as tk
import random
import threading
import time

# ================= 原有节日祝福相关代码 =================
class FestivalWishes:
    def __init__(self, root):
        self.root = root
        self.root.title("节日祝福")
        self.root.geometry("600x400")
        
        # 主祝福内容
        self.main_label = tk.Label(
            root, 
            text="节日快乐！愿你每天都充满阳光与喜悦！",
            font=("微软雅黑", 20),
            padx=20,
            pady=50
        )
        self.main_label.pack()
        
        # 关闭按钮，点击后显示小弹窗
        self.close_btn = tk.Button(
            root,
            text="接收祝福",
            font=("微软雅黑", 14),
            command=self.show_final_popups
        )
        self.close_btn.pack(pady=30)
    
    def show_final_popups(self):
        # 关闭主窗口
        self.root.destroy()
        # 启动小弹窗序列
        self.start_popups()
    
    # ================= 融合的小弹窗模块 =================
    TEXT_LIST = [
        "晚风绕开云朵，偷偷吻了你额头", "你眼里的星星，比银河更璀璨", "每朵云都在替我，说声喜欢你",
        "奶茶的甜，不及你笑的万分之一", "路边的花为你开，晚风为你停", "草稿本里藏的不是公式，是你的名字",
        "月亮在贩售温柔，我在贩售对你的偏爱", "你站在那里，就是整个春天的样子", "口袋里的糖分你一半，快乐分你全部",
        "星星掉进海里，你掉进我心里的柔软", "连打哈欠的弧度，都刚好长在我审美上", "风把烦恼吹到九霄，把你吹到我身边",
        "日落是橘子味的，你是心动味的", "你笑时，世界的灰度都降成了彩色", "耳机分你一半，从此歌单有了共同意义",
        "落叶写了封秋信，落款是“想见你”", "咖啡加了双倍奶泡，像你加了双倍可爱", "连影子都在模仿，我看你时的温柔",
        "把不开心折成纸飞机，让它载着烦恼飞走", "你眨眼的瞬间，我翻阅了整个银河的浪漫",
        "蝉鸣藏着夏的秘密，我藏着喜欢你的秘密", "每一步靠近，都像踩在棉花糖的甜蜜里"
    ]
    COLOR_LIST = [
        "#FFE5E5", "#E5F3FF", "#E5FFEE", "#FFF9E5",
        "#FFE5F5", "#F5E5FF", "#E5FFFB", "#FFF0E5"
    ]
    POPUP_COUNT = 50  # 保持50个弹窗
    POPUP_INTERVAL = 0.1  # 保持0.1秒弹出间隔
    POPUP_SCALE = 1.7  # 保持1.7倍弹窗尺寸

    def create_small_popup(self):
        window = tk.Tk()
        window.attributes("-topmost", True)
        window.title("心动提示")

        # 固定弹窗尺寸，计算随机位置（带安全边距）
        w = int(190 * self.POPUP_SCALE)
        h = int(65 * self.POPUP_SCALE)
        screen_w = window.winfo_screenwidth()
        screen_h = window.winfo_screenheight()
        x = random.randint(20, screen_w - w - 20)
        y = random.randint(20, screen_h - h - 20)
        window.geometry(f"{w}x{h}+{x}+{y}")

        # 随机文字与颜色
        text = random.choice(self.TEXT_LIST)
        bg_color = random.choice(self.COLOR_LIST)
        label = tk.Label(
            window, text=text, bg=bg_color, fg="#333333",
            font=("微软雅黑", int(14 * self.POPUP_SCALE)),
            padx=12, pady=12, wraplength=w-40,
            justify="center", bd=2, relief="solid"
        )
        label.pack(fill="both", expand=True)

        window.update()
        window.mainloop()

    def start_popups(self):
        # 分批启动弹窗，避免系统卡顿
        for i in range(self.POPUP_COUNT):
            if i % 5 == 0 and i != 0:
                time.sleep(0.5)
            thread = threading.Thread(target=self.create_small_popup)
            thread.daemon = False
            thread.start()
            time.sleep(self.POPUP_INTERVAL)

# 主程序入口
if __name__ == "__main__":
    root = tk.Tk()
    app = FestivalWishes(root)
    root.mainloop()