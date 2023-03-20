import json
import tkinter as tk

from subtitle_automater import *


def ui_root():
    def get_sync_amount():
        sync_amount = sync_amount_entry.get()
        source_folder = source_file_path_entry.get()
        target_folder = target_file_path_entry.get()
        file_list = show_files_in_folder(source_folder)
        sync_subtitles(sync_amount, file_list, source_folder, target_folder)

    def save_paths():
        with open("save_paths.json", "w") as f:
            json.dump(
                {
                    "target_folder": target_file_path_entry.get(),
                    "source_folder": source_file_path_entry.get(),
                },
                f,
            )

    def load_paths():
        if os.path.exists("save_paths.json"):
            with open("save_paths.json", "r") as f:
                data = json.load(f)
        else:
            data = {
                "target_folder": "/",
                "source_folder": "/",
            }
        return data

    target_folder, source_folder = load_paths().values()

    style = {"padx": 3, "pady": 3}

    root = tk.Tk()
    root.title("Sync subtitles")
    root.configure(bg="#d3d3d3")

    label_sync_amount = tk.Label(root, text="Amount to shift in ms")
    label_sync_amount.pack(**style, fill=tk.X)
    sync_amount_entry = tk.Entry(root)
    sync_amount_entry.pack(**style, fill=tk.X)

    label_file_path = tk.Label(root, text="Source folder, like: E:/_DL/_Subs/")
    label_file_path.pack(**style, fill=tk.X)
    source_file_path_entry = tk.Entry(root)
    source_file_path_entry.pack(**style, fill=tk.X)
    source_file_path_entry.insert(0, source_folder)

    label_target_file_path = tk.Label(root, text="Target folder")
    label_target_file_path.pack(**style, fill=tk.X)
    target_file_path_entry = tk.Entry(root)
    target_file_path_entry.pack(**style, fill=tk.X)
    target_file_path_entry.insert(0, target_folder)

    save_paths_button = tk.Button(root, text="Save", width=25, command=save_paths)
    save_paths_button.pack(**style, side="left")

    sync_subs_button = tk.Button(root, text="Sync", width=25, command=get_sync_amount)
    sync_subs_button.pack(**style, side="right")

    root.mainloop()
