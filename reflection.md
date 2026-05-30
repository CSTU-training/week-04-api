<!--
 * @Author: Telliex telliexyuzo@gmail.com
 * @Date: 2026-05-30 16:22:12
 * @LastEditors: Telliex telliexyuzo@gmail.com
 * @LastEditTime: 2026-05-30 16:22:41
 * @FilePath: /week-03-api/reflection.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
## Week 3 Reflection

1. What was the most confusing thing about Python compared to JavaScript?

   Python 最讓人困惑的地方是**縮排即語法**。在 JavaScript 中，程式區塊用 `{}` 括起來，縮排只是風格問題；但在 Python 中，縮排本身就代表程式區塊的範圍，縮排錯誤會直接導致程式報錯。此外，Python 沒有 `let` / `const` / `var`，變數直接賦值即可，一開始會不太習慣。

2. What does an HTTP status code tell you? Give one example.

   HTTP 狀態碼是伺服器回應請求時附帶的三位數字，告訴客戶端「這個請求的結果是什麼」。
   例如：`404 Not Found` 表示伺服器找不到請求的資源（像是查詢一本不存在的書），`201 Created` 表示資源成功被建立（像是新增一本書後回傳的狀態）。

3. What was the difference between a path parameter and a query parameter?

   - **路徑參數 (Path parameter)**：嵌入在 URL 路徑中，用來識別特定資源。例如 `/books/3` 中的 `3` 就是路徑參數，代表 id 為 3 的書。
   - **查詢參數 (Query parameter)**：附加在 URL 的 `?` 之後，用來過濾或修飾結果。例如 `/books?status=reading` 中的 `status=reading` 就是查詢參數，表示只回傳「閱讀中」的書。

4. What would happen to all the data if you restarted the server right now? Why is that a problem, and what will we use to fix it?

   重新啟動伺服器後，所有資料都會消失。因為目前的資料存放在 `books_db`（一個 Python 列表），它只存在於記憶體（RAM）中，伺服器一關閉，記憶體就被清空。這是個問題，因為使用者新增的書籍無法被保存，每次重啟都要重頭開始。Week 4 將引入**資料庫（PostgreSQL）搭配 SQLAlchemy**，把資料持久化存到硬碟，就能解決這個問題。
