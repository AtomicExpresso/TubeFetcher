import customtkinter as ctk
from utils.config import Config
from utils.utils import Utils
from PIL import Image


# Handles creating app widgets
class AppWidgets:
    def __init__(self, parent):
        self.parent = parent

    def create_images(self):
        #Ensures resource path is correct
        settingsImgPath = Utils.get_resource_path("images/settings.png")
        folderImgPath = Utils.get_resource_path("images/folder.png")
        trashImgPath = Utils.get_resource_path("images/trash.png")
        plusImgPath = Utils.get_resource_path("images/plus.png")

        settingsImgSrc = Image.open(settingsImgPath)
        folderImgSrc = Image.open(folderImgPath)
        trashImgSrc = Image.open(trashImgPath)
        plusImgSrc = Image.open(plusImgPath)

        self.settingsImg = ctk.CTkImage(light_image=settingsImgSrc, size=(20, 20))
        self.folderImg = ctk.CTkImage(light_image=folderImgSrc, size=(20, 20))
        self.trashImg = ctk.CTkImage(light_image=trashImgSrc, size=(20, 20))
        self.plusImg = ctk.CTkImage(light_image=plusImgSrc, size=(20, 20))

    # create widgets for progress frame
    def create_progress_widgets(self):
        # labels
        self.download_progress_txt = ctk.CTkLabel(
            self.parent.frames.progress_frame,
            text="0%",
            text_color=Config.theme["text_colors"]["primary"],
            fg_color=Config.theme["colors"]["primary"],
            font=("ariel", 20),
        )
        self.error_txt = ctk.CTkLabel(
            self.parent.frames.progress_frame,
            text_color=f"{Config.theme["colors"]["error"]}",
            text="Error",
            fg_color="transparent",
            font=("ariel", 20),
        )
        # progress bar
        self.download_progress_bar = ctk.CTkProgressBar(
            self.parent.frames.progress_frame,
            progress_color=f"{Config.theme["colors"]["progress"]}",
            fg_color=Config.theme["colors"]["primary"],
            bg_color=Config.theme["colors"]["primary"],
            orientation="horizontal",
            width=250,
        )

    # create widgets for top frame
    def create_top_widgets(self):
        # input box
        self.input = ctk.CTkEntry(
            self.parent.frames.top_frame,
            border_width=0,
            height=30,
            corner_radius=0,
            fg_color=Config.theme["colors"]["button"]["default"],
            text_color=Config.theme["text_colors"]["primary"],
            placeholder_text="Video URL",
        )
        # Add videos to que button
        self.addvideo_btn = ctk.CTkButton(
            self.parent.frames.top_frame,
            image=self.plusImg,
            fg_color=f"{Config.theme["colors"]["secondary"]}",
            hover_color=f"{Config.theme["colors"]["button"]["default"]}",
            text="",
            bg_color="transparent",
            corner_radius=0,
            width=45,
            command=self.parent.add_video_clbck,
        )
        # Settings button
        self.settings_btn = ctk.CTkButton(
            self.parent.frames.top_frame,
            image=self.settingsImg,
            fg_color=f"{Config.theme["colors"]["secondary"]}",
            hover_color=f"{Config.theme["colors"]["button"]["default"]}",
            text="",
            width=45,
            command=self.parent.st_clbck,
        )

    # create widgets for bottom frame
    def create_bottom_widgets(self):
        # buttons
        self.download_button = ctk.CTkButton(
            self.parent.frames.bottom_frame,
            text="Download",
            fg_color=f"{Config.theme["colors"]["button"]["download"]["default"]}",
            hover_color=f"{Config.theme["colors"]["button"]["download"]["hover"]}",
            command=self.parent.download_btn_clbck,
        )
        # App download option
        self.options = ctk.CTkOptionMenu(
            self.parent.frames.bottom_frame,
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
        # Folder button for file path
        self.folder_btn = ctk.CTkButton(
            self.parent.frames.bottom_frame,
            fg_color=f"{Config.theme["colors"]["secondary"]}",
            hover_color=f"{Config.theme["colors"]["button"]["default"]}",
            image=self.folderImg,
            text="",
            width=45,
            command=self.parent.folder_path_clbck,
        )
        # Trash button
        self.trash_btn = ctk.CTkButton(
            self.parent.frames.bottom_frame,
            image=self.trashImg,
            fg_color=f"{Config.theme["colors"]["secondary"]}",
            hover_color=f"{Config.theme["colors"]["button"]["default"]}",
            text="",
            width=45,
            command=self.parent.clear_mf_clbck,
        )

    # creates all widgets
    def create_widgets(self):
        # top frame widgets
        self.create_top_widgets()
        # Progress frame widgets
        self.create_progress_widgets()
        # Bottom frame widgets
        self.create_bottom_widgets()
