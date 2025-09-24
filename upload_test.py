from clearml import Task, StorageManager

# Kết nối task với ClearML
task = Task.init(
    project_name="TestProject",
    task_name="upload_test_minio",
    task_type=Task.TaskTypes.training,
)

# Ví dụ upload một file local
local_file = "test_file.txt"

# Tạo file test
with open(local_file, "w") as f:
    f.write("Hello ClearML + MinIO!")

# Upload file lên ClearML file server (MinIO)
remote_url = StorageManager.upload_file(local_file)

print(f"File uploaded to: {remote_url}")

# Hoặc dùng task.get_logger() nếu muốn ghi log
logger = task.get_logger()
logger.report_text(f"File uploaded to {remote_url}")
