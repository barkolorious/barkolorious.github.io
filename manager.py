import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import shutil
from PIL import Image, ImageTk
import json
from datetime import datetime

class PortfolioManager:
  def __init__(self, root):
    self.root = root
    self.root.title("Portfolio Project Manager")
    self.root.geometry("800x800")
    
    # Data storage
    self.images = []  # List of {path, caption, preview, original_path}
    self.current_preview = None
    self.json_file = "projects.json"
    
    # Create main container
    main_frame = ttk.Frame(root, padding="10")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
    
    # Project details
    ttk.Label(main_frame, text="Project ID:").grid(row=0, column=0, sticky=tk.W, pady=5)
    self.project_id = ttk.Entry(main_frame, width=40)
    self.project_id.grid(row=0, column=1, columnspan=2, sticky=tk.W, pady=5)
    
    ttk.Label(main_frame, text="Project Title:").grid(row=1, column=0, sticky=tk.W, pady=5)
    self.project_title = ttk.Entry(main_frame, width=40)
    self.project_title.grid(row=1, column=1, columnspan=2, sticky=tk.W, pady=5)
    
    ttk.Label(main_frame, text="Tags (comma-separated):").grid(row=2, column=0, sticky=tk.W, pady=5)
    self.tags = ttk.Entry(main_frame, width=40)
    self.tags.grid(row=2, column=1, columnspan=2, sticky=tk.W, pady=5)

    ttk.Label(main_frame, text="Description:").grid(row=3, column=0, sticky=tk.W, pady=5)
    self.description = ttk.Entry(main_frame, width=40)
    self.description.grid(row=3, column=1, columnspan=2, sticky=tk.W, pady=5)

    ttk.Label(main_frame, text="Project Statement:").grid(row=4, column=0, sticky=tk.W, pady=5)
    self.statement = tk.Text(main_frame, width=40, height=4)
    self.statement.grid(row=4, column=1, columnspan=2, sticky=tk.W, pady=5)
    
    # Image management
    ttk.Button(main_frame, text="Add Images", command=self.add_images).grid(row=5, column=0, pady=10)
    ttk.Button(main_frame, text="Load Project", command=self.load_project).grid(row=5, column=1, pady=10)
    
    # Image list
    self.image_frame = ttk.Frame(main_frame)
    self.image_frame.grid(row=6, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S))
    
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
    ttk.Button(main_frame, text="Save Project", command=self.save_project).grid(row=7, column=0, columnspan=3, pady=10)

  def on_frame_configure(self, event=None):
    self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
  def on_canvas_configure(self, event):
    self.canvas.itemconfig(self.canvas_frame, width=event.width)
    
  def create_thumbnail(self, image_path):
    """Create a thumbnail while preserving aspect ratio"""
    with Image.open(image_path) as img:
      aspect_ratio = img.height / img.width
      thumb_width = 100
      thumb_height = int(thumb_width * aspect_ratio)
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

  def load_project(self):
    project_id = self.project_id.get()
    if not project_id:
      messagebox.showerror("Error", "Please enter a project ID to load")
      return
      
    try:
      with open(self.json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
      project = next((p for p in data['projects'] if p['id'] == project_id), None)
      if not project:
        messagebox.showerror("Error", f"Project with ID '{project_id}' not found")
        return
        
      # Load project data into form
      self.project_title.delete(0, tk.END)
      self.project_title.insert(0, project['title'])
      
      self.tags.delete(0, tk.END)
      self.tags.insert(0, ', '.join(project['tags']))
      
      self.description.delete(0, tk.END)
      self.description.insert(0, project['description'])
      
      self.statement.delete('1.0', tk.END)
      self.statement.insert('1.0', '\n'.join(project['statement']))
      
      # Load images
      self.images = []
      for caption in project['captions']:
        idx = len(self.images)
        img_path = f"assets/{project_id}/img{str(idx).zfill(2)}.png"
        if os.path.exists(img_path):
          preview = self.create_thumbnail(img_path)
          self.images.append({
            "original_path": img_path,
            "caption": caption,
            "preview": preview
          })
      
      self.update_image_list()
      messagebox.showinfo("Success", "Project loaded successfully")
      
    except FileNotFoundError:
      messagebox.showerror("Error", "Projects file not found")
    except Exception as e:
      messagebox.showerror("Error", f"Failed to load project: {str(e)}")
    
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
    if not self.project_id.get() or not self.project_title.get():
      messagebox.showerror("Error", "Project ID and title are required!")
      return
      
    try:
      # Create assets directory if it doesn't exist
      assets_dir = f"assets/{self.project_id.get()}"
      os.makedirs(assets_dir, exist_ok=True)
      
      # Save images
      for i, img_data in enumerate(self.images):
        output_path = os.path.join(assets_dir, f"img{str(i).zfill(2)}.png")
        if not img_data["original_path"].endswith(output_path):  # Only copy if it's a new image
          with Image.open(img_data["original_path"]) as img:
            img.save(output_path, "PNG")
      
      # Prepare project data
      project_data = {
        "id": self.project_id.get(),
        "title": self.project_title.get(),
        "tags": [tag.strip() for tag in self.tags.get().split(',') if tag.strip()],
        "description": self.description.get(),
        "statement": [p.strip() for p in self.statement.get("1.0", tk.END).strip().split('\n') if p.strip()],
        "captions": [img["caption"] for img in self.images]
      }
      
      # Load existing projects
      try:
        with open(self.json_file, 'r', encoding='utf-8') as f:
          data = json.load(f)
      except FileNotFoundError:
        data = {"projects": []}
      
      # Update or add project
      project_index = next((i for i, p in enumerate(data['projects']) if p['id'] == project_data['id']), None)
      if project_index is not None:
        data['projects'][project_index] = project_data
      else:
        data['projects'].append(project_data)
      
      # Save updated projects file
      with open(self.json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
      
      messagebox.showinfo("Success", "Project saved successfully!")
      
    except Exception as e:
      messagebox.showerror("Error", f"Failed to save project: {str(e)}")

def main():
  root = tk.Tk()
  app = PortfolioManager(root)
  root.mainloop()

if __name__ == "__main__":
  main()