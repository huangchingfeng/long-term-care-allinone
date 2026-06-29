/**
 * 長照 AI 工具箱・報名表單後端（Google Apps Script）
 * 收 register.html 送來的報名資料，寫進這個 Apps Script 綁定的 Google Sheet。
 * 欄位刻意對齊 08-admin 報名 CSV（姓名,Email,電話,公司,職稱,來源,狀態,報名時間,活動），方便日後合流進 CRM。
 *
 * 部署步驟見同資料夾 SETUP.md。
 */

// 表頭（第一次執行會自動建立）
const HEADERS = ['報名時間', '姓名', 'Email', '電話', '公司', '職稱', '來源', '電子報', '狀態', '活動'];

function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.waitLock(20000); // 避免同時寫入打架
  try {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();

    // 第一次：補表頭
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(HEADERS);
      sheet.getRange(1, 1, 1, HEADERS.length).setFontWeight('bold');
      sheet.setFrozenRows(1);
    }

    const d = JSON.parse(e.postData.contents || '{}');
    const tz = Session.getScriptTimeZone() || 'Asia/Taipei';
    const now = Utilities.formatDate(new Date(), tz, 'yyyy-MM-dd HH:mm:ss');

    sheet.appendRow([
      now,
      d.name || '',
      d.email || '',
      d.phone || '',
      d.company || '',
      d.title || '',
      d.source || '',
      d.consent || '',
      '名單',                       // 狀態：新報名一律從「名單」這個生命週期階段起算
      d.activity || '長照工具箱註冊'  // 活動：標明來源表單
    ]);

    return ContentService
      .createTextOutput(JSON.stringify({ ok: true }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ ok: false, error: String(err) }))
      .setMimeType(ContentService.MimeType.JSON);
  } finally {
    lock.releaseLock();
  }
}

// 方便測試：部署後在瀏覽器直接開 Web App 網址，看到這行就代表活著
function doGet() {
  return ContentService
    .createTextOutput('長照工具箱報名後端運作中 ✅（請用表單 POST 送資料）')
    .setMimeType(ContentService.MimeType.TEXT);
}
