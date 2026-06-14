from storage.disk_manager import calculate_disk_blocks
from storage.io_helper import safe_create_dir
from analytics.time_validator import parse_and_inspect_date

raw_media_files = [
    {"filename": "pod_ep1.mp3", "size_bytes": 4500, "duration_sec": 180, "upload_at": "2026-06-10"},
    {"filename": "movie_trailer.mp4", "size_bytes": 105000, "duration_sec": 145, "upload_at": "2026-06-31"},
    {"filename": "clip_short.mp4", "size_bytes": 8200, "duration_sec": 15, "upload_at": "2026-05-15"}
]

def run_media_processor():
    print("======== HỆ THỐNG QUẢN LÝ LƯU TRỮ RIKKEI MEDIA =======")
    
    root_vault = "media_vault"
    safe_create_dir(root_vault)
    print("[SYSTEM] Kiểm tra hạ tầng lưu trữ... Hoàn tất.")
    
    success_count = 0
    total_files = len(raw_media_files)
    
    for file_info in raw_media_files:
        filename = file_info["filename"]
        size_bytes = file_info["size_bytes"]
        upload_date_str = file_info["upload_at"]
        
        print(f"[TỆP TIN: {filename}]")
        
        try:
            parse_and_inspect_date(upload_date_str)
            
            allocated_blocks = calculate_disk_blocks(size_bytes, block_size=4096)
            
            file_extension = filename.split(".")[-1].lower()
            category = "audio" if file_extension == "mp3" else "video"
            
            safe_create_dir(f"{root_vault}/{category}")
            
            print(f" Dung lượng thực tế: {size_bytes:,} Bytes")
            print(f" Số khối phân vùng (4KB Block): {allocated_blocks} Blocks")
            print(f" Trạng thái phân loại: HỢP LỆ (Lưu trữ vào thư mục '{category}')")
            
            success_count += 1
            
        except ValueError:
            print(f" Trạng thái phân loại: THẤT BẠI (Lỗi: Định dạng ngày upload '{upload_date_str}' không tồn tại)")
            
    print(f"TIẾN ĐỘ QUÉT: Hoàn thành xử lý {success_count}/{total_files} tệp tin thành công. Hệ thống ổn định.")

if __name__ == "__main__":
    run_media_processor()