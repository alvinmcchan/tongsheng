import sxtwl
import datetime


# 宜忌示範資料（可自行擴充）
def get_yi_ji():
    yi = ["祭祀", "沐浴", "掃舍", "納財", "祈福", "會親友", "開光", "理髮"]
    ji = ["嫁娶", "安葬", "動土", "開市", "破土", "造屋", "伐木"]
    return yi, ji

def get_ganzhi_name(gz):
    """干支轉中文"""
    tiangan = "甲乙丙丁戊己庚辛壬癸"
    dizhi = "子丑寅卯辰巳午未申酉戌亥"
    return tiangan[gz.tg] + dizhi[gz.dz]

def get_shengxiao(dz):
    """地支轉生肖"""
    shengxiao = ["鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬"]
    return shengxiao[dz]

def get_chong_sha(day):
    """計算沖煞（使用日干支地支計算）"""
    dgz = day.getDayGZ()
    chong_list = ["鼠", "牛", "虎", "兔", "龍", "蛇", "馬", "羊", "猴", "雞", "狗", "豬"]
    sha_dir = ["東", "南", "西", "北"]
    
    chong_index = (dgz.dz + 6) % 12
    sha_index = dgz.dz % 4
    
    today_sx = get_shengxiao(dgz.dz)
    chong_sx = chong_list[chong_index]
    
    return f"沖 {chong_sx} 煞 {sha_dir[sha_index]}"

def get_week_cn(week_num):
    """數字轉星期中文"""
    weeks = ["日", "一", "二", "三", "四", "五", "六"]
    return weeks[week_num]

def print_tongsheng(year, month, day):
    d = sxtwl.fromSolar(year, month, day)
    
    # 公曆
    week_cn = get_week_cn(d.getWeek())
    gregorian = f"{year}年 {month}月 {day}日  星期{week_cn}"
    
    # 農曆
    lunar_year = d.getLunarYear()
    leap = "閏" if d.isLunarLeap() else ""
    lunar_month = d.getLunarMonth()
    lunar_day = d.getLunarDay()
    lunar_str = f"農曆 {lunar_year}年 {leap}{lunar_month}月 {lunar_day}日"
    
    # 干支
    ygz = get_ganzhi_name(d.getYearGZ())
    mgz = get_ganzhi_name(d.getMonthGZ())
    dgz = get_ganzhi_name(d.getDayGZ())
    ganzhi_str = f"干支：{ygz}年 {mgz}月 {dgz}日"
    
    # 衝煞
    chongsha = get_chong_sha(d)
    
    # 宜忌
    yi, ji = get_yi_ji()
    
    # 輸出
    print("=" * 65)
    print("                      通勝 / 老黃曆")
    print("=" * 65)
    print(f"公曆：{gregorian}")
    print(f"{lunar_str}")
    print(f"{ganzhi_str}")
    print(f"{chongsha}")
    print("-" * 55)
    print("宜：" + "、".join(yi))
    print("忌：" + "、".join(ji))
    print("-" * 55)
    print("※ 此為程式示範版，宜忌與衝煞僅供娛樂參考。")
    print("   傳統擇日請以專業通勝書或老師為準。")
    print("=" * 65)

def main():
    print("=== Python 通勝程式 ===\n")
    
    today = datetime.date.today()
    
    choice = input("1. 查詢今天通勝\n2. 輸入指定日期查詢\n請輸入選擇 (1 或 2)：").strip()
    
    if choice == "1":
        y, m, d = today.year, today.month, today.day
        print(f"\n今天 {y}年{m}月{d}日 的通勝：")
        print_tongsheng(y, m, d)
        
    elif choice == "2":
        try:
            date_str = input("請輸入日期 (格式：2026-03-31)：").strip()
            y, m, d = map(int, date_str.split('-'))
            print(f"\n{y}年{m}月{d}日 的通勝：")
            print_tongsheng(y, m, d)
        except Exception:
            print("輸入格式錯誤！請使用 YYYY-MM-DD 格式，例如 2026-03-31")
    else:
        print("選擇錯誤，程式結束。")

if __name__ == "__main__":
    main()

# D:\Workspace_AC\alvin_project\project\tongsheng\tongsheng.py
# pip install sxtwl
# python tongsheng.py
# 用python寫一個通勝程式
# 用python寫一個用天干地支程式, 可以輸入日期, 顯示當天的干支, 生肖, 宜忌, 衝煞等資訊    
# 用python寫一個用天干地支程式, 由1至49選出六個數字, 今天的幸運數字, 宜忌, 衝煞等資訊
# python D:\Workspace_AC\alvin_project\project\tongsheng\tongsheng.py