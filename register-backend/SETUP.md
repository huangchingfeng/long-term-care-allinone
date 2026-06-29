# 報名表單後端・部署步驟（約 3 分鐘）

報名表單（register.html）的資料會寫進一個 Google Sheet。照下面做一次就好。

## 步驟

1. **開一個新的 Google Sheet**
   到 https://sheets.new 建立一張空白試算表，命名例如「長照工具箱報名名單」。
   （表頭不用自己打，第一筆報名進來時程式會自動補上。）

2. **打開 Apps Script 編輯器**
   在這張 Sheet 上方選單：`擴充功能 → Apps Script`。

3. **貼上程式**
   把 `Code.gs` 的全部內容複製進去，蓋掉預設的 `function myFunction(){}`，按 💾 儲存。

4. **部署成 Web App**
   - 右上角 `部署 → 新增部署作業`
   - 齒輪選 `網頁應用程式 (Web app)`
   - 「執行身分」：**我（你的帳號）**
   - 「誰可以存取」：**任何人 (Anyone)** ← 一定要選這個，表單才送得進來
   - 按 `部署`，第一次會要你授權（選你的帳號 → 進階 → 前往 → 允許）

5. **複製網址**
   部署完成會給一條 `https://script.google.com/macros/s/AKfy.../exec` 的網址，整條複製。

6. **貼回表單**
   把那條網址貼進 `register.html` 裡這一行（搜 `REPLACE_WITH_YOUR_APPS_SCRIPT_URL`）：
   ```js
   var ENDPOINT = '你複製的網址';
   ```
   （或把網址傳給阿峰的 AI 助手，請它貼上並重新上線。）

## 驗證
- 部署後直接用瀏覽器開那條 `.../exec` 網址，看到「長照工具箱報名後端運作中 ✅」就代表活著。
- 到 register.html 隨便填一筆送出 → 回 Sheet 應該看到新增一列。

## 之後接 CRM / 電子報
- 這張 Sheet 的欄位（姓名/Email/電話/公司/職稱/來源/狀態/活動）已對齊 08-admin 報名 CSV，之後 n8n 可直接讀它去重、合流進總名單。
- 電子報：選 Substack（每週匯出這張 Sheet 的 Email 欄→上傳 Substack Import）或 MailerLite（n8n 自動把「電子報=願意」的人 POST 進去）。
