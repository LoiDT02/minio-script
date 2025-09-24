from clearml import Task

# Tạo task
task1 = Task.init(project_name="Examples", task_name="create_artifact")

# Tạo file local test
local_file = "sample.json"
with open(local_file, "w") as f:
    f.write('{"message": "Hello ClearML"}')

# Upload file như artifact
task1.upload_artifact(name="data file", artifact_object=local_file)
print("Uploaded artifact:", local_file)

# Kết thúc task
task1.close()
