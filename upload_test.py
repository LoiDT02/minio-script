from clearml import Task, StorageManager

# Khởi tạo task
task = Task.init(project_name="MinIO-Test", task_name="upload_test")

# File cần upload
local_file = "test_file.txt"
with open(local_file, "w") as f:
    f.write("Hello ClearML + MinIO!")

# Upload file lên Storage (MinIO)
# Sử dụng StorageManager.put_file để tương thích ClearML 2.x
remote_url = StorageManager.put_file(
    local_file,
    name="test_file.txt",  # Tên file trên remote
    parent_uri="s3://mybucket/",  # URI của bucket trên MinIO
)

print(f"File uploaded to: {remote_url}")

task.close()
