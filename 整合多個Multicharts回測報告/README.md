## 整合多個Multicharts回測報告

因為目前有在使用Multicharts寫些小策略，但是用的是券商閹割版，沒有投資組合多個策略一起回測的功能，所以做了個小工具，將各策略的回測報告，組合起來，並產出我所需要看的資訊。

### 使用說明

* 須注意檔名要有 [**策略回測績效報告**] 字串
* 目前起始金額寫死20萬，單邊手續費50
* 若策略貨幣非台幣，需開啟檔案將 [**獲利(¤)**] 手動調整成台幣

[程式碼](https://github.com/HankGuo93/python_ToolForWork/blob/master/%E6%95%B4%E5%90%88%E5%A4%9A%E5%80%8BMulticharts%E5%9B%9E%E6%B8%AC%E5%A0%B1%E5%91%8A/PortfolioManager_Beta.md)
