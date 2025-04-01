import numpy as np
import tkinter as tk
from tkinter import messagebox,simpledialog

def add_matrices(matrix_a,matrix_b):
  return matrix_a + matrix_b
def subtract_matrices(matrix_a,matrix_b):
  return matrix_a - matrix_b
def strassen_multiplication(matrix_a,matrix_b):
  if len(matrix_a)==1:
    return matrix_a * matrix_b
  mid len(matrix_a)//2
  a11,a12,a21,a22=matrix_a[:mid,:mid],matrix_a[:mid,mid:],matrix_a[mid:,:mid]matrix_a[mid:,mid:]
  b11,b12,b21,b22=matrix_b[:mid,:mid],atrix_b[:mid,mid:],matrix_b[mid:,:mid],matrix_b[mid:,mid:]
  p1=strassen_multiplicatiom(a11,subtract_matrices(b12,b22))
  p2=strassen_multiplication(add_matrices(a11,a12),b22)
  p3=strassen_multiplication(add_matrices(a21,a22),b11)
  p4=strassen_multiplication(a22,subtract_matrices(b21,b11))
  p5=strassen_multiplicaton(add_matrices(a11,a22),add_matrices(b11,b22))
  p6 = strassen_multiplication(subtract_matrices(a12, a22), add_matrices(b21, b22))
  p7 = strassen_multiplication(subtract_matrices(a11, a21), add_matrices(b11, b12))

  c11=add_matrices(subtract_matrices(p5,p4),p2)
  c12=add_matrices(p1,p2)
  c21=add_matrices(p3,p4)
  c22=subtract_matrices(subtract_matrices(add_matrices(p5,p1),p3),p7)
  top,bottom =np.hstack((c11,c12)),np.hstack((c21,c22)
  return np.vstack((top,bottom))
def strassen(matrix_a,matrix_b):
  assert matrix_a.shape== matrix.shape
  assert matrix_a.shape[0]==matrix_a.shape[1]
  n,m =matrix_a.shape[0],1
  while m<n:
    m*=2
  if m!=n:
    padded_a,padded_b=np.zeros((m,m)),np.zeros((m,m))
    padded_a[:n,:n],padded_b[:n,:n]=matrix_a,matrix_b
    return strassen_multiplication(padded_a,padded_b)[:n,:n]
  return strassen_multiplication(matrix_a,matrix_b)
def get_matrix_input(size,input):
  matrix=[]
  for i in range(size):
    row =simpledialog.askstring(title,f"Enter row {i+1} (comma-separated):")
    matrix.append(list(map(int,row.split(','))))
  return np.arry(matrix)
def compute_result():
  try:
    size=int(size_entry.get())
    matrix_a=get_matrix_input(size,"Matrix A input")
    matrix_b=get_matrix_input(size,"matrix B input")
    result=strassen(matrix_a,matrix_b)
    messagebox.showinfo("Result",f"Resultant matrix:\n{result}")
  except Exception as e:
    messagebox.showerror("error",str(e))
root=tk.Tk()
root.title("strassen matrix multiplication")
root.geometry("600x400")
tk.Label(root,text="Enter matrix size (NxN):",font=("Arial",14).pack(pady=10))
size_entry=tk.Entry(root,font=("Arial",12))
tk.Button(root,text="compute multiplication",font=("Arial",14),command=compute_result).pack(pady=20))
root.mainloop()
                    

         
         
    
    
    
                              
    
  
  
  
  
  
