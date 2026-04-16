# tongsheng

## 專案說明

本專案為一個簡易的 Python 通勝 / 天干地支工具箱，包含兩個示範程式：

- `tongsheng.py`：查詢指定日期的通勝資訊，顯示公曆、農曆、年/月/日干支、沖煞、宜忌等項目。
- `ganzhi_lucky.py`：根據天干地支產生今日幸運數字，並顯示簡單的宜忌與沖煞提示。

這些程式主要用於娛樂和學習，並非正式命理或擇日工具。實際決策請依據專業書籍或老師建議。

## 目錄結構

- `tongsheng.py`：通勝查詢主程式（需安裝 `sxtwl` 套件以取得精準農曆與干支）。
- `ganzhi_lucky.py`：簡易天干地支幸運數字程式（無須額外套件）。
- `README.md`：專案說明檔。
- `git.md`：Git 推送設定備忘錄。

## 安裝需求

建議使用 Python 3.x 環境。

如果要執行 `tongsheng.py`，請先安裝：

```bash
pip install sxtwl
```

`ganzhi_lucky.py` 則可直接執行，無需額外安裝其他套件。

## 使用方法

### 1. 查詢通勝

```bash
python tongsheng.py
```

執行後可選擇：

1. 查詢今天的通勝
2. 輸入指定日期查詢（格式：`YYYY-MM-DD`）

### 2. 取得天干地支幸運數字

```bash
python ganzhi_lucky.py
```

執行後可選擇：

1. 查詢今天
2. 輸入指定日期（格式：`YYYY-MM-DD`）

## 注意事項

- `tongsheng.py` 的宜忌與沖煞為示範資料，可根據需求自行擴充。
- `ganzhi_lucky.py` 的干支計算為簡化模擬，不保證與專業曆法輸出完全一致。
- 以上程式僅供學習與參考用途。

