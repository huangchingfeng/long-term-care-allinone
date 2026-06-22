#!/usr/bin/env python3
"""Generate 14 LTC microsystem demo HTML files with seed data."""

import os, json

OUT = os.path.dirname(os.path.abspath(__file__))

# --------------- shared CSS / helper -----------------
BASE_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Noto Sans TC',sans-serif;background:#f0f4f8;color:#1a202c;min-height:100vh}
.hdr{background:#0D9488;color:#fff;padding:14px 20px;display:flex;align-items:center;gap:10px}
.hdr h1{font-size:1.1rem;font-weight:700}
.badge{background:#F59E0B;color:#fff;border-radius:20px;padding:2px 10px;font-size:.75rem;white-space:nowrap}
.wrap{max-width:960px;margin:0 auto;padding:18px}
.notice{background:#FFFBEB;border:1px solid #FCD34D;border-radius:8px;padding:10px 14px;font-size:.82rem;color:#92400E;margin-bottom:16px}
h2{font-size:1rem;font-weight:700;margin:16px 0 10px;color:#134E4A}
table{width:100%;border-collapse:collapse;font-size:.87rem}
th{background:#0D9488;color:#fff;padding:8px 10px;text-align:left;font-weight:600}
td{padding:8px 10px;border-bottom:1px solid #e2e8f0}
tr:hover td{background:#f0fdfa}
.tag{display:inline-block;padding:2px 9px;border-radius:12px;font-size:.76rem;font-weight:700}
.red{background:#FEE2E2;color:#991B1B}
.yellow{background:#FEF3C7;color:#92400E}
.green{background:#DCFCE7;color:#166534}
.blue{background:#DBEAFE;color:#1E40AF}
.card{background:#fff;border-radius:10px;box-shadow:0 1px 4px rgba(0,0,0,.08);padding:16px;margin-bottom:14px}
.stat{display:inline-block;text-align:center;min-width:90px;padding:10px 14px;border-radius:8px;background:#f0fdfa;margin:4px}
.stat-n{font-size:1.6rem;font-weight:800;color:#0D9488}
.stat-l{font-size:.78rem;color:#666;margin-top:2px}
btn{cursor:pointer;padding:7px 16px;border:none;border-radius:6px;font-size:.88rem;font-weight:600}
.btn-p{background:#0D9488;color:#fff;border-radius:6px;padding:7px 16px;border:none;font-size:.88rem;font-weight:600;cursor:pointer}
.btn-p:hover{background:#0F766E}
.prog-bar{height:14px;background:#e2e8f0;border-radius:7px;overflow:hidden;margin:4px 0}
.prog-fill{height:100%;border-radius:7px;transition:width .3s}
input,select,textarea{border:1px solid #CBD5E1;border-radius:6px;padding:7px 10px;font-size:.9rem;width:100%}
label{font-size:.85rem;font-weight:600;color:#334155;display:block;margin:8px 0 3px}
"""

def page(title, body, extra_css="", extra_js=""):
    return f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — 長照微系統示範</title>
<style>
{BASE_CSS}
{extra_css}
</style>
</head>
<body>
<div class="hdr">
  <h1>🔧 {title}</h1>
  <span class="badge">示範模式</span>
</div>
<div class="wrap">
  <div class="notice">⚠️ 本頁為示範資料，所有人名、機構名均為虛構。實際使用請輸入您機構的真實資料（測試時用假代號）。</div>
{body}
</div>
{extra_js}
</body>
</html>"""


# ============================================================
# 1. 核銷單據檢核工具
# ============================================================
billing_checker_html = """
<h2>📋 核銷單據檢核 — 補助計畫示範</h2>
<div class="card" style="margin-bottom:16px">
  <b>各科目核定上限（示範）</b>
  <div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:8px">
    <span class="tag blue">人事費 120,000</span>
    <span class="tag blue">業務費 60,000</span>
    <span class="tag blue">材料費 30,000</span>
    <span class="tag blue">設備費 50,000</span>
  </div>
</div>
<div style="margin-bottom:10px;display:flex;gap:8px;align-items:center;flex-wrap:wrap">
  <span><span class="tag red">紅燈</span> 缺件或超支</span>
  <span><span class="tag yellow">黃燈</span> 請確認</span>
  <span><span class="tag green">綠燈</span> 正常</span>
</div>
<table>
<tr><th>單據編號</th><th>科目</th><th>品名／說明</th><th>金額</th><th>附件狀態</th><th>判讀</th></tr>
<tr><td>R-001</td><td>人事費</td><td>照服員 A 六月薪資</td><td>$42,000</td><td>領據✓、印領清冊✓</td><td><span class="tag green">✓ 正常</span></td></tr>
<tr><td>R-002</td><td>人事費</td><td>護理師 B 六月薪資</td><td>$52,000</td><td>領據✓、印領清冊✓</td><td><span class="tag green">✓ 正常</span></td></tr>
<tr><td>R-003</td><td>業務費</td><td>衛教文宣印製</td><td>$8,500</td><td>統一發票✓、採購單✓</td><td><span class="tag green">✓ 正常</span></td></tr>
<tr><td>R-004</td><td>業務費</td><td>講師費（外聘）</td><td>$15,000</td><td>收據✓、<b>印領清冊未附</b></td><td><span class="tag red">✗ 缺印領清冊</span></td></tr>
<tr><td>R-005</td><td>材料費</td><td>復健器材耗材</td><td>$12,800</td><td>發票✓、驗收單✓</td><td><span class="tag green">✓ 正常</span></td></tr>
<tr><td>R-006</td><td>設備費</td><td>電動床（A 廠商）</td><td>$48,000</td><td>報價單✓、採購合約✓、驗收✓</td><td><span class="tag green">✓ 正常</span></td></tr>
<tr><td>R-007</td><td>材料費</td><td>尿布耗材（5 月）</td><td>$9,600</td><td>發票✓</td><td><span class="tag yellow">⚠ 品名請確認符合材料費</span></td></tr>
<tr><td>R-008</td><td>業務費</td><td>7 月活動場地費</td><td>$18,000</td><td>收據✓</td><td><span class="tag red">⚠ 業務費累計 $41,500，加此筆超上限 $1,500</span></td></tr>
</table>
<div class="card" style="margin-top:18px">
  <b>各科目使用進度</b>
  <div style="margin-top:10px">
    <div style="margin-bottom:8px"><span style="font-size:.85rem">人事費 $94,000 / $120,000（78%）</span><div class="prog-bar"><div class="prog-fill" style="width:78%;background:#0D9488"></div></div></div>
    <div style="margin-bottom:8px"><span style="font-size:.85rem">業務費 $41,500 / $60,000（69%）—— ⚠️ R-008 若通過將超支</span><div class="prog-bar"><div class="prog-fill" style="width:69%;background:#F59E0B"></div></div></div>
    <div style="margin-bottom:8px"><span style="font-size:.85rem">材料費 $22,400 / $30,000（75%）</span><div class="prog-bar"><div class="prog-fill" style="width:75%;background:#0D9488"></div></div></div>
    <div style="margin-bottom:8px"><span style="font-size:.85rem">設備費 $48,000 / $50,000（96%）</span><div class="prog-bar"><div class="prog-fill" style="width:96%;background:#EF4444"></div></div></div>
  </div>
</div>
<div class="card" style="background:#FEF2F2;border:1px solid #FECACA;margin-top:8px">
  <b>🔴 退補件清單</b>
  <ul style="margin-top:8px;padding-left:18px;font-size:.88rem">
    <li>R-004 講師費：<b>補附印領清冊</b>（簽名蓋章）才可核銷</li>
    <li>R-008 場地費：<b>業務費已近上限</b>，送件前與主辦確認科目或申請調整</li>
  </ul>
</div>
"""

# ============================================================
# 2. 計畫經費執行進度儀表板
# ============================================================
budget_dashboard_html = """
<h2>📊 計畫經費執行進度儀表板 — 示範</h2>
<div class="card" style="display:flex;flex-wrap:wrap;gap:8px;margin-bottom:6px">
  <div class="stat"><div class="stat-n">68%</div><div class="stat-l">整體執行率</div></div>
  <div class="stat"><div class="stat-n">$680,000</div><div class="stat-l">核定總額</div></div>
  <div class="stat"><div class="stat-n">$462,800</div><div class="stat-l">已支用</div></div>
  <div class="stat"><div class="stat-n">$217,200</div><div class="stat-l">剩餘額度</div></div>
</div>
<p style="font-size:.83rem;color:#666;margin-bottom:14px">計畫期程：2026/01/01 — 2026/12/31 ｜ 目前已過 48% 時間 ｜ 執行率略超時間進度（正常）</p>
<table>
<tr><th>科目</th><th>核定金額</th><th>已支用</th><th>剩餘</th><th>執行率</th><th>狀態</th></tr>
<tr>
  <td>人事費</td><td>$320,000</td><td>$224,000</td><td>$96,000</td>
  <td><div class="prog-bar" style="width:120px;display:inline-block"><div class="prog-fill" style="width:70%;background:#0D9488"></div></div> 70%</td>
  <td><span class="tag green">✓ 正常</span></td>
</tr>
<tr>
  <td>業務費</td><td>$120,000</td><td>$109,500</td><td>$10,500</td>
  <td><div class="prog-bar" style="width:120px;display:inline-block"><div class="prog-fill" style="width:91%;background:#EF4444"></div></div> 91%</td>
  <td><span class="tag red">⚠ 即將用盡</span></td>
</tr>
<tr>
  <td>材料費</td><td>$80,000</td><td>$42,300</td><td>$37,700</td>
  <td><div class="prog-bar" style="width:120px;display:inline-block"><div class="prog-fill" style="width:53%;background:#0D9488"></div></div> 53%</td>
  <td><span class="tag green">✓ 正常</span></td>
</tr>
<tr>
  <td>設備費</td><td>$100,000</td><td>$62,000</td><td>$38,000</td>
  <td><div class="prog-bar" style="width:120px;display:inline-block"><div class="prog-fill" style="width:62%;background:#0D9488"></div></div> 62%</td>
  <td><span class="tag green">✓ 正常</span></td>
</tr>
<tr>
  <td>雜支</td><td>$60,000</td><td>$25,000</td><td>$35,000</td>
  <td><div class="prog-bar" style="width:120px;display:inline-block"><div class="prog-fill" style="width:42%;background:#F59E0B"></div></div> 42%</td>
  <td><span class="tag yellow">⚠ 進度略落後</span></td>
</tr>
</table>
<div class="card" style="margin-top:16px;background:#FEF3C7;border:1px solid #FCD34D">
  <b>📌 自動提醒</b>
  <ul style="margin-top:8px;padding-left:18px;font-size:.87rem">
    <li>業務費已用 91%，本計畫還有 6 個月，<b>建議暫停業務費新採購</b>，或向主辦申請科目調整</li>
    <li>雜支執行率較低（42%），時間已過 48%，<b>確認是否有未開立的費用單據需補送</b></li>
  </ul>
</div>
"""

# ============================================================
# 3. 評鑑佐證進度追蹤看板
# ============================================================
accreditation_board_html = """
<h2>🏆 評鑑佐證進度追蹤看板 — 示範</h2>
<div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:6px">
  <span class="stat"><span class="stat-n" style="color:#0D9488">12</span><div class="stat-l">已完成</div></span>
  <span class="stat"><span class="stat-n" style="color:#F59E0B">6</span><div class="stat-l">進行中</div></span>
  <span class="stat"><span class="stat-n" style="color:#EF4444">5</span><div class="stat-l">待完成</div></span>
</div>
<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px;margin-top:16px">

<div class="card" style="border-top:4px solid #0D9488">
  <h3 style="font-size:.9rem;color:#134E4A;margin-bottom:10px">✅ 已完成 (12)</h3>
  <div style="display:flex;flex-direction:column;gap:6px">
    <div style="background:#F0FDF4;border-radius:6px;padding:8px 10px;font-size:.83rem">📄 服務契約（住民簽署）<span class="tag green" style="float:right">✓</span></div>
    <div style="background:#F0FDF4;border-radius:6px;padding:8px 10px;font-size:.83rem">📄 個別照顧計畫（最近 1 季）<span class="tag green" style="float:right">✓</span></div>
    <div style="background:#F0FDF4;border-radius:6px;padding:8px 10px;font-size:.83rem">📄 在職教育訓練記錄（2025 年）<span class="tag green" style="float:right">✓</span></div>
    <div style="background:#F0FDF4;border-radius:6px;padding:8px 10px;font-size:.83rem">📄 緊急疏散演練記錄<span class="tag green" style="float:right">✓</span></div>
    <div style="background:#F0FDF4;border-radius:6px;padding:8px 10px;font-size:.83rem">📄 藥品管理稽核表<span class="tag green" style="float:right">✓</span></div>
    <div style="background:#F0FDF4;border-radius:6px;padding:8px 10px;font-size:.83rem">📄 感染管制月報<span class="tag green" style="float:right">✓</span></div>
    <div style="background:#F0FDF4;border-radius:6px;padding:8px 10px;font-size:.83rem">📄 身體約束紀錄 (0 件)<span class="tag green" style="float:right">✓</span></div>
    <div style="background:#F0FDF4;border-radius:6px;padding:8px 10px;font-size:.83rem">📄 住民滿意度調查<span class="tag green" style="float:right">✓</span></div>
    <div style="background:#F0FDF4;border-radius:6px;padding:8px 10px;font-size:.83rem">📄 家屬滿意度調查<span class="tag green" style="float:right">✓</span></div>
    <div style="background:#F0FDF4;border-radius:6px;padding:8px 10px;font-size:.83rem">📄 跌倒預防措施說明<span class="tag green" style="float:right">✓</span></div>
    <div style="background:#F0FDF4;border-radius:6px;padding:8px 10px;font-size:.83rem">📄 膳食及營養衛教記錄<span class="tag green" style="float:right">✓</span></div>
    <div style="background:#F0FDF4;border-radius:6px;padding:8px 10px;font-size:.83rem">📄 機構簡介與服務說明手冊<span class="tag green" style="float:right">✓</span></div>
  </div>
</div>

<div class="card" style="border-top:4px solid #F59E0B">
  <h3 style="font-size:.9rem;color:#92400E;margin-bottom:10px">🔄 進行中 (6)</h3>
  <div style="display:flex;flex-direction:column;gap:6px">
    <div style="background:#FFFBEB;border-radius:6px;padding:8px 10px;font-size:.83rem">📋 出院準備計畫（整理中）<span class="tag yellow" style="float:right">進行中</span></div>
    <div style="background:#FFFBEB;border-radius:6px;padding:8px 10px;font-size:.83rem">📋 新進員工訓練資料補齊<span class="tag yellow" style="float:right">進行中</span></div>
    <div style="background:#FFFBEB;border-radius:6px;padding:8px 10px;font-size:.83rem">📋 住民照片同意書（7 位未簽）<span class="tag yellow" style="float:right">進行中</span></div>
    <div style="background:#FFFBEB;border-radius:6px;padding:8px 10px;font-size:.83rem">📋 品管會議記錄（Q2 補開）<span class="tag yellow" style="float:right">進行中</span></div>
    <div style="background:#FFFBEB;border-radius:6px;padding:8px 10px;font-size:.83rem">📋 評鑑自評報告（撰寫中）<span class="tag yellow" style="float:right">進行中</span></div>
    <div style="background:#FFFBEB;border-radius:6px;padding:8px 10px;font-size:.83rem">📋 佐證照片整理（150 張分類中）<span class="tag yellow" style="float:right">進行中</span></div>
  </div>
</div>

<div class="card" style="border-top:4px solid #EF4444">
  <h3 style="font-size:.9rem;color:#991B1B;margin-bottom:10px">⏳ 待完成 (5)</h3>
  <div style="display:flex;flex-direction:column;gap:6px">
    <div style="background:#FEF2F2;border-radius:6px;padding:8px 10px;font-size:.83rem">❗ 消防安全演練（7/15 前）<span class="tag red" style="float:right">未開始</span></div>
    <div style="background:#FEF2F2;border-radius:6px;padding:8px 10px;font-size:.83rem">❗ 廁所防滑改善確認<span class="tag red" style="float:right">未開始</span></div>
    <div style="background:#FEF2F2;border-radius:6px;padding:8px 10px;font-size:.83rem">❗ 外聘委員委任狀更新<span class="tag red" style="float:right">未開始</span></div>
    <div style="background:#FEF2F2;border-radius:6px;padding:8px 10px;font-size:.83rem">❗ 勞務外包契約補附<span class="tag red" style="float:right">未開始</span></div>
    <div style="background:#FEF2F2;border-radius:6px;padding:8px 10px;font-size:.83rem">❗ 失智症照護訓練時數補足<span class="tag red" style="float:right">未開始</span></div>
  </div>
</div>

</div>
"""

# ============================================================
# 4. 住民自費項目帳務計算工具
# ============================================================
resident_billing_html = """
<h2>💳 住民自費項目帳務計算工具 — 示範</h2>
<table>
<tr><th>住民代號</th><th>床號</th><th>項目</th><th>單價</th><th>數量</th><th>金額</th><th>備註</th></tr>
<tr><td rowspan="4" style="font-weight:700;color:#0D9488">住民甲</td><td rowspan="4">A-101</td>
  <td>成人紙尿褲（M）</td><td>$12</td><td>90 片</td><td>$1,080</td><td>6 月份</td></tr>
<tr><td>護理耗材包</td><td>$150</td><td>4 組</td><td>$600</td><td>換藥用</td></tr>
<tr><td>物理治療費（自費）</td><td>$500</td><td>8 次</td><td>$4,000</td><td>6 月</td></tr>
<tr style="background:#f0fdfa"><td colspan="2"><b>小計</b></td><td></td><td></td><td><b>$5,680</b></td><td></td></tr>

<tr><td rowspan="3" style="font-weight:700;color:#0D9488">住民乙</td><td rowspan="3">B-205</td>
  <td>成人紙尿褲（L）</td><td>$15</td><td>60 片</td><td>$900</td><td>6 月份</td></tr>
<tr><td>失禁護理特護費</td><td>$800</td><td>1 月</td><td>$800</td><td>重度失禁</td></tr>
<tr style="background:#f0fdfa"><td colspan="2"><b>小計</b></td><td></td><td></td><td><b>$1,700</b></td><td></td></tr>

<tr><td rowspan="4" style="font-weight:700;color:#0D9488">住民丙</td><td rowspan="4">C-308</td>
  <td>特殊膳食（糖尿病餐）</td><td>$80</td><td>30 天</td><td>$2,400</td><td>6 月</td></tr>
<tr><td>氧氣使用費</td><td>$300</td><td>1 月</td><td>$300</td><td>夜間使用</td></tr>
<tr><td>外出陪同費</td><td>$600</td><td>2 次</td><td>$1,200</td><td>回診</td></tr>
<tr style="background:#f0fdfa"><td colspan="2"><b>小計</b></td><td></td><td></td><td><b>$3,900</b></td><td></td></tr>
</table>
<div class="card" style="margin-top:16px;text-align:right;font-size:1rem">
  6 月份住民自費合計：<b style="font-size:1.4rem;color:#0D9488">$11,280</b>
</div>
"""

# ============================================================
# 5. 在職訓練時數追蹤工具
# ============================================================
training_hours_html = """
<h2>📚 在職訓練時數追蹤工具 — 示範</h2>
<div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px">
  <span class="stat"><div class="stat-n">8</div><div class="stat-l">員工總數</div></span>
  <span class="stat"><div class="stat-n" style="color:#0D9488">6</div><div class="stat-l">已達標</div></span>
  <span class="stat"><div class="stat-n" style="color:#EF4444">2</div><div class="stat-l">未達標</div></span>
  <span class="stat"><div class="stat-n">20</div><div class="stat-l">年度規定時數</div></span>
</div>
<table>
<tr><th>員工代號</th><th>職稱</th><th>已完成時數</th><th>規定時數</th><th>達標率</th><th>狀態</th><th>備註</th></tr>
<tr><td>E-001</td><td>護理師</td><td>22h</td><td>20h</td>
  <td><div class="prog-bar" style="width:100px;display:inline-block"><div class="prog-fill" style="width:100%;background:#0D9488"></div></div></td>
  <td><span class="tag green">✓ 達標</span></td><td>已超時數</td></tr>
<tr><td>E-002</td><td>護理師</td><td>18h</td><td>20h</td>
  <td><div class="prog-bar" style="width:100px;display:inline-block"><div class="prog-fill" style="width:90%;background:#F59E0B"></div></div></td>
  <td><span class="tag yellow">⚠ 差 2h</span></td><td>7月還有課程</td></tr>
<tr><td>E-003</td><td>照服員</td><td>21h</td><td>20h</td>
  <td><div class="prog-bar" style="width:100px;display:inline-block"><div class="prog-fill" style="width:100%;background:#0D9488"></div></div></td>
  <td><span class="tag green">✓ 達標</span></td><td></td></tr>
<tr><td>E-004</td><td>照服員</td><td>9h</td><td>20h</td>
  <td><div class="prog-bar" style="width:100px;display:inline-block"><div class="prog-fill" style="width:45%;background:#EF4444"></div></div></td>
  <td><span class="tag red">✗ 差 11h</span></td><td>請病假多，需補訓</td></tr>
<tr><td>E-005</td><td>居服員</td><td>20h</td><td>20h</td>
  <td><div class="prog-bar" style="width:100px;display:inline-block"><div class="prog-fill" style="width:100%;background:#0D9488"></div></div></td>
  <td><span class="tag green">✓ 達標</span></td><td></td></tr>
<tr><td>E-006</td><td>社工</td><td>24h</td><td>20h</td>
  <td><div class="prog-bar" style="width:100px;display:inline-block"><div class="prog-fill" style="width:100%;background:#0D9488"></div></div></td>
  <td><span class="tag green">✓ 達標</span></td><td>外部研討會</td></tr>
<tr><td>E-007</td><td>行政人員</td><td>20h</td><td>20h</td>
  <td><div class="prog-bar" style="width:100px;display:inline-block"><div class="prog-fill" style="width:100%;background:#0D9488"></div></div></td>
  <td><span class="tag green">✓ 達標</span></td><td></td></tr>
<tr><td>E-008</td><td>廚工</td><td>6h</td><td>12h</td>
  <td><div class="prog-bar" style="width:100px;display:inline-block"><div class="prog-fill" style="width:50%;background:#EF4444"></div></div></td>
  <td><span class="tag red">✗ 差 6h</span></td><td>食安課程待完成</td></tr>
</table>
<div class="card" style="margin-top:14px;background:#FEF3C7;border:1px solid #FCD34D">
  <b>⚠️ 待補訓提醒</b>
  <ul style="margin-top:8px;padding-left:18px;font-size:.87rem">
    <li>E-004（照服員）：僅完成 9 小時，距達標差 11 小時，請安排下半年密集補訓</li>
    <li>E-008（廚工）：食安及感控課程需補 6 小時，建議 7 月份安排</li>
  </ul>
</div>
"""

# ============================================================
# 6. 補助計畫進度甘特看板
# ============================================================
gantt_html = """
<h2>📅 補助計畫進度甘特看板 — 示範</h2>
<p style="font-size:.83rem;color:#666;margin-bottom:14px">計畫名稱：社區照顧關懷據點服務強化計畫 ｜ 期程：2026/01 — 2026/12</p>
<div style="overflow-x:auto">
<table>
<tr>
  <th style="min-width:160px">工作項目</th>
  <th style="width:40px;text-align:center">1月</th><th style="width:40px;text-align:center">2月</th>
  <th style="width:40px;text-align:center">3月</th><th style="width:40px;text-align:center">4月</th>
  <th style="width:40px;text-align:center">5月</th><th style="width:40px;text-align:center">6月</th>
  <th style="width:40px;text-align:center">7月</th><th style="width:40px;text-align:center">8月</th>
  <th style="width:40px;text-align:center">9月</th><th style="width:40px;text-align:center">10月</th>
  <th style="width:40px;text-align:center">11月</th><th style="width:40px;text-align:center">12月</th>
  <th>狀態</th>
</tr>
<tr>
  <td>人員招募與訓練</td>
  <td style="background:#0D9488"></td><td style="background:#0D9488"></td>
  <td style="background:#0D9488"></td><td></td><td></td><td></td>
  <td></td><td></td><td></td><td></td><td></td><td></td>
  <td><span class="tag green">✓ 完成</span></td>
</tr>
<tr>
  <td>場地設備布置</td>
  <td style="background:#0D9488"></td><td style="background:#0D9488"></td><td></td><td></td><td></td><td></td>
  <td></td><td></td><td></td><td></td><td></td><td></td>
  <td><span class="tag green">✓ 完成</span></td>
</tr>
<tr>
  <td>社區服務推廣</td>
  <td></td><td></td>
  <td style="background:#0D9488"></td><td style="background:#0D9488"></td>
  <td style="background:#0D9488"></td><td style="background:#0D9488"></td>
  <td style="background:#0D9488"></td><td style="background:#0D9488"></td>
  <td style="background:#0D9488"></td><td style="background:#0D9488"></td>
  <td style="background:#0D9488"></td><td style="background:#0D9488"></td>
  <td><span class="tag yellow">進行中</span></td>
</tr>
<tr>
  <td>月訪視服務</td>
  <td></td><td></td>
  <td style="background:#0D9488"></td><td style="background:#0D9488"></td>
  <td style="background:#0D9488"></td><td style="background:#0D9488"></td>
  <td style="background:#0D9488"></td><td style="background:#0D9488"></td>
  <td style="background:#0D9488"></td><td style="background:#0D9488"></td>
  <td style="background:#0D9488"></td><td style="background:#0D9488"></td>
  <td><span class="tag yellow">進行中</span></td>
</tr>
<tr>
  <td>期中成果報告</td>
  <td></td><td></td><td></td><td></td><td></td>
  <td style="background:#F59E0B"></td>
  <td></td><td></td><td></td><td></td><td></td><td></td>
  <td><span class="tag yellow">⚠ 準備中</span></td>
</tr>
<tr>
  <td>期末核銷送件</td>
  <td></td><td></td><td></td><td></td><td></td><td></td>
  <td></td><td></td><td></td><td></td>
  <td style="background:#94A3B8"></td><td style="background:#94A3B8"></td>
  <td><span class="tag blue">未開始</span></td>
</tr>
<tr>
  <td>成效評估報告</td>
  <td></td><td></td><td></td><td></td><td></td><td></td>
  <td></td><td></td><td></td><td></td><td></td>
  <td style="background:#94A3B8"></td>
  <td><span class="tag blue">未開始</span></td>
</tr>
</table>
</div>
<div style="margin-top:10px;font-size:.82rem;display:flex;gap:12px">
  <span style="display:flex;align-items:center;gap:4px"><span style="display:inline-block;width:14px;height:14px;background:#0D9488;border-radius:2px"></span>進行中/完成</span>
  <span style="display:flex;align-items:center;gap:4px"><span style="display:inline-block;width:14px;height:14px;background:#F59E0B;border-radius:2px"></span>準備中</span>
  <span style="display:flex;align-items:center;gap:4px"><span style="display:inline-block;width:14px;height:14px;background:#94A3B8;border-radius:2px"></span>尚未開始</span>
</div>
"""

# ============================================================
# 7. 訪客志工登記與健康聲明系統
# ============================================================
visitor_checkin_html = """
<div style="display:flex;gap:10px;margin-bottom:12px">
  <button class="btn-p" onclick="showTab('reg')">📝 來訪登記</button>
  <button class="btn-p" onclick="showTab('list')" style="background:#475569">📋 訪客紀錄（示範資料）</button>
</div>

<div id="tab-reg">
<div class="card">
  <h2 style="margin-top:0">來訪登記表</h2>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
    <div><label>來訪者姓名</label><input placeholder="請輸入姓名"></div>
    <div><label>與住民關係</label><select><option>家屬</option><option>志工</option><option>廠商</option><option>外部訪客</option></select></div>
    <div><label>探訪住民（代號）</label><input placeholder="例：住民甲"></div>
    <div><label>來訪日期時間</label><input type="datetime-local"></div>
  </div>
  <div style="margin-top:12px;background:#FEF2F2;border-radius:8px;padding:12px">
    <b>🏥 健康聲明（請確認後勾選）</b>
    <div style="margin-top:8px;display:flex;flex-direction:column;gap:6px;font-size:.88rem">
      <label style="font-weight:400;display:flex;align-items:center;gap:8px"><input type="checkbox"> 今日無發燒、咳嗽、喉嚨痛等症狀</label>
      <label style="font-weight:400;display:flex;align-items:center;gap:8px"><input type="checkbox"> 近 14 天未接觸確診者</label>
      <label style="font-weight:400;display:flex;align-items:center;gap:8px"><input type="checkbox"> 同意接受體溫量測</label>
    </div>
  </div>
  <button class="btn-p" style="margin-top:14px" onclick="alert('示範模式：登記成功！實際系統會寫入資料庫')">確認登記</button>
</div>
</div>

<div id="tab-list" style="display:none">
<h2>訪客登記紀錄 — 示範資料（近 7 天）</h2>
<table>
<tr><th>日期時間</th><th>訪客姓名</th><th>關係</th><th>探訪住民</th><th>健康聲明</th><th>體溫</th></tr>
<tr><td>06/22 14:30</td><td>陳 ○ 明</td><td>家屬</td><td>住民甲</td><td><span class="tag green">✓ 通過</span></td><td>36.2°C</td></tr>
<tr><td>06/22 10:15</td><td>李 ○ 芬</td><td>志工</td><td>—</td><td><span class="tag green">✓ 通過</span></td><td>36.5°C</td></tr>
<tr><td>06/21 15:00</td><td>王 ○ 雄</td><td>家屬</td><td>住民乙</td><td><span class="tag green">✓ 通過</span></td><td>36.1°C</td></tr>
<tr><td>06/21 09:30</td><td>林 ○ 美</td><td>志工</td><td>—</td><td><span class="tag green">✓ 通過</span></td><td>36.3°C</td></tr>
<tr><td>06/20 16:20</td><td>張 ○ 山</td><td>家屬</td><td>住民丙</td><td><span class="tag yellow">⚠ 輕咳（補說明）</span></td><td>36.8°C</td></tr>
<tr><td>06/20 11:00</td><td>醫療器材商</td><td>廠商</td><td>—</td><td><span class="tag green">✓ 通過</span></td><td>36.4°C</td></tr>
<tr><td>06/19 14:00</td><td>吳 ○ 翠</td><td>家屬</td><td>住民甲</td><td><span class="tag green">✓ 通過</span></td><td>36.2°C</td></tr>
</table>
</div>

<script>
function showTab(t){
  document.getElementById('tab-reg').style.display=t==='reg'?'':'none';
  document.getElementById('tab-list').style.display=t==='list'?'':'none';
}
</script>
"""

# ============================================================
# 8. 照服員排班衝突檢核工具
# ============================================================
shift_checker_html = """
<h2>🗓️ 照服員排班衝突檢核工具 — 示範</h2>
<div style="margin-bottom:10px;display:flex;gap:8px;flex-wrap:wrap">
  <span><span class="tag red">紅框</span> 排班衝突</span>
  <span><span class="tag yellow">黃底</span> 人力不足</span>
  <span><span class="tag green">綠</span> 正常</span>
</div>
<div style="overflow-x:auto">
<table>
<tr><th>員工代號</th><th>職稱</th><th>週一 6/23</th><th>週二 6/24</th><th>週三 6/25</th><th>週四 6/26</th><th>週五 6/27</th><th>週六 6/28</th><th>週日 6/29</th></tr>
<tr>
  <td>C-001</td><td>照服員</td>
  <td style="background:#DCFCE7">早班</td>
  <td style="background:#DCFCE7">早班</td>
  <td style="background:#FEF3C7">早班</td>
  <td style="background:#DCFCE7">早班</td>
  <td style="background:#DCFCE7">早班</td>
  <td>休</td>
  <td>休</td>
</tr>
<tr>
  <td>C-002</td><td>照服員</td>
  <td style="background:#DCFCE7">晚班</td>
  <td style="background:#DCFCE7">晚班</td>
  <td style="background:#DCFCE7">晚班</td>
  <td style="background:#DCFCE7">晚班</td>
  <td style="background:#DCFCE7">晚班</td>
  <td style="background:#DCFCE7">晚班</td>
  <td>休</td>
</tr>
<tr>
  <td>C-003</td><td>照服員</td>
  <td>休</td>
  <td style="background:#DCFCE7">早班</td>
  <td style="background:#DCFCE7">早班</td>
  <td style="background:#DCFCE7">早班</td>
  <td>休</td>
  <td style="background:#DCFCE7">早班</td>
  <td style="background:#DCFCE7">早班</td>
</tr>
<tr>
  <td>C-004</td><td>照服員</td>
  <td style="background:#DCFCE7">早班</td>
  <td>休</td>
  <td>休</td>
  <td style="background:#DCFCE7">早班</td>
  <td style="background:#FEE2E2;border:2px solid #EF4444;font-weight:700">早+晚 ⚠️</td>
  <td style="background:#DCFCE7">早班</td>
  <td style="background:#DCFCE7">早班</td>
</tr>
<tr>
  <td>C-005</td><td>夜班照服員</td>
  <td style="background:#DBEAFE">夜班</td>
  <td style="background:#DBEAFE">夜班</td>
  <td style="background:#DBEAFE">夜班</td>
  <td>休</td>
  <td>休</td>
  <td style="background:#DBEAFE">夜班</td>
  <td style="background:#DBEAFE">夜班</td>
</tr>
</table>
</div>
<div style="overflow-x:auto;margin-top:12px">
<table>
<tr><th>時段人力</th><th>週一</th><th>週二</th><th>週三</th><th>週四</th><th>週五</th><th>週六</th><th>週日</th></tr>
<tr><td>早班（需 2 人）</td>
  <td style="background:#DCFCE7">2人✓</td>
  <td style="background:#DCFCE7">2人✓</td>
  <td style="background:#FEF3C7">1人⚠</td>
  <td style="background:#DCFCE7">2人✓</td>
  <td style="background:#DCFCE7">2人✓</td>
  <td style="background:#DCFCE7">2人✓</td>
  <td style="background:#DCFCE7">2人✓</td>
</tr>
<tr><td>晚班（需 1 人）</td>
  <td style="background:#DCFCE7">1人✓</td>
  <td style="background:#DCFCE7">1人✓</td>
  <td style="background:#DCFCE7">1人✓</td>
  <td style="background:#DCFCE7">1人✓</td>
  <td style="background:#DCFCE7">1人✓</td>
  <td style="background:#DCFCE7">1人✓</td>
  <td style="background:#FEF3C7">0人⚠</td>
</tr>
</table>
</div>
<div class="card" style="margin-top:14px;background:#FEF2F2;border:1px solid #FECACA">
  <b>🔴 衝突提醒</b>
  <ul style="margin-top:8px;padding-left:18px;font-size:.87rem">
    <li>C-004 週五（6/27）同時被排早班與晚班，請確認並修正</li>
    <li>週三早班只有 1 人（C-001 請假），需調補人力</li>
    <li>週日晚班無人，需安排備班</li>
  </ul>
</div>
"""

# ============================================================
# 9. 活動報名＋簽到＋滿意度系統
# ============================================================
activity_signin_html = """
<div style="display:flex;gap:10px;margin-bottom:12px;flex-wrap:wrap">
  <button class="btn-p" onclick="showTab('info')">📋 活動資訊</button>
  <button class="btn-p" onclick="showTab('signin')" style="background:#475569">✅ 簽到紀錄</button>
  <button class="btn-p" onclick="showTab('survey')" style="background:#475569">📊 滿意度統計</button>
</div>

<div id="tab-info">
<div class="card">
  <h2 style="margin-top:0">🎉 六月份健康促進活動</h2>
  <table style="margin-top:8px">
    <tr><td style="width:100px;color:#666">活動名稱</td><td><b>長輩體適能與音樂律動</b></td></tr>
    <tr><td>日期時間</td><td>2026/06/25（三）09:30–11:30</td></tr>
    <tr><td>地點</td><td>機構多功能活動室</td></tr>
    <tr><td>帶領者</td><td>職能治療師 A</td></tr>
    <tr><td>報名人數</td><td>12 人（住民 10 + 家屬 2）</td></tr>
    <tr><td>實到人數</td><td>10 人</td></tr>
    <tr><td>缺席</td><td>住民代號 E-003（身體不適）、住民代號 E-007（外出回診）</td></tr>
  </table>
</div>
</div>

<div id="tab-signin" style="display:none">
<h2>✅ 簽到紀錄 — 示範資料</h2>
<table>
<tr><th>序</th><th>參與者代號</th><th>身分</th><th>簽到時間</th><th>狀態</th><th>備註</th></tr>
<tr><td>1</td><td>住民 A-001</td><td>住民</td><td>09:25</td><td><span class="tag green">✓ 出席</span></td><td></td></tr>
<tr><td>2</td><td>住民 A-002</td><td>住民</td><td>09:28</td><td><span class="tag green">✓ 出席</span></td><td></td></tr>
<tr><td>3</td><td>住民 A-004</td><td>住民</td><td>09:30</td><td><span class="tag green">✓ 出席</span></td><td></td></tr>
<tr><td>4</td><td>住民 A-005</td><td>住民</td><td>09:32</td><td><span class="tag green">✓ 出席</span></td><td></td></tr>
<tr><td>5</td><td>住民 A-006</td><td>住民</td><td>09:31</td><td><span class="tag green">✓ 出席</span></td><td></td></tr>
<tr><td>6</td><td>住民 A-008</td><td>住民</td><td>09:35</td><td><span class="tag green">✓ 出席</span></td><td>輪椅參與</td></tr>
<tr><td>7</td><td>住民 A-009</td><td>住民</td><td>09:29</td><td><span class="tag green">✓ 出席</span></td><td></td></tr>
<tr><td>8</td><td>住民 A-010</td><td>住民</td><td>09:33</td><td><span class="tag green">✓ 出席</span></td><td></td></tr>
<tr><td>9</td><td>家屬代甲</td><td>家屬</td><td>09:30</td><td><span class="tag green">✓ 出席</span></td><td>陪同住民甲</td></tr>
<tr><td>10</td><td>家屬代乙</td><td>家屬</td><td>09:45</td><td><span class="tag green">✓ 出席</span></td><td>遲到</td></tr>
<tr><td>—</td><td>住民 E-003</td><td>住民</td><td>—</td><td><span class="tag red">✗ 缺席</span></td><td>身體不適</td></tr>
<tr><td>—</td><td>住民 E-007</td><td>住民</td><td>—</td><td><span class="tag yellow">外出</span></td><td>回診</td></tr>
</table>
</div>

<div id="tab-survey" style="display:none">
<h2>📊 滿意度統計 — 示範資料（有效問卷 9 份）</h2>
<div class="card">
  <b>整體滿意度</b>
  <div style="font-size:2rem;font-weight:800;color:#0D9488;margin:8px 0">4.7 / 5</div>
  <div style="display:flex;flex-direction:column;gap:6px;margin-top:8px">
    <div><span style="font-size:.85rem">非常滿意（5）</span><div class="prog-bar"><div class="prog-fill" style="width:67%;background:#0D9488"></div></div><span style="font-size:.8rem">6 人（67%）</span></div>
    <div><span style="font-size:.85rem">滿意（4）</span><div class="prog-bar"><div class="prog-fill" style="width:22%;background:#22C55E"></div></div><span style="font-size:.8rem">2 人（22%）</span></div>
    <div><span style="font-size:.85rem">普通（3）</span><div class="prog-bar"><div class="prog-fill" style="width:11%;background:#F59E0B"></div></div><span style="font-size:.8rem">1 人（11%）</span></div>
  </div>
</div>
<div class="card" style="margin-top:8px">
  <b>💬 文字回饋（示範）</b>
  <ul style="margin-top:8px;font-size:.87rem;padding-left:18px">
    <li>「老人家很開心，笑聲很多」</li>
    <li>「帶領者有耐心，動作示範清楚」</li>
    <li>「時間太短，希望多辦幾次」</li>
    <li>「音樂選得好，很有氣氛」</li>
  </ul>
</div>
</div>

<script>
function showTab(t){
  ['info','signin','survey'].forEach(function(id){
    document.getElementById('tab-'+id).style.display=(id===t?'':'none');
  });
}
</script>
"""

# ============================================================
# 10. 家屬通知訊息產生器
# ============================================================
family_notice_html = """
<h2>💬 家屬通知訊息產生器 — 示範</h2>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px">
<div>
  <div class="card">
    <h3 style="font-size:.95rem;margin-bottom:12px">填寫內容</h3>
    <label>住民代號</label><input id="nm" value="住民甲">
    <label>通知主旨</label>
    <select id="tp">
      <option>近況說明</option>
      <option>用藥調整</option>
      <option>返家探視建議</option>
      <option>醫療異常通報</option>
      <option>活動邀請</option>
    </select>
    <label>具體說明</label>
    <textarea id="detail" rows="3" placeholder="請填寫說明（示範：近一週食量略減，已請護理師追蹤）">近一週食量略減，已請護理師追蹤，生命徵象穩定，請家屬留意。</textarea>
    <label>建議家屬動作</label><input id="action" value="如有疑問歡迎致電機構或安排探視">
    <button class="btn-p" style="margin-top:10px;width:100%" onclick="generate()">🔄 產生通知</button>
  </div>
</div>
<div>
  <div class="card">
    <h3 style="font-size:.95rem;margin-bottom:8px">📄 產生的通知（可複製發送）</h3>
    <div id="output" style="background:#f8fafc;border-radius:8px;padding:12px;font-size:.87rem;min-height:180px;white-space:pre-wrap;line-height:1.7"></div>
    <button class="btn-p" style="margin-top:10px;width:100%;background:#475569" onclick="copyMsg()">📋 複製訊息</button>
  </div>
  <div class="card" style="margin-top:10px">
    <b>📌 範例通知</b>
    <div style="font-size:.83rem;color:#475569;margin-top:6px;background:#f8fafc;padding:10px;border-radius:6px;line-height:1.7">親愛的家屬，您好：<br>
住民甲近況說明：本週體溫、血壓、血氧均正常，精神狀況良好，有參與院內音樂活動，反應不錯。<br>
如有任何疑問，歡迎致電機構或預約探視，謝謝您的關心。<br>
——○○長照機構 護理站</div>
  </div>
</div>
</div>
<script>
function generate(){
  var nm=document.getElementById('nm').value||'住民';
  var tp=document.getElementById('tp').value;
  var detail=document.getElementById('detail').value;
  var action=document.getElementById('action').value;
  var date=new Date().toLocaleDateString('zh-TW');
  var msg='親愛的家屬，您好：\\n\\n' +
    '以下是關於 '+nm+' 的'+tp+'通知（'+date+'）：\\n\\n'+
    detail+'\\n\\n'+
    '建議：'+action+'\\n\\n'+
    '如有任何疑問，歡迎來電洽詢，謝謝您。\\n——機構護理站';
  document.getElementById('output').textContent=msg;
}
function copyMsg(){
  var t=document.getElementById('output').textContent;
  if(!t){alert('請先產生通知');return;}
  navigator.clipboard.writeText(t).then(function(){alert('已複製！可貼到 LINE 傳送');});
}
generate();
</script>
"""

# ============================================================
# 11. 藥品衛材效期＋庫存提醒工具
# ============================================================
supply_expiry_html = """
<h2>💊 藥品衛材效期＋庫存提醒工具 — 示範</h2>
<div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px">
  <span class="stat"><div class="stat-n" style="color:#EF4444">3</div><div class="stat-l">即將到期（30天內）</div></span>
  <span class="stat"><div class="stat-n" style="color:#F59E0B">2</div><div class="stat-l">庫存偏低</div></span>
  <span class="stat"><div class="stat-n" style="color:#0D9488">9</div><div class="stat-l">正常</div></span>
</div>
<table>
<tr><th>品項名稱</th><th>類型</th><th>庫存量</th><th>安全庫存</th><th>有效日期</th><th>效期狀態</th><th>庫存狀態</th></tr>
<tr><td>血壓計電池 (AA)</td><td>衛材</td><td>8 顆</td><td>20 顆</td><td>2028/12/31</td><td><span class="tag green">✓</span></td><td><span class="tag red">⚠ 庫存不足</span></td></tr>
<tr><td>酒精棉片 (100片/盒)</td><td>耗材</td><td>12 盒</td><td>10 盒</td><td>2027/06/30</td><td><span class="tag green">✓</span></td><td><span class="tag green">✓</span></td></tr>
<tr><td>防水膠帶</td><td>耗材</td><td>5 捲</td><td>5 捲</td><td>2026/07/10</td><td><span class="tag red">⚠ 18天後到期</span></td><td><span class="tag yellow">庫存剛好</span></td></tr>
<tr><td>乳膠手套 (M)</td><td>耗材</td><td>200 雙</td><td>100 雙</td><td>2027/03/31</td><td><span class="tag green">✓</span></td><td><span class="tag green">✓</span></td></tr>
<tr><td>生理食鹽水 250mL</td><td>藥品</td><td>24 瓶</td><td>20 瓶</td><td>2026/07/25</td><td><span class="tag red">⚠ 33天後到期</span></td><td><span class="tag green">✓</span></td></tr>
<tr><td>體溫貼片</td><td>耗材</td><td>3 包</td><td>10 包</td><td>2026/09/30</td><td><span class="tag green">✓</span></td><td><span class="tag red">⚠ 庫存不足</span></td></tr>
<tr><td>優碘 (100mL)</td><td>藥品</td><td>6 瓶</td><td>5 瓶</td><td>2026/07/01</td><td><span class="tag red">⚠ 9天後到期</span></td><td><span class="tag green">✓</span></td></tr>
<tr><td>彈性繃帶 (3吋)</td><td>耗材</td><td>20 捲</td><td>10 捲</td><td>2028/01/15</td><td><span class="tag green">✓</span></td><td><span class="tag green">✓</span></td></tr>
<tr><td>量血糖試紙</td><td>耗材</td><td>3 盒</td><td>5 盒</td><td>2026/10/31</td><td><span class="tag green">✓</span></td><td><span class="tag yellow">⚠ 略偏低</span></td></tr>
<tr><td>口罩 (醫用) 50入/盒</td><td>耗材</td><td>15 盒</td><td>10 盒</td><td>2027/08/31</td><td><span class="tag green">✓</span></td><td><span class="tag green">✓</span></td></tr>
<tr><td>無菌紗布塊</td><td>耗材</td><td>10 包</td><td>8 包</td><td>2027/12/31</td><td><span class="tag green">✓</span></td><td><span class="tag green">✓</span></td></tr>
<tr><td>護膚乳液 (大)</td><td>日用</td><td>8 瓶</td><td>6 瓶</td><td>2027/04/30</td><td><span class="tag green">✓</span></td><td><span class="tag green">✓</span></td></tr>
</table>
<div class="card" style="margin-top:14px;background:#FEF2F2;border:1px solid #FECACA">
  <b>🔴 即刻行動清單</b>
  <ul style="margin-top:8px;padding-left:18px;font-size:.87rem">
    <li>優碘：9 天後到期，<b>立即確認是否需補購或提前使用完畢</b></li>
    <li>防水膠帶：18 天後到期，請評估庫存是否足夠或補購</li>
    <li>血壓計電池：庫存 8 顆低於安全庫存 20 顆，<b>本週補購</b></li>
    <li>體溫貼片：僅剩 3 包，安全庫存為 10 包，<b>補購中</b></li>
  </ul>
</div>
"""

# ============================================================
# 12. 跌倒異常事件通報＋月統計工具
# ============================================================
incident_report_html = """
<div style="display:flex;gap:10px;margin-bottom:12px;flex-wrap:wrap">
  <button class="btn-p" onclick="showTab('form')">📝 填寫通報</button>
  <button class="btn-p" onclick="showTab('stats')" style="background:#475569">📊 本月統計</button>
  <button class="btn-p" onclick="showTab('log')" style="background:#475569">📋 通報紀錄</button>
</div>

<div id="tab-form">
<div class="card">
  <h2 style="margin-top:0">事件通報表單</h2>
  <div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">
    <div><label>事件類型</label>
    <select><option>跌倒</option><option>壓傷</option><option>異食</option><option>走失</option><option>藥物不良反應</option><option>其他</option></select></div>
    <div><label>當事人代號</label><input placeholder="例：住民甲"></div>
    <div><label>發生日期時間</label><input type="datetime-local"></div>
    <div><label>發現者代號</label><input placeholder="員工代號"></div>
    <div style="grid-column:1/-1"><label>事件經過（去識別化）</label>
    <textarea rows="3" placeholder="請用代號描述事件，不要填真實姓名、病歷號"></textarea></div>
    <div><label>立即處置</label><textarea rows="2" placeholder="已採取的處置措施"></textarea></div>
    <div><label>傷害程度</label>
    <select><option>無傷害</option><option>輕微（皮膚擦傷）</option><option>中度（需就醫）</option><option>嚴重（住院）</option></select></div>
  </div>
  <button class="btn-p" style="margin-top:12px" onclick="alert('示範模式：通報已提交！實際系統會存入資料庫並寄送主管通知')">📨 提交通報</button>
</div>
</div>

<div id="tab-stats" style="display:none">
<h2>📊 2026年6月 事件統計 — 示範資料</h2>
<div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:12px">
  <span class="stat"><div class="stat-n" style="color:#EF4444">8</div><div class="stat-l">本月事件總數</div></span>
  <span class="stat"><div class="stat-n" style="color:#F59E0B">5</div><div class="stat-l">跌倒</div></span>
  <span class="stat"><div class="stat-n" style="color:#0D9488">2</div><div class="stat-l">壓傷</div></span>
  <span class="stat"><div class="stat-n" style="color:#6366F1">1</div><div class="stat-l">其他</div></span>
</div>
<div class="card">
  <b>跌倒事件分析</b>
  <table style="margin-top:8px">
    <tr><th>時段</th><th>次數</th><th>比例</th></tr>
    <tr><td>早班（07:00–15:00）</td><td>2次</td><td><div class="prog-bar" style="width:150px;display:inline-block"><div class="prog-fill" style="width:40%;background:#0D9488"></div></div></td></tr>
    <tr><td>晚班（15:00–23:00）</td><td>1次</td><td><div class="prog-bar" style="width:150px;display:inline-block"><div class="prog-fill" style="width:20%;background:#F59E0B"></div></div></td></tr>
    <tr><td>夜班（23:00–07:00）</td><td>2次</td><td><div class="prog-bar" style="width:150px;display:inline-block"><div class="prog-fill" style="width:40%;background:#EF4444"></div></div></td></tr>
  </table>
</div>
<div class="card" style="margin-top:8px">
  <b>發生地點</b>
  <table style="margin-top:8px">
    <tr><th>地點</th><th>次數</th></tr>
    <tr><td>浴室 / 廁所</td><td>2</td></tr>
    <tr><td>床邊</td><td>2</td></tr>
    <tr><td>走廊</td><td>1</td></tr>
  </table>
</div>
<div class="card" style="margin-top:8px;background:#FEF3C7;border:1px solid #FCD34D">
  <b>💡 改善建議（AI 自動分析）</b>
  <ul style="margin-top:8px;padding-left:18px;font-size:.87rem">
    <li>夜班跌倒比例偏高，建議加強夜間巡視頻率（每 2 小時一次）</li>
    <li>浴室跌倒 2 次，建議檢查防滑墊狀況及扶手安裝</li>
    <li>高跌倒風險住民名單（代號）本月應加強跌倒預防介入</li>
  </ul>
</div>
</div>

<div id="tab-log" style="display:none">
<h2>📋 6月通報紀錄 — 示範資料</h2>
<table>
<tr><th>日期</th><th>類型</th><th>當事人</th><th>地點</th><th>傷害程度</th><th>處置</th></tr>
<tr><td>06/21</td><td>跌倒</td><td>住民代甲</td><td>浴室</td><td><span class="tag yellow">輕微</span></td><td>消毒包紮、通知家屬</td></tr>
<tr><td>06/19</td><td>壓傷</td><td>住民代乙</td><td>臥室</td><td><span class="tag yellow">輕微</span></td><td>換藥、調整翻身頻率</td></tr>
<tr><td>06/17</td><td>跌倒</td><td>住民代丙</td><td>走廊</td><td><span class="tag green">無傷</span></td><td>協助站立、評估步態</td></tr>
<tr><td>06/15</td><td>跌倒</td><td>住民代甲</td><td>床邊</td><td><span class="tag yellow">輕微</span></td><td>X 光確認無骨折</td></tr>
<tr><td>06/12</td><td>壓傷</td><td>住民代丁</td><td>臥室</td><td><span class="tag red">中度</span></td><td>護理處置、回診追蹤</td></tr>
<tr><td>06/08</td><td>跌倒</td><td>住民代戊</td><td>廁所</td><td><span class="tag green">無傷</span></td><td>增加夜間巡視</td></tr>
<tr><td>06/05</td><td>跌倒</td><td>住民代己</td><td>床邊</td><td><span class="tag yellow">輕微</span></td><td>消毒、通知家屬</td></tr>
<tr><td>06/02</td><td>其他</td><td>住民代庚</td><td>活動室</td><td><span class="tag green">無傷</span></td><td>安撫、記錄行為</td></tr>
</table>
</div>

<script>
function showTab(t){
  ['form','stats','log'].forEach(function(id){
    document.getElementById('tab-'+id).style.display=(id===t?'':'none');
  });
}
</script>
"""

# ============================================================
# 13. 長輩日常作息與活動參與紀錄表
# ============================================================
daily_routine_html = """
<h2>📒 長輩日常作息與活動參與紀錄表 — 示範</h2>
<p style="font-size:.83rem;color:#666;margin-bottom:12px">記錄日期：2026/06/22（週一）｜ 記錄員：照服員C-001</p>
<table>
<tr>
  <th rowspan="2">住民代號</th>
  <th colspan="4">飲食</th>
  <th colspan="3">活動參與</th>
  <th colspan="2">排泄</th>
  <th>睡眠</th>
  <th>備註</th>
</tr>
<tr>
  <th>早餐</th><th>午餐</th><th>晚餐</th><th>水分</th>
  <th>晨操</th><th>午間活動</th><th>下午手工</th>
  <th>排便</th><th>尿量</th>
  <th>午睡</th>
  <th></th>
</tr>
<tr>
  <td style="font-weight:700;color:#0D9488">住民甲</td>
  <td><span class="tag green">全</span></td>
  <td><span class="tag green">全</span></td>
  <td><span class="tag yellow">半</span></td>
  <td>1200cc</td>
  <td><span class="tag green">參與</span></td>
  <td><span class="tag green">參與</span></td>
  <td><span class="tag green">參與</span></td>
  <td>正常</td>
  <td>正常</td>
  <td>1.5h</td>
  <td>晚餐食量略減</td>
</tr>
<tr>
  <td style="font-weight:700;color:#0D9488">住民乙</td>
  <td><span class="tag yellow">半</span></td>
  <td><span class="tag green">全</span></td>
  <td><span class="tag green">全</span></td>
  <td>800cc</td>
  <td><span class="tag red">未參與</span></td>
  <td><span class="tag green">參與</span></td>
  <td><span class="tag red">未參與</span></td>
  <td>未排</td>
  <td>正常</td>
  <td>2h</td>
  <td>早起情緒不佳，後改善</td>
</tr>
<tr>
  <td style="font-weight:700;color:#0D9488">住民丙</td>
  <td><span class="tag green">全</span></td>
  <td><span class="tag green">全</span></td>
  <td><span class="tag green">全</span></td>
  <td>1500cc</td>
  <td><span class="tag green">參與</span></td>
  <td><span class="tag yellow">部分</span></td>
  <td><span class="tag green">參與</span></td>
  <td>正常</td>
  <td>正常</td>
  <td>1h</td>
  <td>午間活動提早離席（疲倦）</td>
</tr>
<tr>
  <td style="font-weight:700;color:#0D9488">住民丁</td>
  <td><span class="tag red">未用</span></td>
  <td><span class="tag yellow">半</span></td>
  <td><span class="tag yellow">半</span></td>
  <td>600cc</td>
  <td><span class="tag red">未參與</span></td>
  <td><span class="tag red">未參與</span></td>
  <td><span class="tag red">未參與</span></td>
  <td>未排</td>
  <td>偏少</td>
  <td>3h</td>
  <td><span class="tag red">⚠ 食慾差、少動，須追蹤</span></td>
</tr>
<tr>
  <td style="font-weight:700;color:#0D9488">住民戊</td>
  <td><span class="tag green">全</span></td>
  <td><span class="tag green">全</span></td>
  <td><span class="tag green">全</span></td>
  <td>1300cc</td>
  <td><span class="tag green">參與</span></td>
  <td><span class="tag green">參與</span></td>
  <td><span class="tag yellow">部分</span></td>
  <td>正常</td>
  <td>正常</td>
  <td>1.5h</td>
  <td></td>
</tr>
</table>
<div class="card" style="margin-top:14px;background:#FEF2F2;border:1px solid #FECACA">
  <b>📌 今日異常追蹤</b>
  <ul style="margin-top:8px;padding-left:18px;font-size:.87rem">
    <li>住民丁：全日食慾差、水分攝取不足、無活動參與，建議通知護理師評估，並聯繫家屬</li>
    <li>住民乙：兩天未排便，請確認排便促進措施是否執行</li>
  </ul>
</div>
"""

# ============================================================
# 14. 接送排班路線小工具
# ============================================================
transport_scheduler_html = """
<h2>🚐 接送排班路線小工具 — 示範</h2>
<p style="font-size:.83rem;color:#666;margin-bottom:12px">本週排班：2026/06/23（一）—— 06/27（五）｜ 日照中心</p>
<div style="overflow-x:auto">
<table>
<tr><th>路線</th><th>司機代號</th><th>車輛</th><th>週一</th><th>週二</th><th>週三</th><th>週四</th><th>週五</th><th>接送人數</th></tr>
<tr>
  <td><b>路線甲</b><br><span style="font-size:.78rem;color:#666">北區 → 機構</span></td>
  <td>D-001</td><td>中型廂車</td>
  <td style="background:#DCFCE7">06:50出發</td>
  <td style="background:#DCFCE7">06:50出發</td>
  <td style="background:#DCFCE7">06:50出發</td>
  <td style="background:#DCFCE7">06:50出發</td>
  <td style="background:#DCFCE7">06:50出發</td>
  <td>5人（4長輩+1陪同）</td>
</tr>
<tr>
  <td><b>路線乙</b><br><span style="font-size:.78rem;color:#666">南區 → 機構</span></td>
  <td>D-002</td><td>小型廂車</td>
  <td style="background:#DCFCE7">07:10出發</td>
  <td style="background:#DCFCE7">07:10出發</td>
  <td style="background:#FEF3C7">D-003 代班</td>
  <td style="background:#DCFCE7">07:10出發</td>
  <td style="background:#DCFCE7">07:10出發</td>
  <td>4人</td>
</tr>
<tr>
  <td><b>路線丙</b><br><span style="font-size:.78rem;color:#666">東區 → 機構</span></td>
  <td>D-003</td><td>無障礙車</td>
  <td style="background:#DCFCE7">07:30出發</td>
  <td style="background:#FEE2E2;border:2px solid #EF4444">⚠ 車輛保養</td>
  <td style="background:#DCFCE7">07:30出發</td>
  <td style="background:#DCFCE7">07:30出發</td>
  <td style="background:#DCFCE7">07:30出發</td>
  <td>3人（含輪椅2）</td>
</tr>
<tr>
  <td><b>路線丁</b><br><span style="font-size:.78rem;color:#666">市區 → 回診接送</span></td>
  <td>D-001</td><td>中型廂車</td>
  <td>—</td>
  <td>—</td>
  <td style="background:#DBEAFE">13:00 出發</td>
  <td>—</td>
  <td>—</td>
  <td>2人（週三醫院回診）</td>
</tr>
</table>
</div>
<div class="card" style="margin-top:14px">
  <b>📋 本週注意事項</b>
  <ul style="padding-left:18px;font-size:.87rem;margin-top:8px">
    <li>路線丙週二（6/24）車輛定期保養，已安排 D-002 小型廂車代送（載客數 3 人，需確認輪椅可否折疊）</li>
    <li>路線乙週三 D-003 代班（因支援路線丙），請確認乙路線住民已告知家屬</li>
    <li>週三下午路線丁：回診接送需提前聯繫醫院停車接送入口</li>
  </ul>
</div>
<div class="card" style="margin-top:10px">
  <b>📍 本週接送人員名冊（去識別化）</b>
  <table style="margin-top:8px;font-size:.85rem">
    <tr><th>代號</th><th>路線</th><th>特殊需求</th><th>緊急聯絡人</th></tr>
    <tr><td>住民代 P-01</td><td>路線甲</td><td>無</td><td>家屬甲（已留號）</td></tr>
    <tr><td>住民代 P-02</td><td>路線甲</td><td>糖尿病飲食</td><td>家屬乙</td></tr>
    <tr><td>住民代 P-05</td><td>路線丙</td><td>電動輪椅</td><td>家屬丙</td></tr>
    <tr><td>住民代 P-06</td><td>路線丙</td><td>手動輪椅</td><td>家屬丁</td></tr>
    <tr><td>住民代 P-09</td><td>路線乙</td><td>行動緩慢</td><td>家屬戊</td></tr>
  </table>
</div>
"""

# ============================================================
# Write all files
# ============================================================

demos = [
    ("manus-billing-checker.html",       "核銷單據檢核工具",           billing_checker_html),
    ("manus-budget-dashboard.html",      "計畫經費執行進度儀表板",     budget_dashboard_html),
    ("manus-accreditation-board.html",   "評鑑佐證進度追蹤看板",       accreditation_board_html),
    ("manus-resident-self-pay-billing.html", "住民自費項目帳務計算工具", resident_billing_html),
    ("manus-training-hours-tracker.html","在職訓練時數追蹤工具",       training_hours_html),
    ("manus-subsidy-gantt-board.html",   "補助計畫進度甘特看板",       gantt_html),
    ("manus-visitor-volunteer-checkin.html","訪客志工登記與健康聲明系統", visitor_checkin_html),
    ("manus-shift-conflict-checker.html","照服員排班衝突檢核工具",     shift_checker_html),
    ("manus-activity-signin-survey.html","活動報名＋簽到＋滿意度系統", activity_signin_html),
    ("manus-family-notice-generator.html","家屬通知訊息產生器",        family_notice_html),
    ("manus-supply-expiry-stock.html",   "藥品衛材效期＋庫存提醒工具", supply_expiry_html),
    ("manus-incident-report-stats.html", "跌倒異常事件通報＋月統計工具", incident_report_html),
    ("manus-daily-routine-log.html",     "長輩日常作息與活動參與紀錄表", daily_routine_html),
    ("manus-transport-route-scheduler.html","接送排班路線小工具",      transport_scheduler_html),
]

for fname, title, body in demos:
    html = page(title, body)
    path = os.path.join(OUT, fname)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ {fname}")

print(f"\n生成完成：{len(demos)} 個示範頁面")
