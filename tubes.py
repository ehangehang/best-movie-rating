import pandas as pd
import time

def swap(data, i, j):
    temp = data.iloc[[i]]
    data.iloc[[i]] = data.iloc[[j]]
    data.iloc[[j]] = temp
    
def bubbleSort(dataset):
    for i in range(len(dataset.index)):
        for j in range(len(dataset.index)-i-1):
            if (dataset.iloc[[j+1]]["averageRating"].reset_index(drop=True) > dataset.iloc[[j]]["averageRating"].reset_index(drop=True)).bool():
                swap(dataset, j, j+1)

def partition(dataset, start, end):
    pivot = dataset.iloc[[start]]["averageRating"]
    left = start + 1
    right = end

    while True:
        while left <= right and (dataset.iloc[[right]]["averageRating"].reset_index(drop=True) <= pivot.reset_index(drop=True)).bool():
            right -= 1
        while left <= right and (dataset.iloc[[left]]["averageRating"].reset_index(drop=True) >= pivot.reset_index(drop=True)).bool():
            left += 1

        if left <= right:
            swap(dataset, left, right)
        else:
            break
        
    swap(dataset, start, right)

    return right

def quickSort(dataset, left, right):
    if left >= right:
        return
    
    p = partition(dataset, left, right)
    quickSort(dataset, left, p-1)
    quickSort(dataset, p+1, right)

if __name__ == '__main__':
    dataset = pd.read_csv("./datasets/1000.csv")
    dataset["genres"] = dataset["genres"].astype("string")

    dataset_genre = pd.DataFrame()
    print("Masukkan Genre yang diinginkan: ")
    input_genre = input()
    input_genre = input_genre.capitalize()


    time_start_grouping = time.time()
    for i in range(len(dataset.index)):
        if not(pd.isna(dataset["genres"][i])):
            if "," in dataset["genres"][i]:
                genre = dataset["genres"][i].split(",")
                for j in range(len(genre)):
                    if input_genre == genre[j]:
                        dataset_genre = dataset_genre.append(dataset.iloc[[i]])
    dataset_genre.reset_index(drop=False)
    print(dataset_genre, "\n")
    print("grouping runtime:", (time.time() - time_start_grouping))
    
    time_start = time.time()
    bubbleSort(dataset_genre)
    # quickSort(dataset_genre, 0, len(dataset_genre.index)-1)

    print("\nFilm terbaik dengan genre", input_genre, "adalah:")
    print(dataset_genre.iloc[[0]], "\n")

    print("Pilihan film lain berdasarkan genre", input_genre, "yang lain:")
    print(dataset_genre.head(11))

    print("sorting runtime:", (time.time() - time_start))
