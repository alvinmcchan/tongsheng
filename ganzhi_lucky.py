import datetime
import random


# 天干地支資料
TIANGAN = "甲乙丙丁戊己庚辛壬癸"
DIZHI = "子丑寅卯辰巳午未申酉戌亥"
SHENGXIAO = ["鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬"]

def get_ganzhi_name(gz_tuple):
    """把 (天干序, 地支序) 轉成文字"""
    tg, dz = gz_tuple
    return TIANGAN[tg] + DIZHI[dz]

def get_shengxiao_from_dz(dz):
    """地支轉生肖"""
    return SHENGXIAO[dz]

def calculate_lucky_numbers(day_dz):
    """根據日地支產生 6 個不重複幸運數字 (1~49)"""
    random.seed(day_dz + datetime.date.today().toordinal())  # 讓每天固定但與日干支有關
    numbers = random.sample(range(1, 50), 6)
    numbers.sort()
    return numbers

def get_chong_sha(day_dz):
    """計算沖煞"""
    chong_index = (day_dz + 6) % 12
    sha_dir = ["東", "南", "西", "北"]
    sha_index = day_dz % 4
    chong_sx = SHENGXIAO[chong_index]
    return f"沖 {chong_sx}　煞 {sha_dir[sha_index]}"

def get_yi_ji(day_dz):
    """根據日地支簡單決定宜忌（示範，可自行擴充）"""
    base_yi = ["祭祀", "沐浴", "掃舍", "納財", "會親友", "祈福"]
    base_ji = ["嫁娶", "安葬", "動土", "開市", "破土"]
    
    # 根據地支微調
    if day_dz in [0, 6]:   # 子、午
        yi = base_yi + ["出行", "開光"]
        ji = base_ji + ["伐木"]
    elif day_dz in [3, 9]: # 卯、酉
        yi = base_yi + ["理髮", "修造"]
        ji = base_ji + ["安床"]
    else:
        yi = base_yi
        ji = base_ji
    
    return yi, ji

def print_today_ganzhi_lucky(year=None, month=None, day=None):
    if not year:
        today = datetime.date.today()
        year, month, day = today.year, today.month, today.day
    
    # 簡單計算干支（這裡用模擬方式，實際精準需 sxtwl 庫）
    # 為了讓程式不需要安裝額外套件，我們用較簡單但合理的模擬
    base_year = 2024  # 2024年是甲辰年
    year_offset = (year - base_year) % 60
    year_tg = year_offset % 10
    year_dz = year_offset % 12
    
    # 月干支簡化計算（實際較複雜，這裡用近似）
    month_tg = (year_tg * 2 + month) % 10
    month_dz = (month + 1) % 12   # 粗略
    
    # 日干支用日期序號模擬（讓每天不同）
    day_num = (year * 365 + month * 31 + day) % 60
    day_tg = day_num % 10
    day_dz = day_num % 12
    
    ygz = get_ganzhi_name((year_tg, year_dz))
    mgz = get_ganzhi_name((month_tg, month_dz))
    dgz = get_ganzhi_name((day_tg, day_dz))
    
    today_sx = get_shengxiao_from_dz(day_dz)
    
    lucky_numbers = calculate_lucky_numbers(day_dz)
    chongsha = get_chong_sha(day_dz)
    yi, ji = get_yi_ji(day_dz)
    
    print("=" * 70)
    print(f"          🌟 {year}年{month}月{day}日 天干地支幸運占卜 🌟")
    print("=" * 70)
    print(f"干支：{ygz}年　{mgz}月　{dgz}日")
    print(f"生肖：{today_sx}　　{chongsha}")
    print("-" * 60)
    print(f"今日幸運數字（1~49）： {lucky_numbers}")
    print("-" * 60)
    print("宜：" + "、".join(yi))
    print("忌：" + "、".join(ji))
    print("-" * 60)
    print("※ 幸運數字與宜忌僅供娛樂參考，實際決策請理性判斷。")
    print("=" * 70)

def main():
    print("=== 天干地支幸運數字程式 ===\n")
    
    choice = input("1. 查詢今天\n2. 輸入指定日期 (格式：2026-03-31)\n請輸入選擇 (1 或 2)：").strip()
    
    if choice == "1":
        print_today_ganzhi_lucky()
    elif choice == "2":
        try:
            date_str = input("請輸入日期 (YYYY-MM-DD)：").strip()
            y, m, d = map(int, date_str.split('-'))
            print_today_ganzhi_lucky(y, m, d)
        except:
            print("日期格式錯誤！請使用 2026-03-31 格式。")
    else:
        print("輸入錯誤，程式結束。")

if __name__ == "__main__":
    main()


# 用python寫一個用天干地支程式, 由1至49選出六個數字, 今天的幸運數字, 宜忌, 衝煞等資訊
# python ganzhi_lucky.py
# python D:\Workspace_AC\alvin_project\project\tongsheng\ganzhi_lucky.py
