from tkinter.font import BOLD
import customtkinter as ctk
from utils.config import Config
from utils.utils import Utils


# handles popups
class Window(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.geometry(f"{Config.secondary_win_width}x{Config.secondary_win_height}")


class SettingsWindow(Window):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Settings")
        self.create_widgets()
        self.config_grid()
        self.append_grid()

    def create_widgets(self):
        self.settings_frame = ctk.CTkFrame(
            self, fg_color=f"{Config.theme["colors"]["primary"]}"
        )
        self.settings_fp_frame = ctk.CTkFrame(
            self.settings_frame, fg_color=f"{Config.theme["colors"]["primary"]}"
        )

        self.defLbl = ctk.CTkLabel(
            self.settings_frame,
            text="General",
            text_color=Config.theme["text_colors"]["primary"],
            font=("ariel", 20, BOLD),
        )
        self.resLbl = ctk.CTkLabel(
            self.settings_frame,
            text_color=Config.theme["text_colors"]["primary"],
            text="Resolution:",
        )
        self.dowLbl = ctk.CTkLabel(
            self.settings_frame,
            text_color=Config.theme["text_colors"]["primary"],
            text="Download Type:",
        )
        # Download options menu, inherits from config
        self.opt = ctk.CTkOptionMenu(
            self.settings_frame,
            fg_color=f"{Config.theme["colors"]["secondary"]}",
            bg_color=f"{Config.theme["colors"]["secondary"]}",
            dropdown_fg_color=f"{Config.theme["colors"]["button"]["default"]}",
            dropdown_text_color=f"{Config.theme["text_colors"]["primary"]}",
            dropdown_hover_color=f"{Config.theme["colors"]["primary"]}",
            button_color=f"{Config.theme["colors"]["button"]["hover"]}",
            button_hover_color=f"{Config.theme["colors"]["button"]["hover"]}",
            values=[*Config.dl_options],
            command=self.parent.set_dl_option_clbck,
        )
        # Resoultion options menu, inherits from config
        self.res_opt = ctk.CTkOptionMenu(
            self.settings_frame,
            fg_color=f"{Config.theme["colors"]["secondary"]}",
            bg_color=f"{Config.theme["colors"]["secondary"]}",
            dropdown_fg_color=f"{Config.theme["colors"]["button"]["default"]}",
            dropdown_text_color=f"{Config.theme["text_colors"]["primary"]}",
            dropdown_hover_color=f"{Config.theme["colors"]["primary"]}",
            button_color=f"{Config.theme["colors"]["button"]["hover"]}",
            button_hover_color=f"{Config.theme["colors"]["button"]["hover"]}",
            values=[*Config.res_options],
            command=self.parent.set_dl_option_clbck,
        )
        # file path
        self.fpLbl = ctk.CTkLabel(
            self.settings_fp_frame,
            text_color=Config.theme["text_colors"]["primary"],
            text="Downloads folder:",
        )
        self.fpBtn = ctk.CTkButton(
            self.settings_fp_frame,
            fg_color=f"{Config.theme["colors"]["secondary"]}",
            hover_color=f"{Config.theme["colors"]["button"]["default"]}",
            text="Change",
            width=45,
            command=self.parent.folder_path_clbck,
        )
        self.viewFpBtn = ctk.CTkButton(
            self.settings_fp_frame,
            fg_color=f"{Config.theme["colors"]["secondary"]}",
            hover_color=f"{Config.theme["colors"]["button"]["default"]}",
            text="View",
            width=45,
            command=lambda: Utils.create_dialog_notfication(
                f"Current download folder:\n{Config.folder_path}"
            ),
        )
        # -Appearance
        self.appearanceLbl = ctk.CTkLabel(
            self.settings_frame,
            text="Appearance",
            text_color=Config.theme["text_colors"]["primary"],
            font=("ariel", 20, BOLD),
        )
        self.themeLbl = ctk.CTkLabel(
            self.settings_frame,
            text_color=Config.theme["text_colors"]["primary"],
            text="Theme:",
        )
        # Theme options menu, inherits from config
        self.theme_opt = ctk.CTkOptionMenu(
            self.settings_frame,
            fg_color=f"{Config.theme["colors"]["secondary"]}",
            bg_color=f"{Config.theme["colors"]["secondary"]}",
            dropdown_fg_color=f"{Config.theme["colors"]["button"]["default"]}",
            dropdown_text_color=f"{Config.theme["text_colors"]["primary"]}",
            dropdown_hover_color=f"{Config.theme["colors"]["primary"]}",
            button_color=f"{Config.theme["colors"]["button"]["hover"]}",
            button_hover_color=f"{Config.theme["colors"]["button"]["hover"]}",
            values=[*Config.theme_options],
            command=self.parent.set_dl_option_clbck,
        )

    def config_grid(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.settings_frame.grid_columnconfigure(0, weight=0)
        self.settings_frame.grid_rowconfigure(1, weight=0)
        self.settings_frame.grid_rowconfigure(2, weight=0)
        self.settings_frame.grid_rowconfigure(3, weight=0)
        self.settings_frame.grid_rowconfigure(4, weight=0)
        self.settings_frame.grid_rowconfigure(5, weight=0)
        self.settings_frame.grid_rowconfigure(6, weight=0)

    def append_grid(self):
        self.settings_frame.grid(row=0, columnspan=3, column=0, sticky="nsew")

        self.defLbl.grid(
            row=1, column=0, columnspan=3, padx=(10, 0), pady=(20, 0), sticky="w"
        )

        self.resLbl.grid(row=2, column=0, padx=(10, 0), pady=(0, 0), sticky="w")
        self.res_opt.grid(row=2, column=1, padx=(10, 10), pady=(10, 10), sticky="w")

        self.dowLbl.grid(row=3, column=0, padx=(10, 0), pady=(0, 0), sticky="w")
        self.opt.grid(row=3, column=1, padx=(10, 10), pady=(10, 10), sticky="w")

        self.settings_fp_frame.grid(row=4, columnspan=3, column=0, sticky="nsew")
        self.fpLbl.grid(row=0, column=0, padx=(10, 0), pady=(0, 0), sticky="w")
        self.fpBtn.grid(row=0, column=1, padx=(10, 0), pady=(0, 0), sticky="w")
        self.viewFpBtn.grid(row=0, column=2, padx=(10, 0), pady=(0, 0), sticky="w")
        # Apperance
        self.appearanceLbl.grid(
            row=5, column=0, columnspan=3, padx=(10, 0), pady=(20, 0), sticky="w"
        )
        self.themeLbl.grid(row=6, column=0, padx=(10, 0), pady=(0, 0), sticky="w")
        self.theme_opt.grid(row=6, column=1, padx=(10, 10), pady=(10, 10), sticky="w")


class InfoWindow(Window):
    def __init__(self, parent, index: int):
        super().__init__(parent)
        self.parent = parent
        self.index = index
        self.title("Video Info")

        self.create_info_widgets()

    # fetchs video info from app vid queue
    def fetch_info(self) -> None:
        self.info: dict = self.parent.vid_queue[self.index]

    def create_info_frames(self) -> None:
        # Main info frame
        self.info_window_frame = ctk.CTkScrollableFrame(
            self,
            fg_color=f"{Config.theme["colors"]["primary"]}",
            scrollbar_button_color=f"{Config.theme["colors"]["secondary"]}",
            scrollbar_button_hover_color=f"{Config.theme["colors"]["secondary"]}",
        )
        # Attribute frame
        self.info_attr_frame = ctk.CTkFrame(
            self.info_window_frame, fg_color=f"{Config.theme["colors"]["primary"]}"
        )
        # Description frame
        self.info_desc_frame = ctk.CTkFrame(
            self.info_window_frame, fg_color=f"{Config.theme["colors"]["primary"]}"
        )

    def create_info_labels(self) -> None:
        # video title
        self.titleLbl = ctk.CTkLabel(
            self.info_attr_frame,
            text_color=Config.theme["text_colors"]["primary"],
            text=f"Title:",
            font=("ariel", 14, BOLD),
        )
        self.titleContentLbl = ctk.CTkLabel(
            self.info_attr_frame,
            text_color=Config.theme["text_colors"]["primary"],
            text=f"{self.info["title"]}",
        )
        # Video author
        self.authorLbl = ctk.CTkLabel(
            self.info_attr_frame,
            text=f"Author:",
            text_color=Config.theme["text_colors"]["primary"],
            font=("ariel", 14, BOLD),
        )
        self.authorContentLbl = ctk.CTkLabel(
            self.info_attr_frame,
            text_color=Config.theme["text_colors"]["primary"],
            text=f"{self.info["author"]}",
        )
        # Video duriation
        self.duriationLbl = ctk.CTkLabel(
            self.info_attr_frame,
            text=f"Duriation:",
            text_color=Config.theme["text_colors"]["primary"],
            font=("ariel", 14, BOLD),
        )
        self.duriationContentLbl = ctk.CTkLabel(
            self.info_attr_frame,
            text_color=Config.theme["text_colors"]["primary"],
            text=f"{self.info["duriation"]}",
        )
        # Video file size
        self.sizeLbl = ctk.CTkLabel(
            self.info_attr_frame,
            text=f"Size:",
            text_color=Config.theme["text_colors"]["primary"],
            font=("ariel", 14, BOLD),
        )
        self.sizeContentLbl = ctk.CTkLabel(
            self.info_attr_frame,
            text_color=Config.theme["text_colors"]["primary"],
            text=f"{self.info["size"]}",
        )
        # Video Description
        self.descLbl = ctk.CTkLabel(
            self.info_desc_frame,
            text=f"Description:",
            text_color=Config.theme["text_colors"]["primary"],
            font=("ariel", 14, BOLD),
        )
        # Description content
        self.descContentLbl = ctk.CTkLabel(
            self.info_desc_frame,
            text=f"{self.info["desc"]}",
            text_color=Config.theme["text_colors"]["primary"],
            wraplength=Config.max_paragraph_len,
            justify="left",
        )

    def config_info_grid(self) -> None:
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=0)

        self.info_window_frame.grid_rowconfigure(0, weight=1)
        self.info_window_frame.grid_rowconfigure(1, weight=1)
        self.info_window_frame.grid_rowconfigure(2, weight=1)
        self.info_window_frame.grid_rowconfigure(3, weight=0)

        self.info_attr_frame.grid_columnconfigure(0, weight=0)
        self.info_attr_frame.grid_columnconfigure(1, weight=1)

    def append_info_grid(self) -> None:
        self.info_window_frame.grid(row=0, column=0, sticky="nsew")
        self.info_attr_frame.grid(row=1, column=0, sticky="nsew")
        self.info_desc_frame.grid(row=2, column=0, sticky="nsew")

        self.titleLbl.grid(row=0, column=0, padx=(10, 10), pady=(20, 0), sticky="w")
        self.titleContentLbl.grid(row=0, column=1, pady=(20, 0), sticky="w")

        self.authorLbl.grid(row=1, column=0, padx=(10, 10), pady=(0, 0), sticky="w")
        self.authorContentLbl.grid(row=1, column=1, pady=(0, 0), sticky="w")

        self.duriationLbl.grid(row=2, column=0, padx=(10, 10), pady=(0, 0), sticky="w")
        self.duriationContentLbl.grid(row=2, column=1, pady=(0, 0), sticky="w")

        self.sizeLbl.grid(row=3, column=0, padx=(10, 10), pady=(0, 0), sticky="w")
        self.sizeContentLbl.grid(row=3, column=1, pady=(0, 0), sticky="w")

        self.descLbl.grid(row=0, column=0, padx=(10, 10), pady=(0, 0), sticky="w")
        self.descContentLbl.grid(
            row=1, column=0, padx=(10, 0), pady=(0, 10), sticky="w"
        )

    def create_info_widgets(self) -> None:
        self.fetch_info()
        self.create_info_frames()
        self.create_info_labels()
        self.config_info_grid()
        self.append_info_grid()
