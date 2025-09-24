from clearml import Task, StorageManager

# Khởi tạo task ClearML
task = Task.init(
    project_name="MinIO-Test",
    task_name="upload_test",
    task_type=Task.TaskTypes.training,
)

# File cần upload
local_file = "test_file.txt"
with open(local_file, "w") as f:
    f.write("Hello ClearML + MinIO!")

# Upload file lên Storage (MinIO)
remote_path = StorageManager.upload_file(
    local_file, target_uri="s3://mybucket/test_file.txt"
)

print(f"File uploaded to: {remote_path}")

# Thông báo hoàn tất
task.close()
