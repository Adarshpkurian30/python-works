import tkinder as tk
from PIL import Image,ImageTk
class imageprocessor(tk.Tk):
  def __init__(self):
    super().__init__():
    self.title('image processing tool simulation')
    self.geometry("300*200")
    self.label1=tk.label(self,text="hello,guys!!!")
    self.label1.pack(pady=100)
    self.button1=tk.Button(self,text="black and white",command=self.black)
    self.input_imge=Image.open("cat.png")
    self.tk_photo=ImageTk.PhotoImage(self.input_image)
    self.label.config(input_image=self.tk_photo)
    def black(self):
      y=self.input_image.height()
      x=self.input_image.width()
      for i in range(0,y-1):
        for j in range(0,x-1):
          r,g,b=self.input_image.getpixel((x,y))
          average=(r+g+b)//3
          if average < 177:
            self.input_image.putpixel((x,y),(0,0,0))
          else:
            input_image.putpixel((x,y),(255,255,255))
          self.photo_bw=ImageTk.PhotoImage(self.input_image)
          self.label.config(input_image=self.photo_bw)
if __name__=="__main__":
  app=imageprocessor()
  app.mainloop()

          
            
          
    
                        
    

