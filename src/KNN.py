import numpy as np
from PIL import Image , ImageOps , ImageDraw
import tkinter as tk
from sklearn.datasets import fetch_openml



#main program
mnist = fetch_openml('mnist_784' , version=1 , as_frame=False , parser ="liac-arff")
X ,y = mnist["data"] , mnist["target"]
X =X/255.0
X_train ,Y_train = X[:10000] , y[:10000]
X_test ,Y_test = X[1000:1010] , y[1000:1010]

k=10




def predict_one(b,X_train , Y_train , k ):
    
    distance = np.linalg.norm( X_train - b  , axis = 1)
    index = np.argsort(distance)
    final = Y_train[index[:k]]

    unique , counts = np.unique(final , return_counts=True )

    return unique[np.argmax(counts)]

count =0
for i in range (10):
    b= X_test[i]   
    predict = predict_one(b,X_train , Y_train , k)
   #print(predict)
    #print(Y_test[i])
    if predict == Y_test[i] :
        count = count +1

print(count/10)


# board (not completed yet, have some issues)

bg_image = Image.new("L", (280, 280), 255)
draw_handle = ImageDraw.Draw(bg_image)

root = tk.Tk()
root.title("AI DIgit Recoginzer")
canvas = tk.Canvas(root,width=280 ,height =280 , bg="white")
canvas.pack()

def draw(event):
    x,y= event.x , event.y
    canvas.create_oval(x-8,y-8,x+8,y+8 , fill="black", outline="black")
    draw_handle.ellipse([x-8, y-8, x+8, y+8], fill=0)

canvas.bind("<B1-Motion>",draw)

def process(Image_path):
    img = Image.open(Image_path).convert("L")
    img = ImageOps.invert(img)
    bbox = img.getbbox() 
    if bbox:
        img = img.crop(bbox)
    img = img.resize((28,28))

    img.thumbnail((20, 20), Image.Resampling.LANCZOS)
    
    new_img = Image.new("L", (28, 28), 0)
    w, h = img.size
    new_img.paste(img, ((28 - w) // 2, (28 - h) // 2))
    
    img_array = np.array(new_img) / 255.0
    return img_array.flatten()

def submit():
    bg_image.save("user_drawing.png")
    processed_img = process("user_drawing.png")
    print(np.shape(processed_img))
    print(np.size(processed_img))
    prediction = predict_one(processed_img, X_train, Y_train, k)
    print(f"Prediction: {prediction}")

    print("summited")
    
submit_btn= tk.Button(root , text = "predict Digit" , command = submit)

def clear_canvas():
    global bg_image, draw_handle 
    canvas.delete("all")
    bg_image = Image.new("L", (280, 280), 255)
    draw_handle = ImageDraw.Draw(bg_image)

clear_btn = tk.Button(root, text="Clear Canvas", command=clear_canvas)
clear_btn.pack()
submit_btn.pack()

root.mainloop()


