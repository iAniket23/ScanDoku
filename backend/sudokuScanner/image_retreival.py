import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

# function to greyscale, blur and change the receptive threshold of image
def preprocess(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    blur = cv2.GaussianBlur(gray, (3,3),6) 
    threshold_img = cv2.adaptiveThreshold(blur,255,1,1,11,2)
    return threshold_img

def main_outline(contour):
    biggest = np.array([])
    max_area = 0
    for i in contour:
        area = cv2.contourArea(i)
        if area > 50:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02*peri, True)
            if area > max_area and len(approx) == 4:
                biggest = approx
                max_area = area
    return biggest, max_area

def reframe(points):
    points = points.reshape((4,2))
    points_new = np.zeros((4,1,2), dtype = np.int32)
    add = points.sum(1)
    points_new[0] = points[np.argmin(add)]
    points_new[3] = points[np.argmax(add)]
    diff = np.diff(points, axis = 1)
    points_new[1] = points[np.argmin(diff)]
    points_new[2] = points[np.argmax(diff)]
    return points_new

def splitcells(img):
    rows = np.vsplit(img, 9)
    boxes = []
    for r in rows:
        cols = np.hsplit(r, 9)
        for box in cols:
            boxes.append(box)
    return boxes

# The sudoku cell's output contains the boundaries which could lead to misclassifications by the model
# Cropping the cells to avoid that

def CropCell(cells):
    cells_cropped = []
    for image in cells:
        img = np.array(image)
        img = img[4:46, 6:46]
        img = Image.fromarray(img)
        cells_cropped.append(img)
    return cells_cropped

def contour_detection(puzzle):
    sudoku_a = cv2.imread('sudoku.jpg')
    #Preprocessing image to be read
    sudoku_a = cv2.resize(sudoku_a, (450,450))
    threshold = preprocess(sudoku_a)
    # Finding the outline of the puzzle in the sudoku image
    contour_1 = sudoku_a.copy()
    contour_2 = sudoku_a.copy()
    contour = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    cv2.drawContours(contour_1, contour, -1, (0,255,0), 3)
    biggest = main_outline(contour)[0]
    if biggest.size != 0:
        biggest = reframe(biggest)
        cv2.drawContours(contour_2, biggest, -1, (0,255,0), 10)
        pts1 = np.float32(biggest)
        pts2 = np.float32([[0,0],[450,0],[0,450],[450,450]])
        matrix = cv2.getPerspectiveTransform(pts1, pts2)
        imagewrap = cv2.warpPerspective(sudoku_a, matrix, (450,450))
        imagewrap = cv2.cvtColor(imagewrap, cv2.COLOR_BGR2GRAY)

    # Resizing the puzzle to be solved
    puzzle = cv2.resize(puzzle, (450, 450))

    # Preprocessing puzzle
    su_puzzle = preprocess(puzzle)

    # Finding the outline of the sudoku puzzle in the image
    su_contour_1 = su_puzzle.copy()
    su_contour_2 = sudoku_a.copy()
    su_contour = cv2.findContours(su_puzzle, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
    cv2.drawContours(su_contour_1, su_contour, -1, (0,255,0), 3)
    su_biggest = main_outline(su_contour)[0]
    if su_biggest.size != 0:
        su_biggest = reframe(su_biggest)
        cv2.drawContours(su_contour_2,su_biggest,-1, (0,255,0),10)
        su_pts1 = np.float32(su_biggest)
        su_pts2 = np.float32([[0,0],[450,0],[0,450],[450,450]])
        su_matrix = cv2.getPerspectiveTransform(su_pts1,su_pts2)  
        su_imagewrap = cv2.warpPerspective(puzzle,su_matrix,(450,450))
        su_imagewrap = cv2.cvtColor(su_imagewrap, cv2.COLOR_BGR2GRAY)

    sudoku_cell = splitcells(su_imagewrap)
    sudoku_cell_cropped = CropCell(sudoku_cell)

    return sudoku_cell_cropped

   


