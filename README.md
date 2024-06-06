# package_segment
## 需求項目
- 支援箱體於速度100cm/s 輸送帶移動
- 支援回饋物體於影像相對座標
- 支援複數箱體並行移動，並回饋複數箱相對座標
- 支援複數攝影機，滿足多角度偵測

## 問題處理
- 箱子堵塞
- 一箱多物
- 箱體通過紅光

## YOLOv8方法
### 偵測

## Roboflow平台
- 所需的訓練資料集容易取得
- 線上平台工具做圖片標註以及有智慧工具輔助標註
- 可以依比例做訓練資料分配
- 可以對圖片做到不同動作改變的隨機擴增
- 有些開源資料集提供線上偵測功能
### Roboflow方法
- 資料隨機擴增

## 訓練軟硬體設備
| Hardware | PC | Server |
|:-------:|:---------:|:-------:|
| Pre-train model | YOLOv8n-seg.pt |YOLOv8x-seg.pt|
| System|Ubuntu 20.04| Ubuntu 20.04|
| GPU| Nvidia GeForce RTX 3060-TI 8G| Nvidia GeForce RTX 3060-TI 8G|
| CUDA| 11.8   | 11.8 |
| Epoch| 50  | 50 |
| Python| 3.11.5 | 3.11.5 |







