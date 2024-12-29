import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import shutil
from PIL import Image, ImageTk
import pyperclip

class PortfolioManager:
  def __init__(self, root):
      self.root = root
      self.root.title("Portfolio Project Manager")
      self.root.geometry("800x800")
      
      # Data storage
      self.images = []  # List of {path, caption, preview, original_path}
      self.current_preview = None
      
      # Create main container
      main_frame = ttk.Frame(root, padding="10")
      main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
      
      # Project details
      ttk.Label(main_frame, text="Project Name:").grid(row=0, column=0, sticky=tk.W, pady=5)
      self.project_name = ttk.Entry(main_frame, width=40)
      self.project_name.grid(row=0, column=1, columnspan=2, sticky=tk.W, pady=5)
      
      ttk.Label(main_frame, text="Project ID:").grid(row=1, column=0, sticky=tk.W, pady=5)
      self.project_id = ttk.Entry(main_frame, width=40)
      self.project_id.grid(row=1, column=1, columnspan=2, sticky=tk.W, pady=5)
      
      ttk.Label(main_frame, text="Tags (comma-separated):").grid(row=2, column=0, sticky=tk.W, pady=5)
      self.tags = ttk.Entry(main_frame, width=40)
      self.tags.grid(row=2, column=1, columnspan=2, sticky=tk.W, pady=5)

      ttk.Label(main_frame, text="Project Description:").grid(row=3, column=0, sticky=tk.W, pady=5)
      self.project_description = ttk.Entry(main_frame, width=40)
      self.project_description.grid(row=3, column=1, columnspan=2, sticky=tk.W, pady=5)

      ttk.Label(main_frame, text="Project Statement:").grid(row=4, column=0, sticky=tk.W, pady=5)
      self.statement = tk.Text(main_frame, width=40, height=4)
      self.statement.grid(row=4, column=1, columnspan=2, sticky=tk.W, pady=5)
      
      # Image management
      ttk.Button(main_frame, text="Add Images", command=self.add_images).grid(row=6, column=0, pady=10)
      
      # Image list
      self.image_frame = ttk.Frame(main_frame)
      self.image_frame.grid(row=7, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))
      
      # Scrollbar for image list
      self.canvas = tk.Canvas(self.image_frame)
      scrollbar = ttk.Scrollbar(self.image_frame, orient="vertical", command=self.canvas.yview)
      self.scrollable_frame = ttk.Frame(self.canvas)
      
      self.canvas.configure(yscrollcommand=scrollbar.set)
      
      scrollbar.pack(side="right", fill="y")
      self.canvas.pack(side="left", fill="both", expand=True)
      self.canvas_frame = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
      
      self.scrollable_frame.bind("<Configure>", self.on_frame_configure)
      self.canvas.bind("<Configure>", self.on_canvas_configure)
      
      # Save button
      ttk.Button(main_frame, text="Save Project", command=self.save_project).grid(row=8, column=0, columnspan=3, pady=10)
      
  def on_frame_configure(self, event=None):
      self.canvas.configure(scrollregion=self.canvas.bbox("all"))
      
  def on_canvas_configure(self, event):
      self.canvas.itemconfig(self.canvas_frame, width=event.width)
      
  def create_thumbnail(self, image_path):
    """Create a thumbnail while preserving aspect ratio"""
    with Image.open(image_path) as img:
      # Calculate aspect ratio
      aspect_ratio = img.height / img.width
      # Set thumbnail height
      thumb_width = 100
      thumb_height = int(thumb_width * aspect_ratio)
      # Create thumbnail
      img_copy = img.copy()
      img_copy.thumbnail((thumb_width, thumb_height))
      return ImageTk.PhotoImage(img_copy)
      
  def add_images(self):
      file_paths = filedialog.askopenfilenames(
          title="Select Images",
          filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")]
      )
      
      for path in file_paths:
          preview = self.create_thumbnail(path)
          self.images.append({
              "original_path": path,
              "caption": "",
              "preview": preview
          })
      
      self.update_image_list()
      
  def update_image_list(self):
      # Clear existing widgets
    for widget in self.scrollable_frame.winfo_children():
        widget.destroy()
          
      # Recreate image list
    for i, img_data in enumerate(self.images):
      frame = ttk.Frame(self.scrollable_frame)
      frame.pack(fill=tk.X, pady=5)
      
      # Preview
      preview_label = ttk.Label(frame, image=img_data["preview"])
      preview_label.grid(row=0, column=0, rowspan=2, padx=5)
      
      # File name
      file_name = os.path.basename(img_data["original_path"])
      ttk.Label(frame, text=file_name).grid(row=1, column=1, sticky=tk.W)
      
      # Caption
      caption_var = tk.StringVar(value=img_data["caption"])
      caption_entry = ttk.Entry(frame, textvariable=caption_var)
      caption_entry.grid(row=0, column=1, sticky=tk.W+tk.E)
      
      def update_caption(index, var):
        self.images[index]["caption"] = var.get()
      
      caption_var.trace("w", lambda *args, i=i, v=caption_var: update_caption(i, v))
      
      # Control buttons
      btn_frame = ttk.Frame(frame)
      btn_frame.grid(row=0, column=2, padx=5)
      
      if i > 0:
        ttk.Button(btn_frame, text="↑", width=3, command=lambda x=i: self.move_image(x, "up")).pack(side=tk.LEFT)
      
      if i < len(self.images) - 1:
        ttk.Button(btn_frame, text="↓", width=3, command=lambda x=i: self.move_image(x, "down")).pack(side=tk.LEFT)
          
      ttk.Button(btn_frame, text="X", width=3, command=lambda x=i: self.remove_image(x)).pack(side=tk.LEFT)
          
  def move_image(self, index, direction):
    if direction == "up" and index > 0:
      self.images[index], self.images[index-1] = self.images[index-1], self.images[index]
    elif direction == "down" and index < len(self.images) - 1:
      self.images[index], self.images[index+1] = self.images[index+1], self.images[index]
    self.update_image_list()
      
  def remove_image(self, index):
    del self.images[index]
    self.update_image_list()
        
  def save_project(self):
    if not self.project_name.get() or not self.project_id.get():
      messagebox.showerror("Error", "Project name and ID are required!")
      return
        
    # Create project directory structure
    project_dir = f"projects"
    assets_dir = f"assets/{self.project_id.get()}"
    
    os.makedirs(project_dir, exist_ok=True)
    os.makedirs(assets_dir, exist_ok=True)
    
    # Save images
    for i, img_data in enumerate(self.images):
      output_path = os.path.join(assets_dir, f"img{str(i).zfill(2)}.png")
      # Copy and convert the original image
      with Image.open(img_data["original_path"]) as img:
        img.save(output_path, "PNG", quality=100)
    
    # Generate HTML
    html_content = self.generate_project_html()
    
    with open(os.path.join(project_dir, f"{self.project_id.get()}.html"), "w", encoding="utf-8") as f:
      f.write(html_content)
        

    pastable_html = self.generate_index_html()
    pyperclip.copy(pastable_html)

    messagebox.showinfo("Success", "Project saved successfully, paste the clipboard in index.html!")
        
  def generate_project_html(self):
    statement_text = self.statement.get("1.0", tk.END).strip()
    paragraphs = [p.strip() for p in statement_text.split('\n') if p.strip()]
    statement_html = "".join([f'      <p>{p}</p>\n' for p in paragraphs])

    image_grid = "\n".join([
            f'''        <div class="image-wrapper">
          <img src="../assets/{self.project_id.get()}/img{str(i).zfill(2)}.png" alt="{img['caption']}" onclick="openModal(this.src, 'image', this.nextElementSibling.textContent)">
          <p class="image-caption"><center>{img['caption']}</center></p>
        </div>
'''
      for i, img in enumerate(self.images)
    ])
        
    tag_html = "".join([f'<span class="tag">{tag.strip()}</span>' for tag in self.tags.get().split(',') if tag.strip()])
        
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{self.project_name.get()} - Portfolio</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../styles.css">
</head>
<body>
  <div class="project-container">
    <div>
      <a href="../index.html" class="back-link">← Back to Portfolio</a>
      <div class="image-grid">
{image_grid}
      </div>
    </div>

    <div class="project-info">
      <h2>{self.project_name.get()}</h2>
        <div class="tags">
          {tag_html}
        </div>
{statement_html}
    </div>
  </div>

  <div class="modal" id="imageModal">
    <button class="close-modal" onclick="closeModal()">×</button>
    <div id="modalContent"></div>
    <p id="modalCaption" class="image-caption"></p>
  </div>

  <footer>
    <div class="footer-content">
      <p>© 2024 barkolorious</p>
      <p class="last-updated">Last updated: <span id="lastUpdated">December 28, 2024</span></p>
    </div>
  </footer>

  <script src="../script.js"></script>
</body>
</html>'''

  def generate_index_html(self):
    tag_html = "".join([f'<span class="tag">{tag.strip()}</span>' for tag in self.tags.get().split(',') if tag.strip()])

    return f'''<a href="projects/{self.project_id.get()}.html" class="portfolio-item">
      <div class="image-container">
        <img src="assets/{self.project_id.get()}/img00.png" alt="{self.project_name.get()}">
      </div>
      <div class="item-content">
        <h2>{self.project_name.get()}</h2>
        <div class="tags">
          {tag_html}
        </div>
        <p>{self.project_description.get()}</p>
      </div>
    </a>
'''


def main():
    root = tk.Tk()
    app = PortfolioManager(root)
    root.mainloop()

if __name__ == "__main__":
    main()