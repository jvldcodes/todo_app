# import io
import json
import os
import sys

TODO_FILE = os.path.expanduser("~/Desktop/todo_app/tasks.json")


def run():
    def command_line():
        command = input("")
        if command == ":a":
            os.system("clear")
            create_task()
        elif command == ":l":
            os.system("clear")
            read_tasks()
        elif command == ":u":
            os.system("clear")
            update_task()
        elif command == ":d":
            os.system("clear")
            delete_task()
        elif command == ":q":
            os.system("clear")
            sys.exit()
        else:
            command = input("Incorrect usage. (ex.: :a, :l, :u, :d, :q)\n")

    def home_screen():
        check_for_json()
        print("Todo CLI app\n")
        print("- Add a new task - :a\n")
        print("- Check current list - :l\n")
        print("- Update task - :u\n")
        print("- Delete a task - :d\n")
        print("- Quit - :q\n")
        command_line()

    def check_for_json():
        if os.path.isfile("/home/joao/Desktop/todo_app/tasks_json"):
            pass
        else:
            empty_array = []
            with open("tasks_json", "w", encoding="utf-8") as json_file:
                json.dump(empty_array, json_file)

    def create_task():
        with open("tasks_json", "r", encoding="utf-8") as json_file:
            tasks_data = json.load(json_file)
        task_num = len(tasks_data)
        task_string = input("New task:\n")
        tasks_data.append({"id": (task_num + 1), "task": task_string})
        with open("tasks_json", "w", encoding="utf-8") as json_file:
            json.dump(tasks_data, json_file)
            print("New task added successfully!")
        command_line()

    def read_tasks():
        print("These are your current tasks:\n")
        with open("tasks_json", "r", encoding="utf-8") as json_file:
            tasks_data = json.load(json_file)
        task_num = len(tasks_data)
        for i in range(task_num):
            print(str(tasks_data[i]["id"]) + ". " + tasks_data[i]["task"] + "\n")
        after_list = input("Press :h to go back to home or Enter to continue: ")
        if after_list == ":h":
            home_screen()
        else:
            pass

    def update_task():
        read_tasks()
        update_id = int(
            input("Select the task you want to update (ex: 1 for task No. 1, etc):\n")
        )
        with open("tasks_json", "r", encoding="utf-8") as json_file:
            tasks_data = json.load(json_file)
        updated_task = input("Updated Task:\n")
        tasks_data[(update_id - 1)] = {"id": update_id, "task": updated_task}
        with open("tasks_json", "w", encoding="utf-8") as json_file:
            json.dump(tasks_data, json_file)
            print("Task Updated successfully!")
        command_line()

    def delete_task():
        read_tasks()
        deleted_task = int(
            input("Select the task you want to delete (ex: 1 for task No. 1, etc):\n")
        )
        with open("tasks_json", "r", encoding="utf-8") as json_file:
            tasks_data = json.load(json_file)
        new_tasks_data = [
            {**d, "id": index}
            for index, d in enumerate(
                (item for item in tasks_data if item.get("id") != deleted_task), start=1
            )
        ]
        with open("tasks_json", "w", encoding="utf-8") as json_file:
            json.dump(new_tasks_data, json_file)
            print("Task deleted successfully!")
        command_line()

    home_screen()
    if __name__ == "__main__":
        run()
