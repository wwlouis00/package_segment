# 影片分割成圖片
import cv2 as cv

# 打開影片文件
video_path = '/home/wwlouis/project/Dataset/兆輝科技物流影片/智慧物流/05_11_19_00_46.mp4'  # 替換為您的影片文件路徑

cap = cv.VideoCapture(video_path)

# 確保影片文件成功打開
if not cap.isOpened():
    print("無法打開影片文件")
    exit()

frame_count = 0

while True:
    # 讀取一帧
    ret, frame = cap.read()
    # 如果影片結束，則退出循環
    if not ret:
        break
    # 保存當前幀為圖像文件
    output_file = f"video/frame_{frame_count}.jpg"  # 每個幀都保存為一個單獨的圖像文件
    cv.imwrite(output_file, frame)
    
    frame_count += 1

# 釋放影片文件
cap.release()

print(f"共分割了 {frame_count} 幀圖像")
