# uj-playable-ads

宇峻奧汀遊戲的 **HTML5 互動廣告（playable ads）** 集中庫。每支廣告一個資料夾，成品都是單一 `index.html`：素材以 base64 內嵌，離線可開、可直接上傳投放。

## 目前收錄

| 資料夾 | 遊戲 / 檔期 | 玩法 | 尺寸 | 大小 |
|---|---|---|---|---|
| [`s87-guanyu/`](s87-guanyu/) | 三國群英傳－霸王之業 ‧ S87 旁親明德（8/26 開服） | 放置掛機：庫銀累積 → 出戰／守城／強化 → 晉升官階加速 → 導預約 | 720×1280（9:16） | 1.18 MB |

線上試玩：**https://<帳號>.github.io/uj-playable-ads/**（GitHub Pages，推上去後補上實際網址）

## 每支廣告的資料夾結構

```
<ad-name>/
├── index.html          ← 成品，單一檔案、素材內嵌（投放時上傳這支）
├── src/template.html   ← 原始檔，素材為 {{BG}} 等佔位符；要改內容改這支
├── build.py            ← 把 src/template.html + assets/ 打包成 index.html
├── assets/             ← 已壓縮好的素材
└── README.md           ← 素材來源、玩法數值、投放注意
```

改完原始檔後重新打包：

```bash
python build.py
```

## 投放規格備忘

- **Meta**：單一 HTML 檔，上限 2 MB，CTA 必須呼叫 `FbPlayableAd.onCTAClick()`
- **Google**：單一 HTML 檔，上限 5 MB，CTA 呼叫 `ExitApi.exit()`
- 本庫的 CTA 都寫成通用相容：依序嘗試 `FbPlayableAd` → `ExitApi` → `mraid.open()` → `dapi.openStoreUrl()` → 開新視窗，同一支檔案兩邊都能投
- 舞台固定用 transform scale 等比置中，直式手機滿版、橫式不破版

## 素材原則

- 一律用**官方原檔**重製，不要在成品上後製疊圖
- Logo 不加襯底（scrim）
- 遊戲畫面截圖當背景時要壓暗＋微模糊，避免和自製 HUD 打架
